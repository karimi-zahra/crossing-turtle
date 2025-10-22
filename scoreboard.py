from turtle import Turtle
FONT = ("Courier",18,"normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-260,260)

    def write_score(self):
        self.write(arg=f"Level: {self.level}",font=FONT)

    def level_up(self):
        self.clear()
        self.level +=1
        self.write_score()
