import random
print("Hello what is your name")
name = input()
secretNumber = random.randint(1,20)
print ("Well " + name + ": im thinking of a number between 1 and 20")

print("DEBUG: SECRET NUMBER IS " +str(secretNumber))

# In range , starting at 1 and going up to 7 , in order for our guesseTaken to be accurate
for guessesTaken in range(1,7):
    print("Take a guess")
    guess = int(input())
    if guess < secretNumber:
        print("Guess is too low")
    elif guess > secretNumber:
        print("your guess is too high")
    else:

        #If correctly guessed, we just break the loop and run the rest of program, loop will end because they took 6 guesses or because they got the answer correct
        break

#str converts string value of number to string on order to concatinate it
if guess == secretNumber:
    print("Yay you guessed right " + name + " it was : " + str(guess) + " it took you " + str(guessesTaken) + " tries")
else:
    print("No thats not the number i was thinking of, i was thinking: " + str(secretNumber))
