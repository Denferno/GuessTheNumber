#   Mijn guessthenumber game
import random
secret_number = random.randint(1, 20)
print("Guess The Number Game")
print("What is your name?")
name = input()
print("Hello " + name + "\nhere are the rules:")
print("You have 5 attempts")
print("The number is between 1 and 20\n")
def game():
    for attempts in range(1, 6):
        number = int(input("Choose a number between 1 and 20: "))
        if number >= 21 or number <= 0:
            print("Not possible, read the rules again")
            print("Rules:")
            print("You have 5 attempts in total")
            print("The number is between 1 and 20\n")
        elif number > secret_number:
            print("Incorrect, the number is too HIGH.")
        elif number < secret_number:
            print("Incorrect, the number is too LOW")
        if number == secret_number:
            break

    if number == secret_number:
        print("\nYou won " + str(name) + ",the correct number is " + str(secret_number))
        print("You used " + str(attempts) + " attempts")
    else:
        print("\nYou lost, you used all 5 of your attempts")
        print("The correct number was " + str(secret_number))
game()
