from sklearn import svm

import csv
import serial
import sys

DEVICE = '/dev/ttyACM0'

def init():
	ser = serial.Serial(DEVICE, 9600)
	return ser

def list_from_string(input):
	"""Reads in a comma delmited string and returns a list."""
	output = map(int, input.split(','))
	return output

def read_from_serial(ser):
	"""Reads a string from serial in"""
	input = ser.readline()
	# read input string from serial in here
	return input

def read_combined(ser) {
	line = read_from_serial(ser)
	list = list_from_string(line)
	return list
}

def read(ser) {
	list = [-1]
	sum = 0

	while len(list) != 6 and sum != list[-1]:
		list = read_combined(ser)
		for x in list[:-1]:
			sum = sum + x
	return list[:-1]
}
