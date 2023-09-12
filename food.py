# Import the Turtle class from the turtle module
from turtle import Turtle

# Import the random module to generate random coordinates
import random


# Create a Food class that inherits from the Turtle class
class Food(Turtle):
    def __init__(self):
        # Initialize the Food object
        super().__init__()

        # Set the shape of the food to a circle
        self.shape('circle')

        # Lift the pen (so it doesn't draw while moving)
        self.penup()

        # Adjust the size of the food
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        # Set the color of the food to blue
        self.color('blue')

        # Set the speed of the food to 'fastest'
        self.speed('fastest')

        # Call the refresh method to position the food randomly on the screen
        self.refresh()

    # Method to refresh the food's position with random coordinates
    def refresh(self):
        # Generate random x and y coordinates within the screen boundaries
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)

        # Move the food to the generated random coordinates
        self.goto(random_x, random_y)
