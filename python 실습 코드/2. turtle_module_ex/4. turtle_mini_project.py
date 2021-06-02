import turtle

def draw_art() :
    window = turtle.Screen()
    window.bgcolor("black")

    # Create the turtle Brad -- draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(10)
    for i in range(1,51) :
        brad.circle(80)
        brad.left(360/50)

    window.exitonclick()
    


draw_art()
