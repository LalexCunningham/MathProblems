import re
from datetime import datetime
import datetime as dt

# Returns the average time recorded for a type of sum
def getAvg(sumType):
	', 0:00:16.167658'
	solveTimeRegex = re.compile(', \d:\d\d:\d\d.\d\d\d\d\d\d')
	solveTimes = []

	f = open('./mathProblemsData/{}_data.dat'.format(sumType), 'r')
	fList = f.readlines()

	totalTime = dt.timedelta()
	counter = 0
	for line in fList:	
		try:
			solveTime = solveTimeRegex.findall(line)[0]
		except IndexError:
			pass
		
		try:
			solveTime = dt.timedelta(hours = int(solveTime[2:3]), minutes = int(solveTime[4:6]), seconds = int(solveTime[7:9]), microseconds = int(solveTime[10:140]))
			totalTime = totalTime + solveTime
			counter = counter + 1
			#solveTimes.append(solveTime)
		except UnboundLocalError:
			pass
	try:
		return totalTime / counter
	except ZeroDivisionError:
		print('No records for this sum type!')
# Mainloop
while True:
	option = input('Which statistic would you like to look at?\n')
	if option == 'addition':
		print(getAvg('AD'))
		break
	elif option == 'subtraction':
		print(getAvg('SU'))
		break
	elif option == 'multiplication':
		print(getAvg('MU'))
		break
	elif option == 'division':
		print(getAvg('DI'))
		break
	else:
		print('Invalid input')