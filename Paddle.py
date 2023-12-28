from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, x_pos, y_pos):
    super().__init__()
    self.x_pos = x_pos
    self.y_pos = y_pos
    self.shape("square")
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.color("white")
    self.penup()
    self.goto(x=self.x_pos, y=self.y_pos)

  def up(self):
    if self.y_pos < 240:
      self.y_pos += 20
      self.goto(self.x_pos, self.y_pos)

  def down(self):
    if self.y_pos > -240:
      self.y_pos -= 20
      self.goto(self.x_pos, self.y_pos)
