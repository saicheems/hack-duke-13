from sklearn import svm

import csv
import serial
import shared
import sys

def main():
	# open db file and set up writer
	file = open('../data/db.csv', 'a')
	writer = csv.writer(file)

	# intialize serial read
	ser = shared.init()

	# flush input initially
	#ser.flushInput()

	print "Reading from input..."
	# read input from serial
	list = shared.read(ser)[1]

	print list
	
	# read in label for training data and append to list
	label = raw_input('Enter a label: ')
	list.append(label)

	print "Adding new training data to database..."
	# write list into csv file
	writer.writerow(list)

	file.close()

if __name__ == "__main__":
	main()
