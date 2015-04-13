def mandelbrot(x, y, color_picker):
    z0 = complex(x, y)
    max_it = 255
    it = 0
    z = z0
    while (it < max_it and z.real * z.real + z.imag * z.imag < 4):
        z = z * z + z0
        it += 1
    if it == max_it:
        return [0, 0, 0]
    else:
        return color_picker(1.0 * it, 0.0, 1.0 * max_it)

