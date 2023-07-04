from turtle import Turtle
FONT = ("Courier", 15, "bold")


class Infotext(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(-80, 180)
        self.color("white")


    def xwins(self):
        self.write(f"Player x wins", font=FONT)
        self.speed("slowest")
        self.goto(-80, -180)


    def owins(self):
        self.write(f"Player 0 wins", font=FONT)
        self.speed("slowest")
        self.goto(-80, -180)
