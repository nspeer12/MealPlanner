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
sex = raw_input("what is your sex (m/f) ")

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
while float(meat[2]) < float(dailyProtein) / 3 and breakfastCals > dailyCalories * .45 / 3 : # this expression keeps breakfast cals in range
	breakfastCals -= int(meat[1])
	dailyProtein -= float(meat[2])
	myBreakfast.append(meat)
	meat = getMeat(breakfast)


veg = getVeg(breakfast)
while int(veg[1]) < breakfastCals * .10 / 3:
	breakfastCals -= int(veg[1])
	myBreakfast.append(veg)
	veg = getVeg(breakfast)

# need to tweak margins
while breakfastCals > 100:
	side = getSide(breakfast)
	breakfastCals -= int(side[1])
	myBreakfast.append(side)

myLunch = []
lunchCals = calsPerMeal

meat = getMeat(lunch)
while float(meat[2]) < float(dailyProtein) / 2 and lunchCals > dailyCalories * .45 / 3 :
	lunchCals -= int(meat[1])
	dailyProtein -= float(meat[2])
	myLunch.append(meat)
	meat = getMeat(lunch)

veg = getVeg(lunch)
while int(veg[1]) < lunchCals - 300:
	lunchCals -= int(veg[1])
	myLunch.append(veg)
	veg = getVeg(lunch)

while lunchCals > 100:
	side = getSide(lunch)
	lunchCals -= int(side[1])
	myLunch.append(side)


myDinner = []
dinnerCals = calsPerMeal

meat = getMeat(dinner)
while float(meat[2]) < float(dailyProtein) and dinnerCals > dailyCalories * .275 / 3:
	dinnerCals -= int(meat[1])
	dailyProtein -= float(meat[2])
	myDinner.append(meat)
	meat = getMeat(dinner)

veg = getVeg(dinner)
while int(veg[1]) < dinnerCals - 300:
	dinnerCals -= int(veg[1])
	myDinner.append(veg)
	veg = getVeg(dinner)

while dinnerCals > 100:
	side = getSide(dinner)
	dinnerCals -= int(side[1])
	myDinner.append(side)


def printMeals(breakfast, lunch, dinner):
	print('\n\t\tFood\t\t\tCalories\tProtein(g)\tCarbohydrates(g)\tFat(g)')
	
	print('Breakfast')
	for food in breakfast:
		print('\t\t' + '{:<20}'.format(food[0]) + '\t' + food[1] + '\t\t' + food[2] + '\t\t' + food[3] + '\t\t\t' + food[7])
	
	print('Lunch')
	for food in lunch:
		print('\t\t' + '{:<20}'.format(food[0]) + '\t' + food[1] + '\t\t' + food[2] + '\t\t' + food[3] + '\t\t\t' + food[7])

	print('Dinner')	
	for food in dinner:
		print('\t\t' + '{:<20}'.format(food[0]) + '\t' + food[1] + '\t\t' + food[2] + '\t\t' + food[3] + '\t\t\t' + food[7])


printMeals(myBreakfast, myLunch, myDinner)


# should be as close to zero as possible
print(dinnerCals + lunchCals + breakfastCals)
