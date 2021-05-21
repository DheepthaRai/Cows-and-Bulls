import random

# Gets the no. of digits of a number
def getDigits(num):
    return [int(i) for i in str(num)]


# Checks for duplicates in a number
def noDuplicates(num):
    num_ln = getDigits(num)
    if len(num_ln) == len(set(num_ln)):
        return True
    else:
        return False


# Generates a 4 digit number
def generateNum():
    while True:
        num = random.randint(1000, 9999)
        if noDuplicates(num):
            return num


# Returns bulls and cows (if any)
def numOfBullsCows(num, guess):
    bulls_cows = [0, 0]
    num_ln = getDigits(num)
    guess_ln = getDigits(guess)

    for i, j in zip(num_ln, guess_ln):

        # common digit present
        if j in num_ln:

            # exact match
            if j == i:
                bulls_cows[0] += 1

            # wrong position
            else:
                bulls_cows[1] += 1

    return bulls_cows


# Our Number
num = generateNum()

tries = int(input('Enter number of tries: '))

# The game rules
while tries > 0:
    guess = int(input("Enter your guess: "))

    if not noDuplicates(guess):
        print("XXX  Enter unique digit numbers only! Try again !!!")
        continue
    if guess < 1000 or guess > 9999:
        print("XXX  Enter 4 digit number only! Try again !!!")
        continue

    bulls_cows = numOfBullsCows(num, guess)
    print(f"{bulls_cows[0]} bulls, {bulls_cows[1]} cows")
    tries -= 1

    if bulls_cows[0] == 4:
        print("Woohoo! You guessed right! Yayyy!")
        break
else:
    print(f"Sorry, you ran out of tries ://  \nThe number was {num}")
