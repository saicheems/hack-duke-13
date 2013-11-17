from sklearn import svm

import csv
import serial
import shared
import sys

def main():
	file = open('../data/db.csv', 'rb')
	reader = csv.reader(file)

	ser = shared.init()

	data = []
	label = []
	label_map = []
	i = 0
	for row in reader:
		data.append(row[:-1])
		label.append(i)
		label_map.append(row[-1])
		i = i + 1

	clf = svm.SVC(kernel = 'linear')
	clf.fit(data, label)

	#ser.flushInput()

	while 1:
		# read input from serial
		list = shared.read(ser)

		#print list

		print label_map[int(clf.predict(list))]

	file.close()

if __name__ == "__main__":
	main()
