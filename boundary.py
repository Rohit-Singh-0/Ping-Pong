from turtle import Turtle

class Boundary(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0, -300)
        self.stride = 10
        self.hideturtle()


    def create(self):
        for _ in range(30):
            self.goto(0, self.ycor() + self.stride)
            self.penup()
            self.goto(0, self.ycor() + self.stride)
            self.pendown()
