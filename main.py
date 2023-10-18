import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# import car class
enemy = CarManager()
# import score board
score = Scoreboard()
# call player
player = Player()
# call listen function
screen.listen()
# if user click UP ARROW turtle will move 10px distance
screen.onkeypress(fun=player.move , key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    enemy.create_car()
    enemy.move_car()

    #Detect collision to car 
    for car in enemy.all_car:
        if car.distance(player) < 20:
            game_is_on = False 
            score.game_over()
    
    #Detect player reach other side

    if player.is_finish():
        player.go_start()
        enemy.lvl_up()
        score.increase_level()


screen.exitonclick()