from turtle import Turtle


class Player_o(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.shapesize(0.5)
        self.color("#00755E")
        self.width(16)


    def draw_o(self):
        self.color("#E6F4F1")
        self.pendown()
        self.showturtle()
        self.circle(radius=20)


class Player_x(Turtle):


    def __init__(self):
        super().__init__(visible=False)
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.shape("circle")
        self.shapesize(0.5)
        self.width(16)
        self.right(45)


    def draw_x(self):
        self.color("#5EBBC2")
        self.pendown()
        self.showturtle()
        self.right(90)
        self.forward(20)
        self.backward(60)
        self.forward(30)
        self.left(90)
        self.forward(30)
        self.backward(60)
