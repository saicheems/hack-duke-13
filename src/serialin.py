"""Test reading in data from serial in"""
import serial
ser = serial.Serial('/dev/ttyACM0', 9600)

while 1 :
	ser.readline()

