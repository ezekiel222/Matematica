import numpy as np
import matplotlib.pyplot as plt

# Calculos de la Funcion cuadratica.

class PolinomioCuadratico:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular(self):
        # Raices:
        x1 = (-self.b + ((self.b ** 2 - (4 * self.a * self.c)) ** (1 / 2)).real) / (2 * self.a)
        x2 = (-self.b - ((self.b ** 2 - (4 * self.a * self.c)) ** (1 / 2)).real) / (2 * self.a)

        # Vetice:
        xv = -self.b / (2 * self.a)
        yv = (self.a * (xv ** 2)) + (self.b * xv) + self.c

        return x1, x2, xv, yv

    def graficar(self):
        # Graficar el polinomio
        x = np.linspace(-5, 5, 100)
        y = (self.a * (x ** 2)) + (self.b * x) + self.c

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        ax.spines['left'].set_position(('data', 0.0))
        ax.spines['bottom'].set_position(('data', 0.0))
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')

        plt.plot(x, y, 'r')

        plt.show()


def cuadratica_canonica(a, xv, yv):
    b = a * (2 * xv)
    c = a * (xv ** 2) + yv
    return b, c


def cuadratica_factorizada(a, x1, x2):
    b = a * (x1 + x2)
    c = a * (x1 * x2)
    return b, c
