import time
from r2r_adc import R2R_ADC
from adc_plot import plot_voltage
from adc_plot import plot_sampling_period_hist

adc = None
try:
    adc = R2R_ADC(dynamic_range = 3.285, compare_time = 0.0001, verbose = True)
    print('АЦП запущен')
    print('-' * 50)
    values = []
    time_values = []
    duration = 3.0
    start = time.time()
    current_time = start


    while current_time - start < duration:
        current_voltage = adc.get_sc_voltage()
        current_time = time.time()
        delta_t = current_time - start
        values.append(current_voltage)
        time_values.append(delta_t)
    

    plot_voltage(time_values, values, max_voltage = 3.285)
    plot_sampling_period_hist(time_values)
finally:
    if adc is not None:
        adc.deinit()