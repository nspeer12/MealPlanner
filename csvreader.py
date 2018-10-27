import csv

def caloricIntake(sex, age):

	age = int(age)

	if sex == "m":
		if age >= 18 and age <= 25:
			return 2800
		if age > 25 and age <= 45:
			return 2600
		if age > 45 and age <= 65:
			return 2400
		if age > 65:
			return 2200

	elif sex == "f":
		if age >= 18 and age <= 25:
			return 2200
		if age > 25 and age <= 45:
			return 2000
		if age > 45 and age <= 65:
			return 1800
		if age > 65:
			return 1600







with open('data.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	# obtain user information
	age = input("What is your age in years? ")
	sex = input("what is your sex (m/f) ")

	print("Your suggested caloric intake is " + str(caloricIntake(sex, age)))

	#for line in csv_reader:
	#	if line[0] == choice:
	#		print(line[1] + " " + line[2])
