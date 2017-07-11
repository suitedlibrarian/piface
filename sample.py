#!/usr/bin/env python
import time
import serial
import random
import binascii
import pickle

tty="/dev/ttyAMA0"
baud=57600

config = []

config.append("sys reset")

#change these to values given
config.append("mac set devaddr 260114C8")
config.append("mac set deveui 006117063BA98093")
config.append("mac set appeui 70B3D57EF0005B5B")
config.append("mac set appskey XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
config.append("mac set nwkskey XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")


config.append("mac join abp")

config.append("sys set pindig GPIO0 1")


def send(data, p):
	p.write(data+"\x0d\x0a")
	data.rstrip()
	print(data)
	time.sleep(0.1)
	rdata=p.readline()
	rdata=rdata[:-1]
	print (rdata)

p = serial.Serial(tty , baud)

time.sleep(1)

for c in config:
    send(c, p)

#replace this with the sensor data.
#order is light, red, green, blue, x,y,z, heading, temp, pressure
    
user_data =[898,166,147,135,-0.0025634765625,0.02557373046875,1.0029296875,137.28,28.2777963716,100794.557256]

data = binascii.hexlify(pickle.dumps(user_data)).upper()
print(data)

send("mac tx cnf 1 {}".format(data), p)

time.sleep(1)
rdata=p.readline()
rdata=rdata[:-1]
print (rdata)
time.sleep(5)
rdata=p.readline()
rdata=rdata[:-1]
print (rdata)

