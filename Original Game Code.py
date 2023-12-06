#AP: Alexa Pollard
#AAP: Aditi Patel
#VK: Venusha Kirupakaran
#AK: Abhilash Jakanathan

from itertools import cycle     #AAP: importing cycle from itertools to create a colour cycle
from random import randrange  #AAP: importing randrange from random to generate random numbers
from tkinter import Canvas, Tk, messagebox, font #AAP: importing Tinkter modules

canvas_width = 800  #AAP: setting up canvas width
canvas_height = 400 #AAP: setting up canvas height

root = Tk() #AAP: creates Tinkter window
root.title("Egg Catcher") #AAP: titles the window
c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue") #AAP: creates a canvas with a specified width, height, and background colour
c.create_rectangle(-5, canvas_height-100, canvas_width+5, canvas_height+5, fill="sea green", width=0) #AAP: creates a sea green rectangle to represent the grass
c.create_oval(-80, -80, 120, 120, fill='orange', width=0) #AAP: creates an orange oval to represent the sun
c.pack() #AAP: packs the canvas into the Tinkter window

color_cycle = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"]) #AAP: defines a colour cycle for the eggs
egg_width = 45 #AAP: width of the eggs
egg_height = 55 #AAP: height of the eggs
egg_score = 10 #AAP: score per egg collected
egg_speed = 500 #AAP: speed that eggs fall at
egg_interval = 4000 #AAP: interval between egg drops
difficulty = 0.95 #AAP: level of difficulty
catcher_color = "blue" #AAP: colour of the catcher
catcher_width = 100 #AAP: width of the catcher
catcher_height = 100 #AAP: height of the catcher
catcher_startx = canvas_width / 2 - catcher_width / 2 #AAP: starting x coordinate of the catcher
catcher_starty = canvas_height - catcher_height - 20 #AAP: starting y coordinate of the catcher
catcher_startx2 = catcher_startx + catcher_width #AAP: ending x coordinate of the catcher
catcher_starty2 = catcher_starty + catcher_height #AAP: ending y coordinate of the catcher

catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=3) #AAP: creating the catcher on the canvas
game_font = font.nametofont("TkFixedFont") #AAP: retrieving the Tinkter fixed font
game_font.config(size=18) #AAP: setting a size for the font


score = 0 #AAP: sets intial score
score_text = c.create_text(10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: "+ str(score)) #AAP: displays score on canvas

lives_remaining = 3 #AAP: sets initial number of lives
lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkblue", text="Lives: "+ str(lives_remaining)) #AAP: displays number of lives on canvas

eggs = [] #AJ: To keep track of the eggs in the game, this initializes the variable 'eggs' into a list

def create_egg(): #AJ: Function is used to create new eggs in the game
    x = randrange(10, 740) #AJ: Chooses random x-coordinates for the new eggs to spawn at
    y = 40 #AJ: The eggs will be dropped from the same initial starting height so the y-coordinate will remain constant
    new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0) #AJ: c.create_oval uses canvas, a widget used to create structural graphics, in order to create the oval shape. After defining the boundaries of the oval with x and y, it fills in the oval with a random colour on the colour cycle. The width is set to 0 so there is no border and an oval filled with a single colour is created
    eggs.append(new_egg) #AJ  Keeps track of all the eggs in the game by referencing the new eggs created to the 'eggs' list.
    root.after(egg_interval, create_egg) #AJ:  Manages the intervals in which the eggs are created by calling on the 'create_egg' function after a specific time interval. The 'after' part of the functon is used to delay the calling of the create_function

def move_eggs(): #AJ: Function moves eggs down the screen
    for egg in eggs: #AJ: Creates a loop that will go through every egg in the list 'eggs'
        (eggx, eggy, eggx2, eggy2) = c.coords(egg) #AJ: Retrieves the coordinates off the boundaries of the eggs. It gets the x and y coordinates of the top-left and bottom-right corner.
        #print(c.coords(egg)) #AJ: 
        c.move(egg,0, 10)  #AJ: This moves the egg down the canvas. The first item is what needs to be moved down, the second is the x-coordinate, which should remain the same, and lastly, the y-coordinate will move down by 10 pixels.
        if eggy2 > canvas_height: #AJ: Checks if the bottom corner of the egg has gone greater than/beyond the height of the canvas. This checks if the egg has reached the bottom.
            egg_dropped(egg) #When the egg has reached the bottom, the egg drop function will be called. This will get rid of the egg, take away a life from the player and check if the game is done. (The player has ran out of lives)
    root.after(egg_speed, move_eggs) #After a specific time, this function is called again to move another egg, creating a loop.

def egg_dropped(egg): #AJ: Defines the parameter for the egg that has reached the bottom
    eggs.remove(egg) #AJ: Removes the eggs the egg list, which is used to track all the eggs on the canvas at the time.
    c.delete(egg) #AJ: Removes the egg from the canvas (the graphical representation of the egg)
    lose_a_life() #Calls the lose_a_life function to indicate that the player has lost a life.
    if lives_remaining == 0:    #AJ: Sets a condition for when the player runs out of lives (If the lives_remaining is = 0, then they have ran out)
        messagebox.showinfo("Game Over!", "Final Score: "+ str(score)) #AJ: A message will appear on the screen telling the player that the game is over, including their final score. To do this, the score will be converted into a string so it can be displayed with the other text.
        root.destroy() #AJ: Closes the game window since the game is over

def lose_a_life(): #AP: Takes a life away by  an increment of 1 whenever the egg doesnt fall in the basket
    global lives_remaining #AP: Changes the lives_remaining variable from a local to a global variable, so we can call on it throughout the code
    lives_remaining -= 1 #AP: Reduces the lives_remaining value by 1, showing that a player has lost a life.
    c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining)) #AP: Updates the value of lives remaining on the screen. It updates the displayed text on the canvas where it says 'Lives' and it does this by converting the numerical value of remaining lives into a string.

def check_catch(): # VK This function checks for when collisions occur between the lists 'catcher' and 'egg'. In terms of the game, this refers to when the player catches an egg in the basket
    (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher) #VK assigns the top left and bottom right coordinates of the catcher on the canvas

    for egg in eggs: # VK Starts a for loop that checks through each egg in the list 
        (eggx, eggy, eggx2, eggy2) = c.coords(egg) #VK simalary to the catcher coords, this assigns the coords of the egg on the canvas ???
        if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40: # VK simalary to the catcher coords, this retrieves the coords of the egg on the canvas
            eggs.remove(egg) # VK if this is true then it removes the egg from the list.
            c.delete(egg) # VK Deletes the graphics of the egg on the screen
            increase_score(egg_score) # VK  Increases the score by 10 points
    root.after(100, check_catch) # VK Schedules function to reoccur this function after 100ms 

def increase_score(points): # VK This function increases the points of the user with the parameter points
    global score, egg_speed, egg_interval #VK The variables 'score', 'egg_speed', and 'egg_interval' can be accessed outside the function and through out the script
    score += points # VK Score is increased by the value of points
    egg_speed = int(egg_speed * difficulty) # VK After taking the int value of the egg_speed, it is multiplied by the difficulty, gradually increasing the speed in which the eggs fall
    egg_interval = int(egg_interval * difficulty) # VK  egg_interval is multiplied by the difficulty to decrease the interval in which the eggs are spawning
    c.itemconfigure(score_text, text="Score: "+ str(score)) # VK Updates the score displayed on the screen every time it changes
    
def move_left(event): #VK This function moves the catcher left
    (x1, y1, x2, y2) = c.coords(catcher) # VK Assigns catchers coords to x1, y1, x2 ,y2
    if x1 > 0: # VK Checks if x1 is not at the very left side of the canvas (if x1 is greater than 0). This ensures that the catcher doesn’t go too far left off the canvas.
        c.move(catcher, -20, 0) # VK it moves the catcher left by 20 units if the catcher isn’t too far to the left where it can leave the screen

def move_right(event): # VK This function moves the catcher right
    (x1, y1, x2, y2) = c.coords(catcher) #VK Assigns catchers coords to these variables
    if x2 < canvas_width: # VK checks if the x2 is not at the very right of the canvas (if  x2 less than 800)
        c.move(catcher, 20, 0) # VK moves the catcher to the right by 20 units of the catcher isn’t too far to the right that it will leave the screen

c.bind("<Left>", move_left)  #AAP: binds the move left to pressing the left key
c.bind("<Right>", move_right) #AAP: binds the move right to pressing the right key
c.focus_set() #AAP: refers to the window recieiving keyboard input, prevents other keyboard inputs
root.after(1000, create_egg) #AAP: schedules the creation of the egg after 1000 miliseconds
root.after(1000, move_eggs) #AAP: schedules the movement of the egg after 1000 miliseconds
root.after(1000, check_catch) #AP: checks the catch after 1000 miliseconds
root.mainloop() #AP: game will go on forever until the user runs out of lives and closes the window

#Coded with 💙 by Mr. Unity Buddy #AAP: thank you for this lovely code Mr. Unity Buddy
