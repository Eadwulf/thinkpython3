from createturtle import createTurtle, turtle

def koch(t, order, size):
    """ Make turtle "t" draw a Koch fractal of 'order' and 'size'.
    Leave the turtle facing the same direction. """

    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch(t, order-1, size/3)
            t.left(angle)

t = createTurtle()
koch(t, 1, 300)

turtle.Screen().mainloop()
