import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.new_food()
        scoreboard.update_score()
        snake.extend()

    # Detect wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 260 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()

    # Detect tail collision
    for i in snake.full_snake[1:]:
        if snake.head.distance(i) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
