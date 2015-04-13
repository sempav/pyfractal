#!/usr/bin/env python2

import cmath
import math
import png
import sys

import colors
import fractals
from rect import Rect


def calculate(a, resolution, bounds, fractal, color_picker):
    for y in xrange(resolution[1]):
        if (100 * y) % resolution[1]  == 0:
            print "%d%% done" % ((100 * y) // resolution[1])
        for x in xrange(resolution[0]):
            col = fractal(bounds.left + x * bounds.width / resolution[0],
                          bounds.top - y * bounds.height / resolution[1],
                           color_picker)
            a[y].append(col[0])
            a[y].append(col[1])
            a[y].append(col[2])


def main():
    filename = sys.argv[1] if len(sys.argv) > 1 else "out.png"
    dim_x = 2000
    dim_y = 2000
    a = [[] for i in xrange(dim_y)]
    calculate(a, (dim_x, dim_y),
              Rect(left=-2.5, right=1.0, bottom=-1.25, top=1.25),
              fractals.mandelbrot, colors.log_color)
    wi = len(a[0]) / 3
    he = len(a)
    print wi, he
    w = png.Writer(wi, he)
    with open(filename, "wb") as f:
        w.write(f, a)


if __name__ == "__main__":
    main()
