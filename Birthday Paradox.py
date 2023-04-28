"""Birthday Paradox Simulation, by Al Sweigart al@inventwithpython.com
Explore the surprising probabilities of the "Birthday Paradox".
More info at https://en.wikipedia.org/wiki/Birthday_problem
View this code at https://nostarch.com/big-book-small-python-projects
Tags: short, math, simulation"""

import datetime, random

def getBirthdays(numberOfBirthdays):
    #returns a list of number rnadom data objects for birthdays
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear= datetime.date(2023,1,1)
        
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays


def getMatch(birthdays):
    #returns the date object of a birthdaythat occurs more than once in the birthday list.
    if len(birthdays) == len(set(birthdays)):
        return None #all birthdays are unique so return none.
    
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1 :]):
            if birthdayA == birthdayB:
                return birthdayA #return matching birthday
            
            
print('''Birthday Paradox, by Al Sweigart al@inventwithpython.com
The Birthday Paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.
(It's not actually a paradox, it's just a surprising result.)
''')

#set up a tuple of mon names in order

MONTHS = ('Jan', 'Feb', 'Mar', 'Apr','May','Jun',
          'Jul', 'Aug','Sep', 'Oct','Nov', 'Dec')
while True:
    print("How many birthdays shall I generate (Max 100)")
    response = input('> ')
    if response.isdecimal() and ( 0 < int(response) <= 100):
        numBDays = int(response)
        break
print()

#Generate and display the birthdays:
print(f"Here are {numBDays} brithdays")
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #display a comma for each birthdya after the first birthday
        print(', ', end='')
        monthName = MONTHS[birthday.month - 1]
        dateText = '{}{}'.format(monthName, birthday.day)
        print(dateText, end='')
print()
print()
match = getMatch(birthdays)

print("In this simulation, ", end="")
if match != None:
    monthName= MONTHS[match.month -1]
    dateText = "{}{}".format(monthName, match.day)
    print(f"multiple people have a birthday on, {dateText}")
else:
    print("There are no matching birthdays")
print()

#run throught 100,000 simulations
print(f"Generating {numBDays} random birthdays 100,000 times")
input("Press enter to begin...")

print('let\'s run another 100,000 simulations')
simMatch = 0 #how many birthdyas had matching birthdyas in them.
for i in range (100_000):
    #report progress ever 10,000 simulations
    if i % 10_000 == 0:
        print(i, 'simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print("100,000 simulations run. ")

#display simulation results:
probability = round(simMatch/ 100_000 * 100, 2)
print(f"out of 100,000 sumulations of {numBDays} people, there was a")
print(f"matching birthday in that group {simMatch} times. This means.")
print(f"that, {numBDays} people have a {probability} % chance of")
print(f"having a matching birthday in their group")
print("That's probably more than you would think")
