#! /usr/bin/env python3
'''
commands:
    all - practice all kinds of questions
    addition
    subtraction
    multiplication
    division
shortcuts:
    Ctrl + i = list of commands
    Ctrl + r = return to menu
    Ctrl + e = exit game
    Ctrl + s = stats


'''
import random
from datetime import datetime as dt
import keyboard
import os

def loadHotKeys():
    keyboard.add_hotkey('ctrl+i', printHotKeys)
    keyboard.add_hotkey('ctrl+r', mainMenu)


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
    print("Ctrl + i = list of commands\nCtrl + r = return to menu\nCtrl + e = exit game\nCtrl + s = stats")

def sumProblem():
    num1 = random.randrange(1,2000)
    num2 = random.randrange(1,2000)
    answer = num1 + num2
    while True:
        startTime = dt.now()
        userAnswer = input("{} + {} = \n".format(num1, num2))

        try:
            if int(userAnswer) == answer:
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

        if int(userAnswer) == answer:
            endTime = dt.now()
            time = endTime - startTime
            print(time)
            break

def multProblem():
    num1 = random.randrange(1,12)
    num2 = random.randrange(1, 12)
    answer = num1 * num2
    while True:
        startTime = dt.now()
        userAnswer = input("{} * {} = \n".format(num1, num2))

        if int(userAnswer) == answer:
            endTime = dt.now()
            time = endTime - startTime
            print(time)
            break

def divideProblem():
    num1 = random.randrange(1, 12)
    num2 = random.randrange(num1, 100, num1)
    answer = num2 / num1
    while True:
        startTime = dt.now()
        userAnswer = input("{} / {} = \n".format(num1, num2))

        if int(userAnswer) == answer:
            endTime = dt.now()
            time = endTime - startTime
            print(time)
            break

print("This is a program for improving your math ability, press ctrl + i for a list of commands")
loadHotKeys()
mainMenu()