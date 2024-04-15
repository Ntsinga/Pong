from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move=10
        self.y_move=10
        self.pace=0.1

    def move(self):
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def y_bounce(self):
        self.y_move=self.y_move*-1
        self.pace *= 0.9

    def x_bounce(self):
        self.x_move=self.x_move*-1

    def out_of_bounds(self):
        self.goto(0, 0)
        self.pace=0.1
        self.x_bounce()




