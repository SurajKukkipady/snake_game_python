# Import the Turtle class from the turtle module
from turtle import Turtle

# Define constants for the starting position, move distance, and directions
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


# Create a Snake class to represent the snake in the game
class Snake:
    def __init__(self):
        # Initialize the Snake object
        self.segments = []  # List to store the snake's body segments
        self.create_snake()  # Create the initial snake
        self.head = self.segments[0]  # Set the snake's head as the first segment

    # Method to create the initial snake with three segments
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    # Method to move the snake forward
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Move the snake's head forward

    # Methods to change the snake's direction
    def up(self):
        if self.head.heading() != DOWN:  # Ensure the snake cannot turn directly into its own body
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

    # Method to add a new segment to the snake's body
    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Method to extend the snake's length by adding a new segment to the tail
    def extend(self):
        self.add_segment(self.segments[-1].position())