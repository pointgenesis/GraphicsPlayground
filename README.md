# GraphicsPlayground
Playing around with the Turtle library to create interesting graphics like fractals.

## graphics.py

Main python module, and test area for methods.

### def draw_concentric_squares(draw, length)

Draws a set of concentric squares with the given drawing instrument --> **draw** and given sides length --> **length**.

### def polygon(draw, sides, length)

Draws a polygon shape with the given drawing instrument --> **draw**, given number of sides --> **sides**, and given side length --> **length**.

### def mystery(draw, length, order)

Draws an elementary branching fractal on a honeycombed angle using the given drawing instrument --> **draw**, given side length -->  **length**, and given order --> **order**.

### def koch(draw, order, size)

Draws a Koch curve aka fractal with a given drawing instrument --> **draw**, given order of recursion, i.e. order(0) is a straight line --> **order**, and given length of the line --> **size**.

## References

[1] http://openbookproject.net/thinkcs/python/english3e/genindex.html
