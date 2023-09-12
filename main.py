# Import necessary modules and classes
import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Create a screen object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

screen.tracer(0)  # Turn off automatic screen updates to control when the screen is refreshed

# Create snake, food, and scoreboard objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen for keyboard input
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()  # Update the screen manually
    time.sleep(0.1)  # Introduce a small delay to control the speed of the game
    snake.move()  # Move the snake forward

    # Check if the snake has collided with the food
    if snake.head.distance(food) < 15:
        food.refresh()  # Refresh the position of the food
        snake.extend()  # Increase the length of the snake
        scoreboard.increase_score()  # Update the score on the scoreboard

    # Check if the snake has hit the wall boundaries
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        scoreboard.game_over()  # Display "Game Over" on the scoreboard
        game_is_on = False  # End the game

    # Detect collision with the snake's own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False  # End the game
            scoreboard.game_over()  # Display "Game Over" on the scoreboard

screen.exitonclick()  # Allow the user to exit the game by clicking on the screen