from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):
    score = 0

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pu()
        self.goto(0, 275)
        self.write_score()

    def write_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
        self.goto(0, -25)
        self.write(f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)
