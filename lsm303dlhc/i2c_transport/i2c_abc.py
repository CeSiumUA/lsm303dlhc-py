from abc import ABC

class I2C_ABC(ABC):
    def __init__(self, i2c):
        self.i2c = i2c