
import csv


def getDegreesAndCount():

	degrees = []	
	with open('degree.csv') as csvfile:
		spamreader = csv.reader(csvfile)

		for row in spamreader:
			print row
			tmp_list = []
			tmp_list = row[0].split(",")
			if len(tmp_list) > 0:
				for item in tmp_list:
					degrees.append(item)
			else:
				degrees.append(row[0])
	print degrees

	return degrees

degrees_returned = getDegreesAndCount()

# get all unique elements from the degrees_returned list and return a list
for d in degrees_returned:
	if d not in degrees_returned:
		degrees_returned.append(d)
		print degrees_returned



# create a function, that counts the uniques entries in the degrees_returned list using the list that was returned form the previous function
