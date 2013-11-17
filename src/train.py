from sklearn import svm

import csv
import serial
import shared
import sys

def main():
	file = open('../data/db.csv', 'a')
	writer = csv.writer(file)

	ser = shared.init()

	ser.flushInput()

	print "Reading from input..."
	# read input from serial
	serial_input = shared.read_from_serial(ser)

	print serial_input

	# generate integer list from string
	list = shared.list_from_string(serial_input)
	
	# read in label for training data and append to list
	label = raw_input('Enter a label: ')
	list.append(label)

	print "Adding new training data to database..."
	# write list into csv file
	writer.writerow(list)

	file.close()

if __name__ == "__main__":
	main()
