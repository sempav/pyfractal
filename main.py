#!/usr/bin/env python2

import cmath
import math
import png
import sys

import colors
import fractals


def calculate(a, dim_x, dim_y, fractal, color_picker):
    for y in xrange(dim_y):
        if y % 10 == 0:
            print "%d%% done" % ((100 * y) // dim_y)
        for x in xrange(dim_x):
            col = fractal(-2.50 + x * 3.5 / dim_x,
                           1.25 - y * 2.5 / dim_y,
                           color_picker)
            a[y].append(col[0])
            a[y].append(col[1])
            a[y].append(col[2])


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "out.png"
    dim_x = 2000
    dim_y = 2000
    a = [[] for i in xrange(dim_y)]
    calculate(a, dim_x, dim_y, fractals.mandelbrot, colors.log_color)
    wi = len(a[0]) / 3
    he = len(a)
    print wi, he
    w = png.Writer(wi, he)
    with open(filename, "wb") as f:
        w.write(f, a)


if __name__ == "__main__":
    main()
