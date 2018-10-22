import csv

with open('data.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	for line in csv_reader:
		if(line[3] == "7272518704"):
			print("I found " + line[1] + " " + line[0] + "'s phone number which is " + line[3])
