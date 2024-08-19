def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
def up():
    move()
    turn_left()
    move()

def walk():
     up()
     turn_right()
     move()
     turn_right()
     move()
      
    
def run():

    walk()
    turn_left()
    walk()
    turn_left()
    walk()
    turn_left()
    walk()
    turn_left()
    walk()
    turn_left()
    walk()
    turn_left()

def jump ():
    walk()
    turn_left()
    

while at_goal() == False:
    if front_is_clear() == True:
           move()
    if wall_in_front() == True and right_is_clear() ==False:
           turn_left()

    if wall_on_right() == False:
        turn_right()
     
 

            

    
    

              









    











