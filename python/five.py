import turtle

t = turtle.Turtle()
t.speed(0)


def draw_hexagon(size):
    for _ in range(6):
        t.forward(size)
        t.left(60)


for i in range(10):
    
    t.left(36)
    t.forward(70)
    
    draw_hexagon(50)

t.hideturtle()
turtle.done()