from sklearn import svm

import serial
import sys

DEVICE = '/dev/ttyACM0'

def list_from_string(input):
	"""Reads in a comma delmited string and returns a list."""
	output = map(int, input.split(','))
	return output

def read_from_serial(ser):
	input = ser.readline()
	# read input string from serial in here

	return input

def main():
	ser = serial.Serial(DEVICE, 9600)

	# read input from serial
	serial_input = read_from_serial(ser)
	# print comma delimited list from input string
	print list_from_string(serial_input)

	

if __name__ == "__main__":
	main()
