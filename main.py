from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)
screen.onkeypress(key="w", fun=left_paddle.up)
screen.onkeypress(key="s", fun=left_paddle.down)

game_is_on = True

while game_is_on:
  screen.update()
  time.sleep(ball.move_speed)
  ball.move()

  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.y_bounce()

  if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
    ball.x_bounce()

  if ball.xcor() > 380: 
    ball.reset_position()
    scoreboard.add_left_point()
    
  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.add_right_point()
  



screen.exitonclick()