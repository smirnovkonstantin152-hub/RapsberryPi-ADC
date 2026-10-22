import matplotlib.pyplot as plt
def plot_voltage(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title("Зависимость напряжения от времени", fontsize = 14, fontweight = 'bold')
    plt.xlabel('Время, с', fontsize = 12)
    plt.ylabel("Напряжение В", fontsize = 12)
    plt.grid(True, which = 'both', linestyle = '--', alpha = 0.7)
    plt.show()

def plot_sampling_period_hist(time_data):
    periods = []
    for i in range(len(time_data) - 1):
        delta = time_data[i + 1] - time_data[i]
        periods.append(delta)
    plt.figure(figsize=(10,6))
    plt.hist(periods)
    plt.title("Гистограмма периодов", fontsize = 14, fontweight = 'bold')
    plt.xlabel('Время, с', fontsize = 12)
    plt.ylabel("Частота измерений, Гц", fontsize = 12)
    plt.xlim(0, 0.06)
    plt.grid(True, which = 'both', linestyle = '--', alpha = 0.7)
    plt.show()