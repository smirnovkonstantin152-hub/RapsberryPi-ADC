import matplotlib.pyplot as plt
def plot_voltage(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage)
    plt.title("Зависимость напряжения от времени", fontsize = 14, fontweight = 'bold')
    plt.xlabel('Время, с', fontsize = 12)
    plt.ylabel("Напряжение В", fontsize = 12)
    plt.grid(True, which = 'both', linestyle = '--', alpha = 0.7)
    plt.show()