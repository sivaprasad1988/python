def turnRight():
    turn_left()
    turn_left()
    turn_left()

def trunUp():
    turn_left()

def trun_right():
    turn_left()
    turn_left()
    turn_left()

def moveBot():
    move()
    trunUp()
    move()
    turnRight()
    move()
    trunDown()
    move()

while not at_goal():
    if wall_on_right():
        turn_left()
    if wall_in_front():
        trun_right()
    if front_is_clear():
        move()
    else:
        turn_left()





################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
