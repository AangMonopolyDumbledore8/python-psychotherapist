#created by Andrew Ghastine
#with help from Baylen

#imports
import sys
import time
import random
#Color codes
w  = "\033[0m" # white (normal)
r  = "\033[31m" # red
g  = "\033[32m" # green
o  = "\033[33m" # orange
b  = "\033[34m" # blue
p  = "\033[35m" # purple
#variables
problemDefault = input(p+ "Name something bad that happened in your life: ")
counter = 0
#Definitions
#addToVar()
#nonlocal counter = counter + 1
#lists
questions = ["what's your problem?", "why do you feel that way?", ("Is it because of " + problemDefault + " that you feel that way?")]
#userinput
userinput = input(b+random.choice(questions)+": "+w)
x = 1
if (random.choice(questions)) == "what's your problem?":
    addToVar()
while True:
    if (random.choice(questions)) == "what's your problem?":
        #if (counter) <= 1:
            userinput = input(random.choice(questions)+": ")
            problem = userinput
            questions = ["what's your problem?", "why do you feel that way?", ("Is it because of " + problem + " that you feel that way?")]
print ("done")
