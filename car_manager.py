from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
START_X = 300


class CarManager:
    
    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE


    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_segment = Turtle("square")
            new_segment.color(random.choice(COLORS))
            new_segment.shapesize(stretch_len=2, stretch_wid=1)
            new_segment.penup()
            new_segment.goto(START_X, random.randint(-250, 250))
            self.all_car.append(new_segment)
    
    def move_car(self):
        for car in self.all_car:
            car.backward(self.car_speed)

    def lvl_up(self):
        self.car_speed += MOVE_INCREMENT