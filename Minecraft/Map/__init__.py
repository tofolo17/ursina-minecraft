from random import randint

import matplotlib.pylab as plt
from perlin_noise import PerlinNoise


def generator():
    noise = PerlinNoise(octaves=2, seed=randint(1, 9999))

    x_pix, y_pix = 21, 21
    noise_values = [[noise([i / x_pix, j / y_pix]) for j in range(x_pix)] for i in range(y_pix)]

    plt.imshow(noise_values, cmap='gray')
    plt.show()

    y_coordinates = []
    for noise_set in noise_values:
        y_set = []
        for noise in noise_set:
            y = round(noise * 10)
            y_set.append(y)
        y_coordinates.append(y_set)
    return y_coordinates
