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
		return 1







with open('data.csv', 'r') as csv_file:
	csv_reader = csv.reader(csv_file)

	#meals[3] # breakfast lunch and dinner
	age = input("What is your age in years? ")
	#height = input("What is your height in cm ")
	sex = input("what is your sex (m/f) ")
	#Men	BMR = 66.4730 + (13.7516 x weight in kg) + (5.0033 x height in cm) – (6.7550 x age in years)
	#Women BMR = 655.0955 + (9.5634 x weight in kg) + (1.8496 x height in cm) – (4.6756 x age in years)

	#if sex == "m":
	#	bmr = 66.473 + (13.7516 * float(weight)) + (5.0033 * float(height)) - (6.755 * float(age))
	#elif sex == "f":
	#	bmr = 655.0955 + (9.5634 * weight) + (1.8496 * height) - (4.6756 * age)
	print("Your suggested caloric intake is " + str(caloricIntake(sex, age)))

	#for line in csv_reader:
	#	if line[0] == choice:
	#		print(line[1] + " " + line[2])
