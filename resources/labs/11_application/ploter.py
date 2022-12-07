import matplotlib.pyplot as plt


def make_plot(data, path):
    fig, ax = plt.subplots(1, 1)

    x = [int(item[0]) for item in data]
    y = [int(item[1]) for item in data]

    ax.plot(x, y, label="temperature")
    ax.set_title("Temperature over day")
    ax.set_xlabel('Time [h]')
    ax.set_ylabel('Temperature [°C]')
    ax.set_ylim([-10, 10])
    ax.set_xlim([1, 24])
    ax.legend()
    ax.grid(True)

    # fig.show()

    fig.savefig(path)
