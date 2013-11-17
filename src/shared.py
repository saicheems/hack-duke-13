from sklearn import svm

import csv
import serial
import sys

DEVICE = '/dev/ttyACM0'
NUM_VAR = 10

def init():
	ser = serial.Serial(DEVICE, 9600)
	return ser

def list_from_string(input):
	"""Reads in a comma delmited string and returns a list."""

	# if we get a parsing error, return an empty array
	try:
		output = map(int, input.split(','))
	except:
		return []
	return output

def read_from_serial(ser):
	"""Reads a string from serial in"""
	input = ser.readline()
	# read input string from serial in here
	return input

def read_combined(ser):
	"""Combines the above two methods - gets the string from serial and outputs the integer list."""
	line = read_from_serial(ser)
	list = list_from_string(line)
	return list

def read(ser):
	"""Uses read_combined to get the integer list and runs error checking until a valid list is found."""
	# flush before read
	ser.flushInput()
	list = [-1]
	sum = 0

	# list[-2] is hash, list[-1] is push button
	while len(list) != NUM_VAR or sum != list[-2]:
		list = read_combined(ser)
		sum = 0
		for x in list[:-2]:
			sum = sum + x

	list = [x * 10 for x in list]

	return [list[-1], list[:-2]]
