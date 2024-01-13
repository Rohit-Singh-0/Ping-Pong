from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from boundary import Boundary
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
pong_ball = Ball((0, 0))
scoreboard = Scoreboard()
boundary = Boundary()
boundary.create()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
speed = 0.1
while game_is_on:
    time.sleep(pong_ball.move_speed)
    screen.update()
    pong_ball.move()

    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce()

    if pong_ball.distance(r_paddle) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(
            l_paddle) < 50 and pong_ball.xcor() < -320:
        pong_ball.strike()

    if pong_ball.xcor() > 380:
        pong_ball.reset()
        scoreboard.l_point()

    if pong_ball.xcor() < -380:
        pong_ball.reset()
        scoreboard.r_point()

screen.exitonclick()
