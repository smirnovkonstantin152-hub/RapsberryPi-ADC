import smbus
import time
class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose
    
    def deinit(self):
        self.bus.close()
    
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_bute = data & 0xFF
        number = (upper_data_bute << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"Принятые данные: {data}, Старший байт: {upper_data_bute:x}, Младший байт: {lower_data_byte:x}, Число: {number}")
        return number
    
    def get_voltage(self):
        digital_value = self.get_number()
        voltage = digital_value / 1023 * self.dynamic_range
        return voltage

if __name__ == '__main__':
    mcp = None
    try:
        mcp = MCP3021(dynamic_range = 5, verbose = False)
        while True:
            voltage = mcp.get_voltage()
            print(f'Напряжение на входе: {voltage:3f} В')
            time.sleep(0.5)
    finally:
        if mcp is not None:
            mcp.deinit()