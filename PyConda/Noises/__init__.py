import random

from opensimplex import OpenSimplex


# first and confused contact with Perlin noise - https://www.youtube.com/watch?v=O33YV4ooHSo&t=1180s
def simple_curve(value):
    start = 0.4
    end = 0.6
    if value < start:
        return 0.0
    if value > end:
        return 1.0
    return (value - start) * (1 / (end - start))


def interpolate(a, b, weight):
    new_weight = simple_curve(weight)
    return a * (1 - new_weight) + b * new_weight


def simple_s_curve(x_input, y_input):
    tmp = OpenSimplex(int(random.random() * 10000))

    def noise(x_axis, y_axis):
        n = (tmp.noise2d(x_axis / 5.0, y_axis / 5.0) + 1) / 2.0
        return interpolate(0.0, 1.0, n) * 10.0

    return noise(x_input, y_input)


def plains(x_input, y_input):
    tmp = OpenSimplex(int(random.random() * 10000))

    def noise(x_axis, y_axis):
        value = (tmp.noise2d(x_axis / 3.0, y_axis / 3.0) + 1) / 2.0
        value = value**0.25
        value = value - 0.6
        if value < 0:
            value = 0
        return value * 6.0

    return noise(x_input, y_input)


def mountains(x_input, y_input):
    tmp = OpenSimplex(int(random.random() * 10000))

    def noise(x_axis, y_axis):
        value = (tmp.noise2d(x_axis * 2.0, y_axis) + 1) / 2.0
        value = value
        return value * 20.0

    return noise(x_input, y_input)


# Blends "mountains" and "plains" noise, weighted by an S-curve noise.
def combined(x_input, y_input):
    m_values = mountains(x_input, y_input)
    p_values = plains(x_input, y_input)
    weights = simple_s_curve(x_input, y_input) / 10.0

    def noise():
        m = m_values
        p = p_values
        w = weights
        return (p * w) + (m * (1 - w))

    return noise()


# -------------------------------------------------------
