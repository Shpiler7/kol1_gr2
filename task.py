###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/kol1_gr2
#Good Luck
import random
import numpy as np
class Plane(object):
    angle = 90
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return self.name
    def tiltCorrection(self):
        self.angle = 90
    def currOrientation(self):
        print self.angle
    def turbulence(self):
        mu = 0
        sigma = 0.1
        s = np.random.normal(mu, sigma, 1000)
        self.angle = self.angle - random.randint(1, 10)


plane = Plane("plane")
print(plane)
print("Start orietation:"),
plane.currOrientation()
i = 0
while True:
    print("Turbulence"),
    plane.turbulence()
    print("Current orietation:"),
    plane.currOrientation()
    print("Correcting:"),
    plane.tiltCorrection()
    print("Corrected:"),
    plane.currOrientation()
    print("Contiunue? (Type 'stop' to finish)")
    text = raw_input()
    if text == "stop":
        break
