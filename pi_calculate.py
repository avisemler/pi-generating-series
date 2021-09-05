import numpy as np
import matplotlib.pyplot as plt

TERMS = 100000

class PiSeries:
    def __init__(self):
        self.series = np.zeros(TERMS, dtype = np.longdouble)
        self.current = 0

class Nilakantha(PiSeries):
    def __init__(self):
        PiSeries.__init__(self)
        self.series[0] = 3
    
    def update(self, i):
        """
        self.current += (-1) ** (i + 1) * 4 / ((2*i) * (2*i + 1) * (2*i + 2))
        self.series[i - 1] = self.current
        """
        self.series[i] = self.series[i -1] + (-1) ** (i + 1) * 4 / ((2*i) * (2*i + 1) * (2*i + 2))

class GL(PiSeries):
    def update(self, i):
        self.current += (-1) ** (i + 1) * 4 / (2*i - 1)
        self.series[i] = self.current

approximations = {"nilakantha": Nilakantha(),
    "gregory_leibniz": GL(),
}

for i in range(1, TERMS):
    for series in approximations.values():
        series.update(i)


plot_number = 1
for name in approximations:
    plt.subplot(2, 1, plot_number)
    plt.ylim((3.14, 3.15))

    plt.plot(approximations[name].series[10:])
    plot_number += 1
    print(name, approximations[name].series[-1])

plt.show()