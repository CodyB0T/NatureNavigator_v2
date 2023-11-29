import pandas as pd
import serial
import json
from datetime import datetime, timedelta
import os
import time
import queue
import threading


class Lora:
    connected_bool = False

    def __init__(self):
        # Constants for the serial connection
        SERIAL_PORT = "/dev/ttyUSB0"
        BAUD_RATE = 115200

        # Initialize serial connection to the Arduino
        self.ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        self.initialize_LoRaWAN()

        # Create a queue for method calls
        self.method_queue = queue.Queue()

        # Create a thread to process the method queue
        self.thread = threading.Thread(target=self.process_method_queue, daemon=True)
        self.thread.start()

    def add_to_queue(self, method, *args, **kwargs):
        """Add a method and its arguments to the queue."""
        self.method_queue.put((method, args, kwargs))

    def process_method_queue(self):
        """Process methods in the queue."""
        while True:
            try:
                method, args, kwargs = self.method_queue.get()
                print(self.method_queue.qsize())
                method(*args, **kwargs)
            except queue.Empty:
                pass  # Ignore empty queue

    def initialize_LoRaWAN(self, retry_limit=3):
        """Attempt to initialize LoRaWAN connection with retry mechanism."""
        time.sleep(4)  # Delay for Arduino boot up
        self.ser.write(b"#BEGIN\n")
        for attempt in range(retry_limit):
            bol = self.ser.readline()
            if bol.decode().strip() == "#JOINED":
                self.connected_bool = True
                self.ser.write(b"#BLANK\n")
                time.sleep(10)
                return True

            time.sleep(5)  # Delay between retries

    def terminate_LoRaWAN(self):
        """Terminate the LoRaWAN connection."""
        self.ser.write(b"#QUIT\n")
        self.connected_bool = False

    def change_system_time(self, time_value):
        date_parts = time_value.split(", ")
        formatted_date = datetime.strptime(date_parts[0], "%m/%d/%Y").strftime(
            "%Y-%m-%d"
        )
        formatted_time = date_parts[1]
        formatted_system_time = f"{formatted_date} {formatted_time}"
        os.system(f"sudo date -s '{formatted_system_time}'")
        return

    def passive_listen(self, timeout=15):
        """Listen for incoming data with a specified timeout."""
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                return None
            received_message = self.ser.readline().decode().strip()
            if received_message:
                return received_message
            time.sleep(0.1)  # Short delay to prevent busy waiting

    def save_message_to_csv(self, input_str, csv_filename="data/messages.csv"):
        if "#" in input_str and len(input_str.split("#")) == 2:
            address, message = input_str.split("#")
            if os.path.exists(csv_filename):
                df = pd.read_csv(csv_filename, header=0)
            else:
                df = pd.DataFrame(columns=[address])
                df.to_csv(csv_filename, index=False)
                return self.save_message_to_csv(input_str, csv_filename)
            if address in df.columns:
                df.loc[
                    df[address].last_valid_index() + 1
                    if pd.notna(df[address]).any()
                    else 0,
                    address,
                ] = message
            else:
                df[address] = None
                df.loc[0, address] = message
            df.to_csv(csv_filename, index=False)
        else:
            print("The message format is incorrect. No action taken.")

    def send_emergency(self, gps_data):
        """Send an emergency signal with GPS data if connected."""
        # connected_bool = self.initialize_LoRaWAN()
        if self.connected_bool:
            sent_em_message = f"#EM{gps_data}\r\n".encode()
            self.ser.write(sent_em_message)
            received_message = self.passive_listen()
            # self.terminate_LoRaWAN()
            print(received_message)
        else:
            print("NOT CONNECTED TO NETWORK, CANNOT SEND DISTRESS CALL")
            # self.terminate_LoRaWAN()

    def request_weather_time(self):
        """Request weather data and system time if connected, then save to CSV."""
        # connected_bool = self.initialize_LoRaWAN()
        if self.connected_bool:
            self.ser.write(b"#WEATHER\n")
            received_message = self.passive_listen()
            print(received_message)
            # self.terminate_LoRaWAN()
            weather_data_start_index = received_message.find("[")
            system_time_str = received_message[:weather_data_start_index].strip()
            data = json.loads(received_message[weather_data_start_index:].strip())
            df = pd.DataFrame(data)
            df["p"] = df["p"] * 100  # change from decimal to percentage
            df.rename(
                columns={"m": "max temp", "n": "min temp", "p": "precipitation"},
                inplace=True,
            )
            current_date = datetime.now()
            df["day"] = [
                (current_date + timedelta(days=i)).strftime("%A")
                for i in range(len(df))
            ]
            cols = ["day"] + [col for col in df if col != "day"]
            df = df[cols]
            system_time_df = pd.DataFrame([system_time_str], columns=["day"])
            df = pd.concat([df, system_time_df], ignore_index=True)
            print(df)
            csv_file_path = "data/weather_data.csv"
            df.to_csv(csv_file_path, index=False, header=True)
        else:
            print("FAILED TO CONNECT TO NETWORK. CANNOT UPDATE TIME")
            # self.terminate_LoRaWAN()

    def send_text(self, address, text):
        # connected_bool = self.initialize_LoRaWAN()
        if self.connected_bool:
            sent_message = f"{address}#{text}"
            self.ser.write(f"{sent_message}\n".encode())
            received_message = self.passive_listen()
            # time.sleep(15)  # Replaces time.sleep(15)
            self.active_listen()
            self.save_message_to_csv(sent_message)
            if received_message:
                self.save_message_to_csv(received_message)
        else:
            print("NOT CONNECTED TO NETWORK, CANNOT SEND TEXT")
            # self.terminate_LoRaWAN()

    def active_listen(self, timeout=5):
        while True:
            self.ser.write(b"#LISTEN\n")
            start_time = time.time()
            while True:
                time.sleep(1)  # Replaces time.sleep(1)
                if (time.time() - start_time) > timeout:
                    print("Active listen timeout.")
                    # self.terminate_LoRaWAN()
                    return
                response = self.ser.readline().decode().strip()
                if response:
                    if response == "#FALSE":
                        print("All messages received.")
                        # self.terminate_LoRaWAN()
                        return
                    else:
                        # print(response)
                        self.save_message_to_csv(response)
                        break


if __name__ == "__main__":
    myLora = Lora()

    # Example usage with the queue system
    myLora.add_to_queue(myLora.send_emergency, "10.1100")
    myLora.add_to_queue(myLora.non_blocking_delay, 3)
    myLora.add_to_queue(myLora.send_text, "b69b9d14e5e5b0c0", "hey4!")
    myLora.add_to_queue(myLora.non_blocking_delay, 3)
    myLora.add_to_queue(myLora.active_listen)
    myLora.add_to_queue(myLora.terminate_LoRaWAN)

    # Wait for the queue to be processed (optional)
    myLora.method_queue.join()
