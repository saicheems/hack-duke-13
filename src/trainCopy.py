


from sklearn import svm

import csv
import serial
import shared
import sys

def main():
	
        print "Welcome to Dukesound, the best sign to spoken language device ever created"
	print "##########################################################################"
        print "__---------------------------------------_---|-------------\--------------"
        print "|-\-|---|-|-/-|==--==--|==|-|---|-|\--|-|-\--|---------\----\-------------"
	print "|-|-\---/-|=--|==--|_--|--|-\---/-|-\-|-|-|--|------|---|----|------------"
	print "|_/--\_/--|-\-|==---_|-|==|--\_/--|--\|-|_/-/=\--------/----/-------------"
        print "--------------------------------------------\=/------------/--------------"
        print "##########################################################################"

        # open db file and set up writer
	file = open('../data/db.csv', 'a')
	writer = csv.writer(file)

	# intialize serial read
	ser = shared.init()

	done = False

	while not done:

		# flush input initially
		#ser.flushInput()

		print "Reading from input..."
		# read input from serial
		list = shared.read(ser)[1]

		print list
	
		# read in label for training data and append to list
		label = raw_input('Enter a label: ')
		list.append(label)

		inp = raw_input("Do you want to train another set? y/n: ")
		done = not (inp == 'y')

		print "Adding new training data to database..."
		# write list into csv file
		writer.writerow(list)

	file.close()

if __name__ == "__main__":
	main()
