import numpy

def draw_square(pygui, x = 0, y = 0, size = 10, stroke = (255, 255, 255), fill = (255, 255, 255), show = True, rounding = 0.0):
    pygui.draw_rectangle(pmin = (x, y), pmax = (x + size, y + size), color = stroke, fill = fill, show = show, rounding = rounding)

def lerp_rgb(start, end, steps = 100):
    r1, g1, b1 = start
    r2, g2, b2, = end
    r3 = numpy.linspace(r1, r2, steps, endpoint = False)
    g3 = numpy.linspace(g1, g2, steps, endpoint = False)
    b3 = numpy.linspace(b1, b2, steps, endpoint = False)
    return numpy.column_stack((r3, g3, b3))