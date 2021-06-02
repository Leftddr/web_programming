import turtle

# silly = turtle.Turtle()
#
# silly.forward(50)
# silly.right(90)     # Rotate clockwise by 90 degrees
#
# silly.forward(50)
# silly.right(90)
#
# silly.forward(50)
# silly.right(90)
#
# silly.forward(50)
# silly.right(90)
#
# turtle.done()

# star = turtle.Turtle()
#
# for i in range(50):
#     star.forward(50)
#     star.right(144)
#
# turtle.done()

spiral = turtle.Turtle()
spiral.shape("turtle")
for i in range(20):
    spiral.forward(i * 10)
    spiral.right(144)

turtle.done()