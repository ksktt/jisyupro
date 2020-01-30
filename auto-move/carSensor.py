import smbus
import time
import numpy as np

class CarSensor(object):
    def __init__(self):
        self.address = 0x68
        self.bus     = smbus.SMBus(1)

        # レジスタをリセットする
        self.bus.write_i2c_block_data(self.address, 0x6B, [0x80])
        time.sleep(0.01)
        # PWR_MGMT_1をクリア
        self.bus.write_i2c_block_data(self.address, 0x6B, [0x00])
        time.sleep(0.01)

        # 加速度の計測レンジ <- 2G
        self.bus.write_i2c_block_data(self.address, 0x1C, [0x00])
        self.accCoefficient = 2 / float(0x8000)
        # 角速度の計測レンジ <- 500dps
        self.bus.write_i2c_block_data(self.address, 0x1B, [0x08])
        self.gyroCoefficient = 500 / float(0x8000)

        # データ読み込み形式の指定
        self.dtype = np.dtype(np.int16).newbyteorder('B')

        self.offsetRawAcc = np.zeros(3)
        self.offsetRawGyro = np.zeros(3)

    def calibrate(self,n=1000):
        """オフセットを計測しておく"""
        sg = np.zeros(3)
        sa = np.zeros(3)
        for i in range(n):
            data = self.bus.read_i2c_block_data(self.address, 0x43 ,6)
            raw = np.frombuffer(bytes(data),self.dtype,3)
            sg += raw
            data = self.bus.read_i2c_block_data(self.address, 0x3B ,6)
            raw = np.frombuffer(bytes(data),self.dtype,3)
            sa += raw
        self.offsetRawGyro = -sg/n
        self.offsetRawAcc = -sa/n

    def readGyro(self):
        ## ジャイロ
        data    = self.bus.read_i2c_block_data(self.address, 0x43 ,6)
        rawGyro = np.frombuffer(bytes(data),self.dtype,3)
        return self.gyroCoefficient*(rawGyro+self.offsetRawGyro)

    def readAcc(self):
        ## 加速度
        data    = self.bus.read_i2c_block_data(self.address, 0x3B ,6)
        rawAcc = np.frombuffer(bytes(data),self.dtype,3)
        return self.accCoefficient*(rawAcc+self.offsetRawAcc)
