#!/usr/bin/env python2

import cmath
import math
import png
import sys


def clamp(x, l, h):
    return min(max(x, l), h)


def norclamp(x, l, h):
    return (clamp(x, l, h) - l) / (h - l)


def flt_to_byte(*args):
    return map(lambda x: int(255 * x),
               args)


def heatmap_color(val, lo, hi):
    if val > hi or val < lo:
        return flt_to_byte(1.0, 0.0, 1.0)
    val = clamp(val, lo, hi)
    m = [0, 0, 0]
    for i in xrange(3):
        m[i] = ((3 - i) * lo + (1 + i) * hi) / 4

    b = 1.0 - norclamp(val, m[0], m[1])
    g = norclamp(val,   lo, m[0]) * (1.0 - norclamp(val, m[2],   hi))
    r = norclamp(val, m[1], m[2])
    col = flt_to_byte(b, g, r)
    return col


def fakelog(x):
    d = x - 1
    return d - 0.5 * d * d


def log_color(val, lo, hi):
    return heatmap_color(fakelog(1 + val / hi),
                         fakelog(1 + lo / hi),
                         fakelog(2))


def mandelbrot(z0):
    max_it = 255
    it = 0
    z = z0
    while (it < max_it and z.real * z.real + z.imag * z.imag < 4):
        z = z * z + z0
        it += 1
    if it == max_it:
        return [0, 0, 0]
    else:
        return log_color(1.0 * it, 0.0, 1.0 * max_it)


def calculate(a, dim_x, dim_y):
    for y in xrange(dim_y):
        if y % 10 == 0:
            print "%d%% done" % ((100 * y) // dim_y)
        for x in xrange(dim_x):
            z = complex(-2.5 + x * 3.5 / dim_x,
                        1.25 - y * 2.5 / dim_y)
            col = mandelbrot(z)
            a[y].append(col[0])
            a[y].append(col[1])
            a[y].append(col[2])


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "out.png"
    dim_x = 2000
    dim_y = 2000
    a = [[] for i in xrange(dim_y)]
    calculate(a, dim_x, dim_y)
    wi = len(a[0]) / 3
    he = len(a)
    print wi, he
    w = png.Writer(wi, he)
    with open(filename, "wb") as f:
        w.write(f, a)


if __name__ == "__main__":
    main()
