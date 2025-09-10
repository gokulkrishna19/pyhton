# polygon.py
import turtle
import math
import sys

def draw_regular_polygon(t, sides, side_length, fill=False):
    """Draw a regular polygon with given number of sides and side length."""
    if sides < 3:
        raise ValueError("A polygon must have at least 3 sides.")
    angle = 360.0 / sides
    if fill:
        t.begin_fill()
    for _ in range(sides):
        t.forward(side_length)
        t.left(angle)
    if fill:
        t.end_fill()

def draw_star_polygon(t, sides, step, side_length, fill=False):
    """
    Draw a star-like polygon on the same set of vertices by skipping 'step' vertices.
    Example: sides=5, step=2 -> classic 5-point star.
    """
    if sides < 3:
        raise ValueError("sides must be >= 3")
    if step <= 0 or step >= sides:
        raise ValueError("step must be >0 and <sides")
    # compute polygon vertices
    vertices = []
    angle = 2 * math.pi / sides
    # center the polygon around origin
    radius = side_length / (2 * math.sin(math.pi / sides))
    for i in range(sides):
        x = radius * math.cos(i * angle)
        y = radius * math.sin(i * angle)
        vertices.append((x, y))

    # move to the first vertex
    t.penup()
    t.g
