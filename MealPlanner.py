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
# Carbohydrates and Protein are 4 calories per gram
dailyCarbs = dailyCalories * .45 / 4
dailyProtein = dailyCalories * .275 / 4

# Fat is 9 calories per gram
dailyFat = dailyCalories * .275 / 9


# always have meat and vegetables
# fruits, dairy, grains, and other may or may not be included



# function returns a random meat
def getMeat(meal):
	for i in range(0, len(meal)):
		meat = random.choice(meal)
		if meat[11]== 'meat':
			return meat

# function returns a random vegetable
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
# This function will call a getVarGroup to get a side category
# then it will search for a food of that category and return it
def getSide(meal):
	for i in range(0, len(meal)):
		side = random.choice(meal)
		if side[11] == getVarGroup():
			return side


# How while loops work throughout the program

	# while (calories * modifier) > # of calories
		# get a food item
		# subtract food calories from meal calories
		# subtract grams of protein from dailyProtein
		# subtract grams of carbs from dailyCarbs
		# subtract grams of fat from dailyFat
		# add a food to list of meal


# create a list of our breakfast foods
myBreakfast = []
breakfastCals = calsPerMeal

# first addition to breakfast is meat
# once 1/3 of daily protien is met, loop exits
meat = getMeat(breakfast)
while float(meat[2]) < float(dailyProtein) / 3 and breakfastCals > (dailyCalories * .275/ 3):
	breakfastCals -= int(meat[1])
	dailyProtein -= float(meat[2])
	dailyFat -= float(meat[7])
	dailyCarbs -= float(meat[3])
	myBreakfast.append(meat)
	meat = getMeat(breakfast)

# if breakfast calories are greater than 300, add a side
# do this before adding vegetables, because vegetables are low calorie
# each side is around 300 calories
while breakfastCals > 300:
	side = getSide(breakfast)
	dailyProtein -= float(side[2])
	dailyFat -= float(side[7])
	dailyCarbs -= float(side[3])
	breakfastCals -= int(side[1])
	myBreakfast.append(side)

# while breakfast calories have not been satisfied, add more veggies
# each vegetable is around 20 calories
while breakfastCals > 20:
	veg = getVeg(breakfast)
	breakfastCals -= int(veg[1])
	dailyProtein -= float(veg[2])
	dailyFat -= float(veg[7])
	dailyCarbs -= float(veg[3])
	myBreakfast.append(veg)

# create lunch list
myLunch = []

# var to store remaining calories for lunch
lunchCals = calsPerMeal

# one half of the dailyProtein var will give us 1/3 of daily protein in grams
# add meat until 1/3 of daily protein has been met and 1/3 of lunch calories has been met
meat = getMeat(lunch)
while float(meat[2]) < float(dailyProtein) / 2 and lunchCals > (dailyCalories * .275/ 3):
	lunchCals -= int(meat[1])
	dailyProtein -= float(meat[2])
	dailyFat -= float(meat[7])
	dailyCarbs -= float(meat[3])
	myLunch.append(meat)
	meat = getMeat(lunch)

while lunchCals > 300:
	side = getSide(lunch)
	lunchCals -= int(side[1])
	dailyProtein -= float(side[2])
	dailyFat -= float(side[7])
	dailyCarbs -= float(side[3])
	myLunch.append(side)

while lunchCals > 20:
	veg = getVeg(lunch)
	lunchCals -= int(veg[1])
	dailyProtein -= float(veg[2])
	dailyCarbs -= float(veg[3])
	dailyFat -= float(veg[7])
	myLunch.append(veg)

# create list for dinner
myDinner = []
dinnerCals = calsPerMeal

# the rest of the daily protein requirement needs to be met
# also 27.5 % of dinner calories should come from meat
meat = getMeat(dinner)
while float(meat[2]) < float(dailyProtein) - 50 and dinnerCals > (dailyCalories * .275/ 3):
	dinnerCals -= int(meat[1])
	dailyProtein -= float(meat[2])
	dailyFat -= float(meat[7])
	dailyCarbs -= float(meat[3])
	myDinner.append(meat)
	meat = getMeat(dinner)

# while over 300 calories remain in dinner, get a side
# each side is around 300 calories
while dinnerCals > 300:
	side = getSide(dinner)
	dinnerCals -= int(side[1])
	dailyProtein -= float(side[2])
	dailyCarbs -= float(side[3])
	dailyFat -= float(side[7])
	myDinner.append(side)

# once side-loop breaks, fill remaining calories with vegetables
# > 20 because each vegatable is around 20 calories, we don't want to go over
while dinnerCals > 20:
	veg = getVeg(dinner)
	dinnerCals -= int(veg[1])
	dailyProtein -= float(veg[2])
	dailyFat -= float(veg[7])
	dailyCarbs -= float(veg[3])
	myDinner.append(veg)



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

print('\ncarbs ' + str(dailyCarbs) + '\t protein ' + str(dailyProtein) + ' \tfat ' + str(dailyFat))


# add up calories of each meal
dailyCalories = dinnerCals + lunchCals + breakfastCals

# Ideally, remaining should be as close to zero as possible

# condition within print statement to show if calories are left or exceeded daily requirements
print(str(dailyCalories) + ' daily calories remaining' if dailyCalories > 0 else 'Exceeded daily calories by ' + str( -1 *dailyCalories) )
