from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f"{self.score}", align="center", font=("Arial", 60, "bold"))

    # Update scoreboard when ball goes out of bounds
    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()
