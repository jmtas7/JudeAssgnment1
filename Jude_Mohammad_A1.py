import turtle
turtle.tracer(0)

X_MAX = 400
Y_MAX = 400
X_MIN = -400
Y_MIN = -400

turtle.screensize(X_MAX , Y_MAX)

def rectangle_will_fit(x, y, length, height):
    if x + length <= X_MAX and x + length >= X_MIN and y + height <= Y_MAX and y + height >= Y_MIN :
        return 1
    else :
        return 2

def circle_will_fit(x, y, length, height = 0):
    if x + length <= X_MAX and x + length >= X_MIN and y + height <= Y_MAX and y + height >= Y_MIN :
        return 1
    else :
        return 2

def triangle_will_fit(x, y, length, height = 0):
    if x + length <= X_MAX and x + length >= X_MIN and y + height <= Y_MAX and y + height >= Y_MIN :
        return 1
    else :
        return 2

def draw_shape(shape, color_code, x, y, length, height = 0):

    if shape == "r" and x + length <= X_MAX and x + length >= X_MIN and y + height <= Y_MAX and y + height >= Y_MIN :
        print("Draw the rectangle! ")
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.color("Black" , color_code)
        turtle.begin_fill()
        for i in range(2):
            turtle.forward(length)
            turtle.right(90)
            turtle.forward(height)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        turtle.home()
        turtle.pendown()

        return 2 * (length + height)

    elif shape == "c" and x + length <= X_MAX and x + length >= X_MIN and y + height <= Y_MAX and y + height >= Y_MIN :
        print("Draw the circle! ")
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.color("Black" , color_code)
        turtle.begin_fill()
        turtle.circle(length)
        turtle.end_fill()
        turtle.penup()
        turtle.home()
        turtle.pendown()

        return 2 * 3.14 * length

    elif shape == "t" and x+length <= X_MAX and x+length >= X_MIN and y+height <= Y_MAX and y+height >= Y_MIN :
        print("Draw the triangle! ")
        turtle.penup()
        turtle.goto(x,y)
        turtle.pendown()
        turtle.color("Black" , color_code)
        turtle.begin_fill()
        for i in range(3) :
            turtle.forward(length)
            turtle.left(120)
        turtle.end_fill()
        turtle.penup()
        turtle.home()
        turtle.pendown()

        return 3 * length 

    else :
        print("Wrong Input!")
        exit()

def main():
    draw_shape('r','blue',200,200,100,70)
    draw_shape('c','red',200,-200,70)
    draw_shape('t','yellow',-200,-200,100)
    turtle.done()
main()