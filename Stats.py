import re
from datetime import datetime
import datetime as dt

# TODO: Get weekly averages

# Returns a list of moving averages, average changes with each problem solved, last list item is the overall average
def getMovingAvg(sumType):
	', 0:00:16.167658'
	solveTimeRegex = re.compile(', \d:\d\d:\d\d.\d\d\d\d\d\d')
	solveTimes = []
	averages = []
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
			averages.append(totalTime / counter)
		except UnboundLocalError:
			pass
	try:
		return averages
	except ZeroDivisionError:
		print('No records for this sum type!')
		
# Mainloop
while True:
	option = input('Which statistic would you like to look at?\n')
	if option == 'addition':
		avgs = getMovingAvg('AD')
		for avg in avgs:
			print(avg)
		break
	elif option == 'subtraction':
		avgs = getMovingAvg('SU')
		break
	elif option == 'multiplication':
		avgs = getMovingAvg('MU')
		break
	elif option == 'division':
		avgs = getMovingAvg('DI')
		break
	else:
		print('Invalid input')