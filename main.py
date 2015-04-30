#!/usr/bin/env python2

import png
import sys

import colors
import fractals
import argparse
from rect import Rect


def calculate(a, resolution, bounds, fractal, color_picker):
    ''' Calculate image of the fractal

    :param a: output image buffer
    :param resolution: fractal image resolution
    :param bounds: rectangle describing geometrical bounds of the fractal
    :param fractal: callback describing fractal color in specified point
    :param color_picker: rule of conversion scalar value to color
    :return: None
    '''
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


def main(args):
    a = [[] for i in xrange(args.resolution[1])]
    calculate(a, tuple(args.resolution),
              args.borders, args.fractal, args.cmap)
    wi = len(a[0]) / 3
    he = len(a)
    print wi, he
    w = png.Writer(wi, he)
    with open(args.out, "wb") as f:
        w.write(f, a)


def parse_arguments():
    ''' parse arguments for the PyFractal application '''

    parser = argparse.ArgumentParser(description='Python fractals renderer')

    parser.add_argument('--resolution', metavar=('X', 'Y'), type=int, nargs=2,
                        help="output image resolution (default: %(default)s)",
                        default=[1024, 768])
    parser.add_argument('--out', type=str,
                        help="output file name (default: %(default)s)",
                        default="out.png")
    parser.add_argument('--borders', metavar=('L', 'R', 'D', 'U'), type=float, nargs=4,
                        help="four values representing fractal borders (default: %(default)s)",
                        default=[-1.0, 1.0, -1.0, 1.0])
    parser.add_argument('--fractal', choices=['mandelbrot', 'burning_ship'],
                        help='name of the fractal (default: %(default)s)',
                        default='mandelbrot')
    parser.add_argument('--cmap', choices=['heat', 'heat_log'],
                        help='color map used to represent the fractal (default: %(default)s)',
                        default='heat_log')

    cmap_dispatcher = {
        'heat_log': colors.log_color,
        'heat': colors.linear_color
    }
    fractals_dispatcher = {
        'mandelbrot': fractals.mandelbrot,
        'burning_ship': fractals.burning_ship
    }

    args = parser.parse_args()

    args.fractal = fractals_dispatcher[args.fractal]
    args.cmap = cmap_dispatcher[args.cmap]
    args.borders = Rect(left=args.borders[0],
                        right=args.borders[1],
                        bottom=args.borders[2],
                        top=args.borders[3])
    return args

if __name__ == "__main__":
    main(parse_arguments())
