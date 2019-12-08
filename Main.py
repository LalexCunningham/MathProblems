#! /usr/bin/env python3
'''
Program should give a selection of math problems that the user should solve in as little time as possible.
The program should save the time taken to solve a specific category of question, and provide statistics on this.
commands:
    all - practice all kinds of questions
    addition
    subtraction
    multiplication
    division

    Type cancel to return to main menu

shortcuts:
    Ctrl + i = list of commands
TODO:
    Ctrl + e = exit game
    Ctrl + s = stats
'''

import random
from datetime import datetime as dt
import keyboard
import os

def loadHotKeys():
    # TODO: Make this only work on main menu
    keyboard.add_hotkey('ctrl+i', printHotKeys)
    #keyboard.add_hotkey('ctrl+r', mainMenu)


def mainMenu():
    while True:
        userInput = input("What kind of questions would you like to practice?\n[all, addition, subtraction, multiplication, division]\n")
        if userInput == "all":
            while True:
                problemType = random.randrange(1,4)
                if problemType == 1:
                    sumProblem()
                elif problemType == 2:
                    minusProblem()
                elif problemType == 3:
                    multProblem()
                elif problemType == 4:
                    divideProblem()

        elif userInput == "addition":
            while True:
                sumProblem()

        elif userInput == "subtraction":
            while True:
                    minusProblem()

        elif userInput == "multiplication":
            while True:
                    multProblem()

        elif userInput == "division":
            while True:
                    divideProblem()



def printHotKeys():
    print("Ctrl + i = list of commands\nCtrl + e = exit game\nCtrl + s = stats\nTo stop practicing a specific problem type and return to the main menu, type: cancel")

def sumProblem():
    num1 = random.randrange(1,2000)
    num2 = random.randrange(1,2000)
    answer = num1 + num2
    while True:
        startTime = dt.now()
        userAnswer = input("{} + {} = \n".format(num1, num2))

        try:
            if userAnswer == 'cancel':
                mainMenu()
            elif int(userAnswer) == answer:
                endTime = dt.now()
                time = endTime - startTime
                print(time)
                break
        except ValueError:
            pass

def minusProblem():
    num1 = random.randrange(1,2000)
    num2 = random.randrange(1,2000)
    answer = num1 - num2
    while True:
        startTime = dt.now()
        userAnswer = input("{} - {} = \n".format(num1, num2))

        try:
            if userAnswer == 'cancel':
                mainMenu()
            elif int(userAnswer) == answer:
                endTime = dt.now()
                time = endTime - startTime
                print(time)
                break
        except ValueError:
            pass

def multProblem():
    num1 = random.randrange(1,12)
    num2 = random.randrange(1, 12)
    answer = num1 * num2
    while True:
        startTime = dt.now()
        userAnswer = input("{} * {} = \n".format(num1, num2))

        try:
            if userAnswer == 'cancel':
                mainMenu()
            elif int(userAnswer) == answer:
                endTime = dt.now()
                time = endTime - startTime
                print(time)
                break
        except ValueError:
            pass

def divideProblem():
    num1 = random.randrange(1, 12)
    num2 = random.randrange(num1, 100, num1)
    answer = num2 / num1
    while True:
        startTime = dt.now()
        userAnswer = input("{} / {} = \n".format(num1, num2))

        try:
            if userAnswer == 'cancel':
                mainMenu()
            elif int(userAnswer) == answer:
                endTime = dt.now()
                time = endTime - startTime
                print(time)
                break
        except ValueError:
            pass

print("This is a program for improving your math ability, press ctrl + i for a list of commands\nIf you are done practicing a specific question, type cancel to return to the main menu")
loadHotKeys()
mainMenu()