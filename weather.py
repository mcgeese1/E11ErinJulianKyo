#print('hello world')
import adafruit_bme680
import time
import board
import csv

i2c = board.I2C()
bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c)

bme680.sea_level_pressure = 1013.25

temp =0
humidity=0
press=0
alt=0
starttime=time.time()
time1=time.time()

data=["Temp","Gas","Humidity","Pressure","Alt"]
with open('my_data.csv','a', newline='') as file:
	writer=csv.writer(file)
	writer.writerow(data)

while time1< starttime+10:
	time1=time.time()
	temp,gas, humidity,press,alt=bme680.temperature, bme680.gas, bme680.relative_humidity,bme680.pressure,bme680.altitude
	
	print("\nTime:{}".format(time1))
	print("Temperature: %0.1f c" % temp)
	print("Gas: %d ohm" % gas)
	print("Humidity: %0.1f %%" % humidity)
	print("Pressure: %0.3f hPa" % press)
	print("altitude = %0.2f meters" % alt)
	
	data=[time1,temp,gas, humidity,press,alt]
	with open('my_data.csv','a', newline='') as file:
		writer=csv.writer(file)
		writer.writerow(data)
	
	time.sleep(2)
	
	
	
	
