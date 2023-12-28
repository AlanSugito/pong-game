from turtle import Turtle

FONT_SIZE = 80


class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.color("white")
    self.penup()
    self.hideturtle()
    self.left_point = 0
    self.right_point = 0
    
    self.update_scoreboard()

  def update_scoreboard(self):
    self.clear()
    self.goto(-100, 200)
    self.write(f"{self.left_point}", font=("Courier", FONT_SIZE, "normal"))
    self.goto(100, 200)
    self.write(f"{self.right_point}", font=("Courier", FONT_SIZE, "normal"))
    
  def add_left_point(self):
    self.left_point += 1
    self.update_scoreboard()
    
  def add_right_point(self):
    self.right_point += 1
    self.update_scoreboard()