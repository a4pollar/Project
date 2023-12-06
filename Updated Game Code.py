#AP: Alexa Pollard
#AAP: Aditi Patel
#VK: Venusha Kirupakaran
#AK: Abhilash Jakanathan

#AAP: Importing all the necessary libraries and modulus 
from itertools import cycle     
from random import randrange
from tkinter import Canvas, Tk, messagebox, font
from tkinter import*
from PIL import Image,ImageTk

#AAP: Sets up the dimensions of the canvas
canvas_width = 800
canvas_height = 400

#AAP: letting up the window and canvas
root = Tk() #AAP: Creates Tinkter window
root.title("Egg Catcher") #AAP: Titles the window
c = Canvas(root, width=canvas_width, height=canvas_height, background="deep sky blue") #AAP: Creates a canvas with a specified width, height, and background colour
c.pack(expand = YES, fill = BOTH)   #AAP: packs the canvas into the Tinkter window

#Defining variables
color_cycle = cycle(["light blue", "light green", "light pink", "light yellow", "light cyan"])
egg_width = 45
egg_height = 55
egg_score = 10          #AP: Score if a normal crabapple is eaten by goose
egg_score1 = 20         #AP: Score if a golden crabapple is eaten by goose
egg_score2 = -15        #AP: Score if a bomb hits the goose
egg_speed = 200         #AP: Speed at which the eggs falls was increased to make the game harder from the start
egg_interval = 2000     #AP: Speed at which the eggs are generated was increased to make the game harder from the start
difficulty = 0.95
catcher_color = "green"
catcher_width = 80
catcher_height = 80
catcher_startx = canvas_width / 2 - catcher_width / 2
catcher_starty = canvas_height - catcher_height - 20
catcher_startx2 = catcher_startx + catcher_width
catcher_starty2 = catcher_starty + catcher_height

#AAP: Creates the egg catcher
catcher = c.create_arc(catcher_startx, catcher_starty, catcher_startx2, catcher_starty2, start=200, extent=140, style="arc", outline=catcher_color, width=0)

#AAP: Defining the font of the text displayed on the screen
game_font = font.nametofont("TkFixedFont")
game_font.config(size=18)

eggs = []   #AJ: Creates an empty list that keeps track of the eggs in the game

#AJ: Function that creates and randomly prints an egg to the screen
def create_egg():
    x = randrange(10, 740)      
    y = 40
    new_egg = c.create_oval(x, y, x+egg_width, y+egg_height, fill=next(color_cycle), width=0)
    c.lower(new_egg)            #AJ: Places the egg behind the background, so that it cannot be seen by the user
    eggs.append(new_egg)        
    return x                    #AP: Returns the initial x coordinate of the egg so that the corresponding image can be printed at the same location


def Images():                                                       #AP: Function assigns each image to its associated egg and prints the image to the screen
    global apple_golden, bomb, heart, apple_red, apple_orange       #AP: Defines variables for the images as global so that they can be called at other areas in the code
    x=create_egg()                                                  #AP: Determines the x coordinate of the egg being printed 
    for egg in eggs:                                                #AP: Goes through each egg in the list of eggs
        if eggs[-1]==egg:                                           #AP: The list of eggs can contain multiple eggs at a time (multiple eggs are on the screen at a time), so only the last item of the list is checked, since every egg will be the last item of the list when it is first printed
            x+=25                                                   #AP: Adds 25 to the x coordinate of the egg, so that the image is centered in the egg
#AP: Every object in tkinter is defined by a number (ex. first object created is defined '1'). So the number assosiated to each egg can be used to assign the images to specific eggs. 
#AP: There are a total of 15 objects created in the code, but since the eggs/images are constanly being created and destoryed, their associated object numbers are also changing. 
#AP: The first 5 object values don't change, so there are only 10 object numbers that are changing, and since the object values are changing by 10, the one's digit will remain the same every cycle, and checking the last digit will always tell you what egg is bing created [(object value)%10 determines the ones digit of the object value]         
            if egg%10 == 6:                             #AP: The first egg has an intial object value of 6 and will always have 6 has a ones digit, so its object value%10 will always equal 6  
                bomb=c.create_image(x,100,image=Bomb)   #AP: Creates and displays the bomb image overtop of the corsponding egg
            elif egg%10 == 8:                           #AP: The second egg has an intial object value of 8 and will always have 8 has a ones digit, so its object value%10 will always equal 8
                heart=c.create_image(x,100,image=Heart) #AP: Creates and displays the heart image overtop of the corsponding egg  
            elif egg%10 ==0:                            #AP: The third egg has an intial object value of 10 and will always have 0 has a ones digit, so its object value%10 will always equal 0
                apple_red=c.create_image(x,100,image=Apple_red)         #AP: Creates and displays the red apple image overtop of the corresponding egg
            elif egg%10 == 2:                                           #AP: The forth egg has an initial object value of 12 and will always have 2 has a ones digit, so its object value%10 will always equal 2
                apple_orange=c.create_image(x,100,image=Apple_orange)   #AP: Creates and displays the orange apple image overtop of the corresponding egg
            elif egg%10 == 4:                                           #AP: The fifth egg has an initial object value of 14 and will always have 4 has a ones digit, so its object value%10 will always equal 4
                apple_golden=c.create_image(x,100,image=Apple_golden)   #AP: Creates and displays the golden apple image overtop of the corresponding egg
    root.after(egg_interval, Images)                                    #AP:Schedules function to repeat everytime an egg is created

def lose_a_life():              #AJ: Takes a life away by an increment of 1 whenever an egg doesnt touch the goose
    global lives_remaining
    lives_remaining -= 1        #AJ: Subtracts 1 from the users lives
    c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining))

def gain_a_life():              #AP: Gives a life by an increment of 1 whenever an egg touchs the goose
    global lives_remaining
    lives_remaining += 1        #AP: Adds 1 to the users lives
    c.itemconfigure(lives_text, text="Lives: "+ str(lives_remaining))

def egg_dropped(egg):           #VK: Function that defines the parameter for an egg that has reached the bottom
    lose_a_life()
    eggs.remove(egg)
    c.delete(egg)
    if lives_remaining < 1:
        messagebox.showinfo("Game Over!", "Final Score: "+ str(score))
        root.quit()             #AAP: Closes down the window

def move_eggs():                                        #AP: Function that moves eggs/images on the screen, and deletes them if they get to the bottom of the screen
    for egg in eggs:                                    #AP: Creates a loop that will go through every egg in the list 'eggs'
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)      #AP: Finds the coordinates of the egg being created
        c.move(egg,0, 10)                               #AP: moves the egg 10 units down from its intial position 
        if egg%10 == 6:                                 
            c.move(bomb,0,10)                           #AP: If the specific egg is first egg, move the bomb image down 10 units
        elif egg%10 == 8:                               
            c.move(heart,0,10)                          #AP: If the specific egg is second egg, move the heart image down 10 units
        elif egg%10 == 0:
            c.move(apple_red,0,10)                      #AP: If the specific egg is third egg, move the red apple image down 10 units
        elif egg%10 == 2:
            c.move(apple_orange,0,10)                   #AP: If the specific egg is fourth egg, move the orange apple image down 10 units
        elif egg%10 == 4:
            c.move(apple_golden,0,10)       #AP: If the specific egg is fifth egg, move the golden image down 10 units
        if eggy2 > canvas_height:           #AP: Checks to see if the egg has hit the bottom of the screen
            if egg%10 == 6:                 #AP: If the egg/bomb image hits the bottom of the screen, delete the egg and image
                eggs.remove(egg)            #AP: Removes the eggs the egg list
                c.delete(egg)               #AP: Removes the egg from the screen
                c.delete(bomb)              #AP: Removes the bomb image from the screen
            elif egg%10 == 8:               #AP: If the egg/heart image hits the bottom of the screen, delete the egg and image, and have user loss a life
                egg_dropped(egg)            #AP: Calls egg_dropped function that deletes the egg from the egg list and the screen, and calls the lose_a_life function that causes the user to loss a life
                c.delete(heart)             #AP: Removes the heart image from the screen
            elif egg%10 == 4:               #AP: If the egg/golden apple image hits the bottom of the screen, delete the egg and image, and have user loss a life
                egg_dropped(egg)
                c.delete(apple_golden)
            elif egg%10 == 2:               #AP: If the egg/orange apple image hits the bottom of the screen, delete the egg and image, and have user loss a life
                egg_dropped(egg)
                c.delete(apple_orange)
            elif egg%10 == 0:               #AP: If the egg/red apple image hits the bottom of the screen, delete the egg and image, and have user loss a life
                egg_dropped(egg)
                c.delete(apple_red)
    root.after(egg_speed, move_eggs)        #AP: Schedules function to repeat everytime an egg is created

def check_catch():              #VK: Function checks for when collisions occur between the catcher/goose image and an egg
    (catcherx, catchery, catcherx2, catchery2) = c.coords(catcher)      #VK: Determines the coordinates of the catcher/goose image
    for egg in eggs:                                                    #VK: Creates a loop that will go through every egg in the list 'eggs'
        (eggx, eggy, eggx2, eggy2) = c.coords(egg)                      #VK: Determines the coordinates of the egg
        if catcherx < eggx and eggx2 < catcherx2 and catchery2 - eggy2 < 40:        #VK: Checks to see if there is a collision between the catcher/goose image and an egg
            if egg%10 == 6:                         #AP: If the egg/bomb image hits the catcher/goose image, the user loses a life and 15 points to their score                 
                increase_score(egg_score2)          #AP: The increase_score function is called and 15 points is subtracted from the users score
                lose_a_life()                       #AP: The lose_a_life function is called and the user loses a life
                c.delete(bomb)                      #AP: Bomb image is deleted from the screen
            elif egg%10 == 8:                       #AP: If the egg/heart image hits the catcher/goose image, the user gains a life
                gain_a_life()                       #AP: The gain_a_life function is called and the user gains a life
                c.delete(heart)                     #AP: Heart image is deleted from the screen
            if egg%10 == 4:                         #AP: If the egg/golden apple image hits the catcher/goose image, the user gets 20 points added to their score
                c.delete(apple_golden)              #AP: Golden apple image is deleted from the screen
                increase_score(egg_score1)          #AP: The increase_score funciton is called, and the user gains 20 points
            elif egg%10 == 2:                       #AP: If the egg/orange apple image hits the catcher/goose image, the user gets 10 points added to their score
                c.delete(apple_orange)              #AP: Orange apple image is deleted from the screen
                increase_score(egg_score)           #AP: The increase-score function is called, and the user gains 10 points
            elif egg%10 == 0:                       #AP: If the egg/red apple image hits the catcher/goose image, the user gets 10 points added to their score
                c.delete(apple_red)                 #AP: Red apple image is deleted from the screen
                increase_score(egg_score)           #AP: The increase-score function is called, and the user gains 10 points
            eggs.remove(egg)                        #AP: Removes the eggs the egg list
            c.delete(egg)                           #AP: Removes the egg from the screen
    root.after(100, check_catch)                    #AP: Schedules function to repeat everytime an egg is created
            
def increase_score(points): # VK: This function increases the points of the user with the parameter points
    global score, egg_speed, egg_interval #VK: The variables 'score', 'egg_speed', and 'egg_interval' can be accessed outside the function and through out the script
    score += points # VK: Score is increased by the value of points
    egg_speed = int(egg_speed * difficulty) # VK: Egg_speed is the int value of the initial egg_speed times the difficulty
    egg_interval = int(egg_interval * difficulty) # VK: egg_intercal is the int value of the intial egg_interval times the difficultt
    c.itemconfigure(score_text, text="Score: "+ str(score)) #: VK Updates the score displayed on the screen every time it changes

def move_left(event): #VK: This function moves the catcher left
    (x1, y1, x2, y2) = c.coords(catcher) # VK: Assigns catchers coords to x1, y1, x2 ,y2
    if x1 > 0: # VK: Checks if x1 is not at the very left side of the canvas (if x1 is greater than 0)
        c.move(catcher, -20, 0) # VK: it moves the catcher left by 20 units
        c.move(goose, -20, 0) # VK: moves goose 20 units left

def move_right(event): # VK This function moves the catcher right
    (x1, y1, x2, y2) = c.coords(catcher) #VK Assigns catchers coords to these variables
    if x2 < canvas_width: # VK checks if the x2 is not at the very right of the canvas (if  x2 less than 800)
        c.move(catcher, 20, 0) # VK moves the catcher to the right by 20 units
        c.move(goose, 20, 0) # VK Moves goose 20 units right

#AP: Displays the background picture on the window
background=Image.open("background1.gif")
background=background.resize((810,410))
background=ImageTk.PhotoImage(background)
c.create_image(0,0,anchor='nw',image=background)

#AAP: Sets score to zero and creates and displays the textbox that shows the user the score
score = 0
score_text = c.create_text(10, 10, anchor="nw", font=game_font, fill="darkblue", text="Score: "+ str(score))

#AAP: Sets the lives remaining to three and creates and displays the textblock that shows the user their lives remaining
lives_remaining = 3
lives_text = c.create_text(canvas_width-10, 10, anchor="ne", font=game_font, fill="darkblue", text="Lives: "+ str(lives_remaining))

#AP: Defining the various images
#AP: Displaying Goose image to the useer
Goose=Image.open("crabapple.gif")
Goose=Goose.resize((200,200))
Goose=ImageTk.PhotoImage(Goose)
goose=c.create_image(310,250,anchor='nw',image=Goose)

#AP: Initalizes the golden apple image
Apple_golden=Image.open("crappl (4).gif")
Apple_golden=Apple_golden.resize((300,300))
Apple_golden=ImageTk.PhotoImage(Apple_golden)

#AP: Initalizes the bomb image
bomb=Image.open("Bomb.gif")
bomb=bomb.resize((180,180))
Bomb=ImageTk.PhotoImage(bomb)

#AP: Initalizes the heart image
heart=Image.open("Heart.gif")
heart=heart.resize((250,250))
Heart=ImageTk.PhotoImage(heart)

#AP: Initalizes the red apple image
Apple_red=Image.open("crappl.gif")
Apple_red=Apple_red.resize((300,300))
Apple_red=ImageTk.PhotoImage(Apple_red)

#AP: Initalizes the orange apple image
Apple_orange=Image.open("crappl (3).gif")
Apple_orange=Apple_orange.resize((300,300))
Apple_orange=ImageTk.PhotoImage(Apple_orange)


c.bind("<Left>", move_left)
c.bind("<Right>", move_right)
c.focus_set()
root.after(1000, Images)        #AP: Assigns each image to their corresponding egg and prints egg and image to the screen
root.after(1000, move_eggs)
root.after(1000, check_catch)
root.mainloop()
