# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 14:16:13 2025

@author: erinm
"""

#weather


import adafruit_bme680
import time
import board
import csv

reset_pin = None

import serial
uart = serial.Serial("/dev/ttyS0", baudrate=9600, timeout=0.25)
from adafruit_pm25.uart import PM25_UART
pm25 = PM25_UART(uart, reset_pin)


import sys

print(sys.argv)

if len(sys.argv)<2:
    print("Script needs run_time (int) as input")
    exit()

run_time=int(sys.argv[1])

filename="Weather_AQI.cvs"

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

temp =0
humidity=0
press=0
alt=0
currenttime=time.time()
count=0

data=["Time","Temp","Gas","Humidity","Pressure","Alt","PM 1.0","PM 2.5","PM 10"]


file = open(filename,"w",newline=None)
writer = csv.writer(file)


while count < run_time:
    
    currenttime=time.time()
    
    try:
        aqdata = pm25.read()
        # print(aqdata)
    except RuntimeError:
        print("Unable to read from sensor, retrying...")
        continue
    
    
    temp, gas, humidity,press,alt=bme680.temperature, bme680.gas, bme680.relative_humidity,bme680.pressure,bme680.altitude

    
    print("\nTime:{}".format(currenttime))
    print("Temperature: %0.1f c" % temp)
    print("Gas: %d ohm" % gas)
    
    print("Humidity: %0.1f %%" % humidity)
    print("Pressure: %0.3f hPa" % press)
    print("altitude = %0.2f meters" % alt)
    print(
        "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
        % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
    )
	
    
    data=[currenttime,temp,gas, humidity,press,alt,aqdata["pm10 standard"],aqdata["pm25 standard"],aqdata["pm100 standard"]]
    writer.writerow(data)
	
    time.sleep(1)
    count+=1
    
file.close()
	
    
# #aqi
    
# print("Found PM2.5 sensor, reading data...")

# #file_writer.writerow(["PM 1.0","PM 2.5","PM 10"])
# it = 0

# while it<31:
#     time.sleep(1)

#     try:
#         aqdata = pm25.read()
#         # print(aqdata)
#     except RuntimeError:
#         print("Unable to read from sensor, retrying...")
#         continue

#     print()
#     print("Concentration Units (standard)")
#     print("---------------------------------------")
#     print(
#         "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
#         % (aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"])
#     )
#     print("Concentration Units (environmental)")
#     print("---------------------------------------")
#     print(
#         "PM 1.0: %d\tPM2.5: %d\tPM10: %d"
#         % (aqdata["pm10 env"], aqdata["pm25 env"], aqdata["pm100 env"])
#     )
#     print("---------------------------------------")
#     print("Particles > 0.3um / 0.1L air:", aqdata["particles 03um"])
#     print("Particles > 0.5um / 0.1L air:", aqdata["particles 05um"])
#     print("Particles > 1.0um / 0.1L air:", aqdata["particles 10um"])
#     print("Particles > 2.5um / 0.1L air:", aqdata["particles 25um"])
#     print("Particles > 5.0um / 0.1L air:", aqdata["particles 50um"])
#     print("Particles > 10 um / 0.1L air:", aqdata["particles 100um"])
#     print("---------------------------------------")
    
#     it+= 1
    
#     writer.writerow([aqdata["pm10 standard"], aqdata["pm25 standard"], aqdata["pm100 standard"]])
    





	