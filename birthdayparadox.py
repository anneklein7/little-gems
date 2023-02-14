import datetime, random

# Return a list of number random date objects for bdays.
# The year is unimportant as long as all bdays have the same year
def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        startOfYear = datetime.date(2001, 1, 1)

        # Get a random day of the year
        randomNumberOfDays = datetime.timedelta(random.randint(0, 364))
        birthday = startOfYear = randomNumberOfDays
        birthdays.append(birthday)
    return birthdays

def getMatch(birthdays):

    # Return date object of a birthday occurring more than once 
    # in the bdays list
    
    if len(birthdays) == len(set(birthdays)):
        return None # All bdays are unique so return None

    # Compare each birthday to all the other birthdays:
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a + 1:]):
            if birthdayA == birthdayB:
                return birthdayA # Returns matching birthday

# Display intro
print('''The birthday paradox shows us that in a group of N people, the odds that two of them 
have matching birthdays is surprisingly large. This program does a Monte Carlo simulation
(that is, repeated random simulations) to explore this concept. 
(It's not actually a paradox, it's just a surprising result.)''')

# Set up a tuple of month names in order
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True: # Keep asking until user enters a valid amount
    print('How many birthdays shall I generate? Max. 100:')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # User has entered a valid amount
print()

# Generate and display bdays
print("Here are ", numBDays, ' birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Displays comma for each birthday after the first
        print(', ', end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText, end='')
print()
print()

# Are there two matching bdays?
match = getMatch(birthdays)

# Display results
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on ', dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulations
print('Generating ', numBDays, ' random birthdays 100,000 times...')
input('Press enter to begin...')

print('Let\'s run another 100,000 simulations.')
simMatch = 0 # How many simulations had matching birthdays in them?
for i in range(100000):
    # Report on the progress every 10,000 simulations:
    if i % 10000 == 0:
        print(i, ' simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

# Display simulation results
probability = round(simMatch / 100000 * 100, 2)
print('Out of 100,000 simulations of ', numBDays, ' people, there was a ')
print('matching birthday in that group ', simMatch, ' times. This means')
print(' that ', numBDays, ' people have a ', probability, '% chance of')
print(' having a matching birthday in their group.')