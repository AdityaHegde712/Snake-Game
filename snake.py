from turtle import Turtle

MOVE_DISTANCE = 20
START = [0, -20, -40]
UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.full_snake = []
        self.create_snake()
        self.head = self.full_snake[0]

    def create_snake(self):
        for i in START:
            self.add_segment(i)

    def add_segment(self, position):
        t = Turtle(shape="square")
        t.color("white")
        t.pu()
        t.goto(position, 0)
        self.full_snake.append(t)

    def extend(self):
        self.add_segment(self.full_snake[-1].xcor())

    def move(self):
        for i in range(len(self.full_snake) - 1, 0, -1):
            new_x = self.full_snake[i - 1].xcor()
            new_y = self.full_snake[i - 1].ycor()
            self.full_snake[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
