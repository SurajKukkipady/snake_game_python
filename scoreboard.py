# Import the Turtle class from the turtle module
from turtle import Turtle


# Create a Scoreboard class that inherits from the Turtle class
class Scoreboard(Turtle):
    def __init__(self):
        # Initialize the Scoreboard object
        super().__init__()

        # Initialize the score attribute to 0
        self.score = 0

        # Set the color of the Turtle to white
        self.color('white')

        # Hide the Turtle cursor
        self.hideturtle()

        # Lift the pen (so it doesn't draw while moving)
        self.penup()

        # Set the initial position of the Turtle to (0, 270)
        self.goto(0, 270)

        # Update the scoreboard to display the initial score
        self.update_scoreboard()

    # Method to update the scoreboard with the current score
    def update_scoreboard(self):
        self.clear()  # Clear any previous score display
        self.write(f'Score: {self.score}')  # Write the current score

    # Method to increase the score by 1 and update the scoreboard
    def increase_score(self):
        self.score += 1  # Increment the score by 1
        self.update_scoreboard()  # Update the displayed score

    # Method to display "Game Over" message at the center of the screen
    def game_over(self):
        self.goto(0, 0)  # Move the Turtle to the center of the screen
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))  # Display "Game Over" message
