import smbus
import i2c_transport.i2c_abc as i2c_abc

class SMBusTransport(i2c_abc.I2C_ABC):
    def __init__(self, bus_number: int = 1):
        self.bus_number = bus_number

    def open(self):
        self.bus = smbus.SMBus(self.bus_number)

    def close(self):
        self.bus.close()

    def __enter__(self):
        self.open()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()