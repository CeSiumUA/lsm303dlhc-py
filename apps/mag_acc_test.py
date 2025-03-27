import smbus
import time

lsm303dlhc_acc_address = 0x19
lsm303dlhc_mag_address = 0x1e
gauss_to_microtesla = 100.0

acc_scale = 2
mag_gauss_xy = 1100
mag_gauss_z = 980

bus = smbus.SMBus(1)
bus.write_byte_data(lsm303dlhc_acc_address, 0x20, 0x57)
bus.write_byte_data(lsm303dlhc_acc_address, 0x23, 0x00)

time.sleep(1)

status_byte = bus.read_byte_data(lsm303dlhc_acc_address, 0x27)
print(f"Acc Status byte: {status_byte}")

bus.write_byte_data(lsm303dlhc_mag_address, 0x00, 0x10)
bus.write_byte_data(lsm303dlhc_mag_address, 0x01, 0x20)
bus.write_byte_data(lsm303dlhc_mag_address, 0x02, 0x00)

time.sleep(1)

while True:
    x_data_0 = bus.read_byte_data(lsm303dlhc_acc_address, 0x28)
    x_data_1 = bus.read_byte_data(lsm303dlhc_acc_address, 0x29)

    x_data = (x_data_1 << 8) | x_data_0
    if x_data > 32767:
        x_data -= 65536
    x_data = x_data / 32767.0 * acc_scale

    y_data_0 = bus.read_byte_data(lsm303dlhc_acc_address, 0x2a)
    y_data_1 = bus.read_byte_data(lsm303dlhc_acc_address, 0x2b)

    y_data = (y_data_1 << 8) | y_data_0
    if y_data > 32767:
        y_data -= 65536
    y_data = y_data / 32767.0 * acc_scale

    z_data_0 = bus.read_byte_data(lsm303dlhc_acc_address, 0x2c)
    z_data_1 = bus.read_byte_data(lsm303dlhc_acc_address, 0x2d)

    z_data = (z_data_1 << 8) | z_data_0
    if z_data > 32767:
        z_data -= 65536
    z_data = z_data / 32767.0 * acc_scale

    x_mag_data_0 = bus.read_byte_data(lsm303dlhc_mag_address, 0x03)
    x_mag_data_1 = bus.read_byte_data(lsm303dlhc_mag_address, 0x04)

    x_mag_data = (x_mag_data_1 << 8) | x_mag_data_0

    # x_mag_data = x_mag_data / mag_gauss_xy * gauss_to_microtesla
    if x_mag_data > 32767:
        x_mag_data -= 65536

    y_mag_data_0 = bus.read_byte_data(lsm303dlhc_mag_address, 0x05)
    y_mag_data_1 = bus.read_byte_data(lsm303dlhc_mag_address, 0x06)

    y_mag_data = (y_mag_data_1 << 8) | y_mag_data_0

    # y_mag_data = y_mag_data / mag_gauss_xy * gauss_to_microtesla

    if y_mag_data > 32767:
        y_mag_data -= 65536

    z_mag_data_0 = bus.read_byte_data(lsm303dlhc_mag_address, 0x07)
    z_mag_data_1 = bus.read_byte_data(lsm303dlhc_mag_address, 0x08)

    z_mag_data = (z_mag_data_1 << 8) | z_mag_data_0

    # z_mag_data = z_mag_data / mag_gauss_z * gauss_to_microtesla

    if z_mag_data > 32767:
        z_mag_data -= 65536

    print("{:+06.2f}g : {:+06.2f}g : {:+06.2f}g".format(x_data, y_data, z_data))
    print("{:+06.2f}uT : {:+06.2f}uT : {:+06.2f}uT".format(x_mag_data, y_mag_data, z_mag_data))
    time.sleep(1)
