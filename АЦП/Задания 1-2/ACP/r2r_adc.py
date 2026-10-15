import time
import RPi.GPIO as GPIO


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26,20,19,16,13,12,25,11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)


    def deinit(self):
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()


    def number_to_dac(self, number):
        number = max(0, min(int(number), 256))
        bits = [int(bit) for bit in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, bits)
    
    def sequential_counting_adc(self):
        for x in range(256):
            self.number_to_dac(x)
            time.sleep(self.compare_time)
            if GPIO.input(self.comp_gpio) == 1:
                if self.verbose:
                    print(f'[Равзвертка] Компаратор сработал на числе: {x}')
                return x
        if self.verbose:
            print(f'[Развертка] Сигнал превышает динамический диапазон ЦАП')
        return 255

    def get_sc_voltage(self):
        code = self.sequential_counting_adc()
        voltage = (code / 255) * self.dynamic_range
        return voltage

if __name__ == '__main__':
    adc = None
    try:
        adc = R2R_ADC(dynamic_range = 3.285, compare_time = 0.01, verbose = True)
        print('АЦП запущен')
        print('-' * 50)


        while True:
            voltage = adc.get_sc_voltage()
            print(f'Напряжение: {voltage:.3f} B')
            print('-' * 50)
            time.sleep(0.5)
    finally:
        if adc is not None:
            adc.deinit()