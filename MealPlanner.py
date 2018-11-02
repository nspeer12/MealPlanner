import csv
import random

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


#for x in range(0, len(dinner)):
#	if int(dinner[x][1]) < 50:
#		print(dinner[x])

# obtain user information
age = input("What is your age in years? ")
sex = input("what is your sex (m/f) ")

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

dailyCalories = caloricIntake(sex,age)
calsPerMeal = dailyCalories / 3

# 47 - carbs
# 27.5 - Protein
# 27.5 - Fat
dailyCarbs = dailyCalories * .475 / 4
dailyProtein = dailyCalories * .275 / 4
dailyFat = dailyCalories * .275 / 9




# always have meat and vegetables
# fruits, dairy, grains, and other may or may not be included
myBreakfast = []
breakfastCals = calsPerMeal
print(breakfastCals)

def getMeat(meal):
	for i in range(0, len(meal)):
		meat = random.choice(meal)
		if meat[11]== 'meat':
			return meat

def getVeg(meal):
	for i in range(0, len(meal)):
		veg = random.choice(meal)
		if veg[11]== 'vegetable':
			return veg

# select a random group for our third
# these statements are to find the string name of the group

def getVarGroup():
	variableGroup = random.randint(0,3)

	if(variableGroup == 0):
		variableGroup = 'fruit'
	if(variableGroup == 1):
		variableGroup = 'dairy'
	if(variableGroup == 2):
		variableGroup = 'grain'
	if(variableGroup == 3):
		variableGroup = 'other'

	return variableGroup


# This group is going to be called 'side'
# we want this group to satisfy the remaining breakfast cals
def getSide(meal):
	for i in range(0, len(meal)):
		side = random.choice(meal)
		if side[11] == getVarGroup():
			return side

meat = getMeat(breakfast)
if int(meat[1]) < breakfastCals:
	breakfastCals -= int(meat[1])
	myBreakfast.append(meat)

veg = getVeg(breakfast)
if int(veg[1]) < breakfastCals:
	breakfastCals -= int(veg[1])
	myBreakfast.append(veg)

while breakfastCals > 100:
	side = getSide(breakfast)
	breakfastCals -= int(side[1])
	myBreakfast.append(side)


print(breakfastCals)
print(myBreakfast)
