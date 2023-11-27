import time

# import serial  # pip install pyserial

# ser = serial.Serial(
#     port="/dev/ttyS0",
#     baudrate=9600,
#     parity=serial.PARITY_NONE,
#     stopbits=serial.STOPBITS_ONE,
#     bytesize=serial.EIGHTBITS,
#     timeout=1,
# )


class Gps:
    def __init__(self):
        # self.ser = serial.Serial(
        #     port="/dev/ttyS0",
        #     baudrate=9600,
        #     parity=serial.PARITY_NONE,
        #     stopbits=serial.STOPBITS_ONE,
        #     bytesize=serial.EIGHTBITS,
        #     timeout=1,
        # )

        self.lastCords = [33.93838719687294, -84.52097068126767, 0]

    def getCords(self):
        return self.lastCords

        # while True:
        #     x = self.ser.readline()

        #     try:
        #         decoded = x.decode("utf-8", "ignore")
        #     except UnicodeDecodeError as e:
        #         pass

        #     parts = decoded.strip().split(",")

        #     # parse_nmea
        #     if parts[0] == "$GPGGA":
        #         if parts[6] == "0":  # if there is no sat connection
        #             self.lastCords[2] = 0
        #             return self.lastCords

        #         else:  # if there is a sat connection
        #             latitude = float(parts[2][:2]) + float(parts[2][2:]) / 60.0
        #             if parts[3] == "S":
        #                 latitude = -latitude  # Add negative sign for South latitude

        #             longitude = float(parts[4][:3]) + float(parts[4][3:]) / 60.0

        #             if parts[5] == "W":
        #                 longitude = -longitude  # Add negative sign for West longitude

        #             altitude = float(parts[9])

        #             self.lastCords = [latitude, longitude, 1]

        #             return self.lastCords

    def test(self):
        while True:
            x = self.ser.readline()

            try:
                decoded = x.decode("utf-8", "ignore")
            except UnicodeDecodeError as e:
                print("failed")
                pass

            parts = decoded.strip().split(",")

            if parts[0] == "$GPGGA":
                print(decoded)
            if parts[6] == "1":
                print("1")

            time.sleep(0.2)


if __name__ == "__main__":
    pass
