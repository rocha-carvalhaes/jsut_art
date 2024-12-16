import turtle

def draw_two_lines():
    # Screen setup
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Simultaneous Drawing")
    screen.setup(width=800, height=600)

    # Create two turtles
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()

    # Turtle 1 setup
    t1.color("red")
    t1.pensize(2)
    t1.speed(0)
    t1.penup()
    t1.goto(-100, 0)  # Start position for line 1
    t1.pendown()

    # Turtle 2 setup
    t2.color("blue")
    t2.pensize(2)
    t2.speed(0)
    t2.penup()
    t2.goto(100, 0)  # Start position for line 2
    t2.pendown()

    # Simultaneous drawing
    for _ in range(100):
        t1.forward(5)  # Move Turtle 1 forward
        t2.forward(5)  # Move Turtle 2 forward

    # Close the window on click
    screen.mainloop()

if __name__ == "__main__":
    draw_two_lines()
