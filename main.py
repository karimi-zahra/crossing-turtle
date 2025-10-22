from turtle import Screen
from myturtle import MyTurtle
import time
from cars import Cars
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
tommy = MyTurtle()

cars = Cars()
scoreboard = ScoreBoard()
scoreboard.write_score()
screen.listen()
screen.onkey(fun=tommy.move_up, key="Up")
screen.onkey(fun=tommy.move_down, key="Down")
moving_speed = 0.1
game_not_over = True
while game_not_over:
    time.sleep(moving_speed)
    screen.update()
    cars.create_car()
    cars.moving_cars()
    for car in cars.allcars:
        if car.distance(tommy) < 20:
            game_not_over = False
    if tommy.ycor()>300:
        scoreboard.level_up()
        tommy.creat_turtle()
        cars.car_speed +=5




screen.exitonclick()