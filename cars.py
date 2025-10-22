from turtle import Turtle
import random

COLORS = ["red","blue","green","yellow","orange","purple","pink"]
class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.car_speed = 20
        self.allcars=[]

        
    def create_car(self):
        chance = random.randint(1,6)
        if chance==1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(280,random.randint(-230,230))
            self.allcars.append(car)
        
    def moving_cars(self):
        for car in self.allcars:
            car.backward(self.car_speed)



