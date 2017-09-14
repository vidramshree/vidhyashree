#!/usr/bin/python3
import random
print("hello! welcome to Rock Paper Scissors Programs!")
isWin = False
while isWin == False:
	print("")
	print("Press 1 for Rock.")
	print("Press 2 for Paper.")
	print("Press 3 for Scissors")
	UserInput =int(input("What would you like to play?"))
	computerInput = random.randint(1,3)

	if (UserInput == 1) and (computerInput == 1):
		isWin == False
		print("It's a draw; you both played the Rock!")

	if (UserInput == 2) and (computerInput == 1):
		isWin == True
		print("You win! The computer played Rocks!")

	if (UserInput == 3) and (computerInput == 2):
		isWin == True
		print("You lose! The computer played Rocks!")

	if (UserInput == 1) and (computerInput == 2):
		isWin == True
		print("You lose! The computer played paper!")

	if (UserInput == 2) and (computerInput == 2):
		isWin == False 
		print("It's a draw; the computer played Paper!")

	if (UserInput == 3) and (computerInput == 2):
		isWin == True
		print("You win! The computer played Paper!")

	if (UserInput == 1) and (computerInput == 3):
		isWin == True
		print("You win! The computer played scissors!")

	if (UserInput == 2) and (computerInput == 3):
		isWin == True 
		print("You lose! The computer played scissors!")

	if (UserInput == 3) and (computerInput == 3):
		isWin == False 
print("It's a draw! the computer played scissors!")


	

	