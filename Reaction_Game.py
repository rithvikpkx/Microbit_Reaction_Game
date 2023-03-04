#8.2
#Imports everything from the microbit module
from microbit import *

#8.2
#Imports the random module
import random

#8.6
#Defines a function called wait_button()
#In place of writing the entire block of code continously, the function can just be called whenever needed
#This makes the code readable and more efficient
def wait_button():
    
    #8.3
    #Infinitely loops the indented code block
    while True:
        
        #8.3
        #Checks if Button A was pressed, if pressed, then the function returns the booleon value True
        #Then checks if Button B was pressed, if pressed, then the function returns the booleon value True
        #If either Button A OR Button B was pressed, the conditional if statement runs the indented code block
        if button_a.was_pressed() or button_b.was_pressed():
            
            #8.3
            #Exits this infinite loop and executes the next piece of code
            break
        
        
#8.5
while True:
    
    #8.2
    #Scrolls the string, "321" across the microbit screen
    #This is a countdown for the player to get ready
    display.scroll("321")
    
    #8.2
    #Takes a random number from 1000 to 5000
    #Assigns this number to variable delay_time
    delay_time = random.randrange(1000,5000)
    
    #8.2
    #Waits for "delay_time" number of millseconds before moving on
    #This will make it hard for the player to predict when the target will appear
    #Therefore it will test the raw reaction time of the player
    sleep(delay_time)
    
    #8.2
    #Shows an image of a target on the microbit screen
    display.show(Image.TARGET)
    
    #8.3
    #Measures the amount of time the program has been running
    #Assigns this time to the variable start_time
    start_time = running_time()
    
    #8.6
    #Calls the function wait_button()
    wait_button()
    
    #8.3
    #Subtracts the value of variable start_time from the value that the function running_time() returns
    #Assigns this new subtracted value to variable reaction_time
    reaction_time = running_time() - start_time
    
    #8.4
    #Converts the value of variable reaction_time to a string and infinitely scrolls it across the microbit screen
    display.scroll(str(reaction_time), loop = True, wait = False)
    
    #8.6
    #Calls the function wait_button()
    wait_button()
