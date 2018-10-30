import csv

# capture data from csv file
data = []
with open('DATA_FOOD_CALORIES.csv', mode='r') as csvfile:
	csv_reader = csv.reader(csvfile)
	for row in csv_reader:
		data.append(row)

#separate out meals
breakfast = []
lunch = []
dinner = []
for i in range (0, len(data)):
	if data[i][8] == 'y':
		breakfast.append(data[i])
	if data[i][9] == 'y':
		lunch.append(data[i])
	if data[i][10] == 'y':
		dinner.append(data[i])

for x in range(0, len(dinner)):
	if int(dinner[x][1]) < 50:
		print(dinner[x])
# find the caloric intake of the user
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

	# obtain user information
	age = input("What is your age in years? ")
	sex = input("what is your sex (m/f) ")
