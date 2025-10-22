from turtle import Turtle

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.creat_turtle()
    def creat_turtle(self):
        self.shape("turtle")
        self.penup()
        self.goto(0,-280)
        self.setheading(90)

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)