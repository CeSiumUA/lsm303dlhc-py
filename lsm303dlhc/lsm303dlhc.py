import lsm303dlhc.i2c_transport.i2c_abc as i2c_abc

class LSM303DLHC:
    def __init__(self, i2c: i2c_abc.I2C_ABC):
        self.i2c = i2c