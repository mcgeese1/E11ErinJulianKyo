import RPi.GPIO as GPIO
import datetime
import time
import csv

import sys


if len(sys.argv)<4:
    print("Script needs run_time (int) as input and file name")
    exit()

totaltime=int(sys.argv[1])
filename= str(sys.argv[2])
intervaltime=int(sys.argv[3])


channel= 17
#totaltime=300
starttime=time.time()
#intervaltime = 10
counts = 0
countslist = []


data=["Time", "Counts/"+str(intervaltime)]
#filename= "geiger.csv"

file = open(filename,"w",newline=None)
writer = csv.writer(file)
writer.writerow(data)

def my_callback(channel):
	global counts
	if GPIO.input(channel)==GPIO.LOW:
		print('Detection at ' + str(datetime.datetime.now()))
		counts += 1


GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(channel,GPIO.BOTH,callback=my_callback)
print("DEEZ NUTS")
	
	
while time.time() < totaltime+starttime:
	counts = 0
	time.sleep(intervaltime)
	print('\nThere were {} counts in the last {} seconds\n'.format(counts, intervaltime))
	countslist.append(counts)
	data = [time.time(),counts]
	writer.writerow(data)
	
print('list of interval counts: {}'.format(countslist))
print("Goodbye!")

file.close()






'''

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

tstart =time.time()
trun=60
countsper5seclist = []
tinterval=5

def my_callback(channel):
	if GPIO.input(channel)==GPIO.HIGH:
		print('\n at ' + str(datetime.datetime.now()))
	else:
		print('\n at ' + str(datetime.datetime.now()))

while time.time()<tstart+trun:

	
	t1=time.time()
	counts=0

	while (time.time()<t1+tinterval):

		channel = GPIO.wait_for_edge(channel, GPIO.FALLING,timeout=20000)
		if channel is None:
			print("Timout lol")
		else:
			print('Count detected at ' + str(datetime.datetime.now()))
			counts+=1
			
	countsper5seclist.append(counts)
	print('There were {} counts in he last {} seconds\n'.format(counts, tinterval))
	
print('{}'.format(countsper5seclist))
		
'''
