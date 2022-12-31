from turtle import Turtle
import random as r


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color("blue")
        self.speed("fastest")
        self.new_food()

    def new_food(self):
        random_x = r.randint(-280, 280)
        random_y = r.randint(-280, 260)
        self.goto(random_x, random_y)
