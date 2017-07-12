import turtle
import random




def draw_square(type):
    genevivo = turtle.Turtle()
    genevivo.shape("turtle")
    genevivo.color("white")
    genevivo.speed(7)

    if type == "a" :
        for x in range(0, 4):
            genevivo.forward(100)
            genevivo.left(90)

    if type == "b":
        for y in range (0, 90):
            genevivo.left(4)
            for x in range(0, 4):
                genevivo.forward(100)
                genevivo.left(90)

def draw_circle():
    pafuncia = turtle.Turtle()
    pafuncia.goto(-100,-100)
    pafuncia.shape("turtle")
    pafuncia.color("black")
    pafuncia.speed(3)
    pafuncia.circle(100)

def draw_triangle():
    cusco = turtle.Turtle()
    cusco.goto(200,200)
    cusco.shape("turtle")
    cusco.color("grey")
    cusco.speed(1)
    for x in range(0, 3):
        cusco.forward(100)
        cusco.left(120)


def visual_interface():
    window = turtle.Screen()
    window.bgcolor("red")

    draw_square("b")
    #draw_circle()
    #draw_triangle()

    window.exitonclick()


#visual_interface()


#sierpinski_triangle
myPen = turtle.Turtle()
myPen.ht()
myPen.speed(150)


points = [[-175, -125], [0, 175], [175, -125]]  # size of triangle



def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2) #find midpoint

def triangle(points,depth):

    myPen.pencolor(random.random(),random.random(),random.random())
    myPen.up()
    myPen.goto(points[0][0],points[0][1])
    myPen.down()
    myPen.goto(points[1][0],points[1][1])
    myPen.goto(points[2][0],points[2][1])
    myPen.goto(points[0][0],points[0][1])

    if depth>0:
        triangle([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   depth-1)
        triangle([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   depth-1)
        triangle([points[2],
                         getMid(points[2], points[1]),
                         getMid(points[0], points[2])],
                   depth-1)


triangle(points,5)


