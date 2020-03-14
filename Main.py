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
TODO: Stats system
TODO: Setting system
TODO: Fix inconsistent quotations
'''

import random
from datetime import datetime as dt
import sys

# Git Test

# Create the required data files if they are not already created
def initialize():
    try:
        f = open('./mathProblemsData/AD_data.dat', 'r')
        if f.readline() != '# This is the header for AD_data\n':
            createFiles()
    except FileNotFoundError:
        createFiles()

def createFiles():

    f = open('./mathProblemsData/AD_data.dat', 'w+')
    f.write('# This is the data file for all addition questions\n')
    f.close()

    f = open('./mathProblemsData/SU_data.dat', 'w+')
    f.write('# This is the data file for all subtraction questions\n')
    f.close()

    f = open('./mathProblemsData/MU_data.dat', 'w+')
    f.write('# This is the data file for all multiplication questions\n')
    f.close()

    f = open('./mathProblemsData/DI_data.dat', 'w+')
    f.write('# This is the data file for all division questions\n')
    f.close()




def exitGame():
    print("Thanks for playing!")
    sys.exit()

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
        elif userInput == "exit":
            exitGame()

def saveData(type, timestamp, time):
    if type == 'addition':
        f = open('./mathProblemsData/AD_data.dat', 'a')
        f.write('{}, {}\n'.format(timestamp, time))
        f.close()
    elif type == 'subtraction':
        f = open('./mathProblemsData/SU_data.dat', 'a')
        f.write('{}, {}\n'.format(timestamp, time))
        f.close()
    elif type == 'multiplication':
        f = open('./mathProblemsData/MU_data.dat', 'a')
        f.write('{}, {}\n'.format(timestamp, time))
        f.close()
    elif type == 'division':
        f = open('./mathProblemsData/DI_data.dat', 'a')
        f.write('{}, {}\n'.format(timestamp, time))
        f.close()

def sumProblem():
    num1 = random.randrange(1,1000)
    num2 = random.randrange(1,1000)
    answer = num1 + num2
    while True:
        startTime = dt.now()
        userAnswer = input("{} + {} = \n".format(num1, num2))

        try:
            if userAnswer == 'cancel':
                mainMenu()
            elif userAnswer == 'exit':
                exitGame()
            elif int(userAnswer) == answer:
                endTime = dt.now()
                time = endTime - startTime
                print(time)
                saveData('addition', dt.now(), time)
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
            elif userAnswer == 'exit':
                exitGame()
            elif int(userAnswer) == answer:
                endTime = dt.now()
                time = endTime - startTime
                print(time)
                saveData('subtraction', dt.now(), time)
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
            elif userAnswer == 'exit':
                exitGame()
            elif int(userAnswer) == answer:
                endTime = dt.now()
                time = endTime - startTime
                print(time)
                saveData('multiplication', dt.now(), time)
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
            elif userAnswer == 'exit':
                exitGame()
            elif int(userAnswer) == answer:
                endTime = dt.now()
                time = endTime - startTime
                print(time)
                saveData('division', dt.now(), time)
                break
        except ValueError:
            pass

initialize()
print("This is a program for improving your mathematical ability.\nIf you are done practicing a specific type of question, type cancel to return to the main menu.\nType exit to exit the game.")
mainMenu()