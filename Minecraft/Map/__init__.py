from random import randint

import matplotlib.pylab as plt
from perlin_noise import PerlinNoise


# Builds a size x size height map from 2D Perlin noise (shown first with
# matplotlib: close the plot window to open the game).
def generator(size, octave):
    noise = PerlinNoise(octaves=octave, seed=randint(1, 9999))

    x_pix = z_pix = size
    noise_values = [
        [noise([i / x_pix, j / z_pix]) for j in range(x_pix)]
        for i in range(z_pix)
    ]

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
