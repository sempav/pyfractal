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


def linear_color(val, lo, hi):
    return heatmap_color(val, lo, hi)
