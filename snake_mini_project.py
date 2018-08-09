# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle
import random #We'll need this later in the lab

color_bg = input('what color do you want your backgruond to be?')
turtle.bgcolor(color_bg)

score = 0

border=turtle.clone()
border.penup()
border.goto(-350,-200)
border.pendown()
border.goto(350,-200)
border.goto(350,200)
border.goto(-350,200)
border.goto(-350,-200)
border.penup()

title=turtle.clone()
title.penup()
title.goto(-50,220)
title.write("Yuval's game", font=("arial",20))



turtle.tracer(1,0) #This helps the turtle move more smoothly

SIZE_X=800
SIZE_Y=500
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 6

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

#Set up positions (x,y) of boxes that make up the snake
snake = turtle.clone()
snake.shape("square")

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(START_LENGTH):
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1]

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(x_pos,y_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    snake_stamp= snake.stamp()
    stamp_list.append(snake_stamp)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
DOWN=1
LEFT=2
RIGHT=3
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!

direction = UP
UP_EDGE = 200
DOWN_EDGE = -200
RIGHT_EDGE = 350
LEFT_EDGE = -350

def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    #Update the snake drawing <- remember me later
    print("You pressed the up key!")
turtle.onkeypress(up, UP_ARROW) # Create listener for up key
turtle.listen()

def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
     #Update the snake drawing <- remember me later
    print("You pressed the down key!")
turtle.onkeypress(down,DOWN_ARROW)
turtle.listen()


def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
   #Update the snake drawing <- remember me later
    print("You pressed the left key!")
turtle.onkeypress(left, LEFT_ARROW)
turtle.listen()

def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
    #Update the snake drawing <- remember me later
    print("You pressed the right key!")
turtle.onkeypress(right,RIGHT_ARROW)
turtle.listen()
#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!



#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!
def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    min_x=-int(350/2/SQUARE_SIZE)+1
    max_x=int(350/2/SQUARE_SIZE)-1
    min_y=-int(200/2/SQUARE_SIZE)-1
    max_y=int(200/2/SQUARE_SIZE)+1
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE

        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position
    food.goto(food_x,food_y)
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
    food_pos.append((food_x,food_y))
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list
    food_stamps1 = food.stamp()
    food_stamps.append(food_stamps1)

def move_snake():
    print('move snake called')
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if my_pos in pos_list[:-1]:
        print("you ate yourself bitchhhhh")
        quit()
        
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos,y_pos+SQUARE_SIZE)
        print("you moved up!")
    else:
        snake.goto(x_pos,y_pos-SQUARE_SIZE)
        print("you moved down!") 

    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print("You hit the right edge! Game over!")
        quit()
    elif new_x_pos<= LEFT_EDGE:
        print("you hit the left edge!")
        quit()
    elif new_y_pos>= UP_EDGE:
        print("you hit the up edge!")
        quit()
    elif new_y_pos<=DOWN_EDGE:
        print("you hit the down edge!")
        quit()
    
        

    
        #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
        ######## SPECIAL PLACE - Remember it for Part 5
        #pop zeroth element in pos_list to get rid of last the last 
        #piece of the tail
   


    ######## SPECIAL PLACE - Remember it for Part 5
    global food_stamps, food_pos, score
    #If snake is on top of food item
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print("You have eaten the food!")
        score += 1
    #HINT: This if statement may be useful for Part 8
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)

    #Don't change the rest of the code in move_snake() function:
    #If you have included the timer so the snake moves 
    #automatically, the function should finish as before with a 
    #call to ontimer()

    if len(food_stamps) <= 6 :
        make_food()
    turtle.clear()

    timestep = score_to_timestep(score)

    turtle.write(score, font=('Arial', 20))
    turtle.penup
    turtle.goto(-350,210)
    turtle.ontimer(move_snake,timestep) #<--Last line of function

def score_to_timestep(score_int):
    #for score of 0, should output 100
    timestep = 100
    num_speedups = score_int//5

    for five_point_speedup in range(num_speedups):
        timestep = timestep / 1.5

    timestep = int(timestep)

    print('timestep; ' + str(timestep))
    print('score: ' + str(score_int))
    
    if timestep == 0:
        return 1
    else:
        return timestep
        
    
    
    

turtle.register_shape("trash.gif") #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script

food = turtle.clone()
food.shape("trash.gif") 

#Locations of food
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []

# Write code that:
#1. moves the food turtle to each food position
for i in food_pos :
    food.goto(i)
    food_id=food.stamp()
    food_stamps.append(food_id)

#2. stamps the food turtle at that location
#3. saves the stamp by appending it to the food_stamps list using
# food_stamps.append(    )
#4. Don’t forget to hide the food turtle!



    ####WRITE YOUR CODE HERE!!



move_snake()
turtle.mainloop()
