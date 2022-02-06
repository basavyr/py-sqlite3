import matplotlib.pyplot as plt

import temp


class Graph:

    PLOT_STORAGE_PATH = '../db/'

    def PlotData(self, data, plot_file):
        x_data = [idx for idx in range(len(data))]
        y_data = data
        xmin, xmax = [min(y_data), max(y_data)]
        avg = float(sum(y_data) / len(y_data))
        avgs = [avg for _ in range(len(y_data))]
        plot_path = f'{Graph.PLOT_STORAGE_PATH}{plot_file}'

        plt.plot(x_data, y_data, '-or', label='Room_Temp')
        plt.plot(x_data, avgs, '--k', label='avg')
        plt.xlabel('i')
        plt.ylabel('temp')
        plt.ylim([0, xmax + 2])
        plt.legend(loc='best')
        plt.tight_layout()
        plt.savefig(plot_path, dpi=300, bbox_inches='tight')
        plt.close()
