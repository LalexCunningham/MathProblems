import re
from datetime import datetime
import datetime as dt
def getAvg(sumType):
	', 0:00:16.167658'
	solveTimeRegex = re.compile(', \d:\d\d:\d\d.\d\d\d\d\d\d')
	solveTimes = []

	f = open('./mathProblemsData/{}_data.dat'.format(sumType), 'r')
	fList = f.readlines()

	for line in fList:	
		try:
			solveTime = solveTimeRegex.findall(line)[0]
		except IndexError:
			pass
		
		try:
			solveTime = dt.timedelta(hours = solveTime[2:3], minutes = solveTime[4:6], seconds = solveTime[7:9], microseconds = int(solveTime[10:140]))

			#solveTime = dt.timedelta(solveTime[2:], '%H:%M:%S.%f')

			solveTimes.append(solveTime)
		except UnboundLocalError:
			pass
	
	print(sum(solveTimes))


while True:
	option = input('Which statistic would you like to look at?\n')
	if option == 'addition':
		getAvg('AD')
		break
	elif option == 'subtraction':
		getAvg('SU')
		break
	elif option == 'multiplication':
		getAvg('MU')
		break
	elif option == 'division':
		getAvg('DI')
		break
	else:
		print('Invalid input')