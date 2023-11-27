import smbus2  # pip install smbus2
import bme280  # pip install RPi.bme280

# test


class Bme:
    def __init__(self):
        # connect to serial prot
        self.port = 1
        self.address = 0x76
        self.bus = smbus2.SMBus(self.port)
        self.calibration_params = bme280.load_calibration_params(self.bus, self.address)

    def getTemp(self):
        data = bme280.sample(self.bus, self.address, self.calibration_params)
        return data.temperature

    def getHumidity(self):
        data = bme280.sample(self.bus, self.address, self.calibration_params)
        return data.humidity

    def getPressure(self):
        data = bme280.sample(self.bus, self.address, self.calibration_params)
        return data.pressure

    def getAltitude(self):
        data = bme280.sample(self.bus, self.address, self.calibration_params)
        pressure = data.pressure
        # pressure to altitude conversion
        p0 = 1013.25  # standard atmospheric pressure at sea level in hPa
        L = 0.00976  # temperature lapse rate in K/m
        T0 = 288.16  # standard temp at sea level in K
        g = 9.81  # gravitational acceleration in m/s^2
        M = 0.02896  # molar mass of dry air in kg/mol
        R0 = 8.3144  # universal gas constant in J/(mol·K)
        h = -(((pressure / p0) ** ((L * R0 / (g * M))) - 1) * T0) / L
        return h


if __name__ == "__main__":
    bme = Bme()
    print(bme.getTemp())
