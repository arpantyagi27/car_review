#Write a Python program to guess a number between 1 to 9. Note : User is prompted to enter a guess. If the user guesses wrong then the prompt
#appears again until the guess is correct, on successful guess, user will get a &quot;Well guessed!&quot; message, and the program will exit.
import random
rao=random.randint(1,9)
def reinput():
    userinput=int(input("Enter a guess: "))
    if(rao==userinput):
        print("Well Guessed")
    else:
        reinput()
reinput()
