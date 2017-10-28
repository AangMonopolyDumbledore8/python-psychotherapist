#created by Andrew Ghastine
#with help from Baylen

#imports
import sys
import time
import random
#Colour codes
w  = "\033[0m" # white (normal)
r  = "\033[31m" # red
g  = "\033[32m" # green
o  = "\033[33m" # orange
b  = "\033[34m" # blue
p  = "\033[35m" # purple
#variables
problem = "someone hit you"
#lists
questions = ["what's your problem?", "why do you feel that way?", ("Is it because" + problem + "that you feel that way?")]
#userinput
userinput = input(b+random.choice(questions)+": "+w)
amountOftimesQuestionOnewasAsked = 0
x = 1
if (random.choice(questions)) == "what's your problem?":
    amountOftimesQuestionOnewasAsked = amountOftimesQuestionOnewasAsked + 1
while True:
    if (random.choice(questions)) == "what's your problem?":
        if (amountOftimesQuestionOnewasAsked) <= 1:
            problem = userinput
            userinput = input(random.choice(questions)+": ")
print ("done")
