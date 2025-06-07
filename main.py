import csv
import datetime
import math
import random
import time
from codelib import *
from colors import *

"""
Input - input the user's choice of categories and letters
Math -  add special items to the list, like money based on length of puzzle.
Output - Display fun things on the screen to increase the feel of the game show experience
Variable - Store user guesses 
DataCamp - Python Logic, Control Flow and Filtering
Elif - work through the user's puzzle guesses
For Loop - fill in the blanks on the screen
Functions -  random number generator, file handling, screen displays
If Else - select consonants or select vowels
Lists - store the choices for the puzzle categories
While - while the user has not completed guessing the puzzle answer and has not run out of guesses
CSV Files - read in the choices for each puzzle category and store them in lists
"""
bell = "\a"
print('\a')

wheel = ['' for j in range(26)] # Creates a list with 26 empty strings, indexed as 0..25

# initial letters of guess are NSTLR and E
initial_guess = ["N","S","T","L","R","E"]
vowels = ["A","E","I","O","U"]
categories = ["Situation Comedies", "Top Places to Visit in America","Fun activities for students at college","Exit"]
		
music_play()
print("Ladies and gentlemen, the star of our show is . . .")  # Output - Display fun things on the screen 
dingpy.ding()

print(CRED + ". . . YOU!  " + CEND) # from file that contains constant colors

contestant = ""
while len(contestant) < 1 :
	contestant = input("Your name, please: ")

tries = 0
display_rules = input("Would you like to see the rules (Yes or No)? ")
if len(display_rules) > 0 :
	display_rules = display_rules[0].upper()
	
	while display_rules not in "YN" and tries < 3 :
		tries += 1 
		if tries <= 3  :
			print("Answer yes or no.") 
			display_rules = input("Would you like to see the rules (Yes or No)? ")
			if len(display_rules) > 0 :
				display_rules = display_rules[0].upper()
	
if tries >= 3 or display_rules == "Y" :
	show_rules()  # Functions - screen displays
	
print("Ready for the final and bonus round", end="", flush=True)	
dots = 0
while dots < 3: 
	dots +=1
	print(". ", end="", flush=True)
	time.sleep(1)
	
play_again = True
while play_again :
	print("The categories are: ")
	for k, category_name in enumerate(categories) : # Datacamp discusses the enumerate function
		c_index = k+1
		if c_index == 4 :
			print(CRED, end="")
		print(str(c_index)+ ". " + category_name)
		if c_index == 4 :
			print(CEND)

	number = -1
	in_filename = ""
	time_to_exit =  False
	str_number = ""
	play_again = True

	while len(str_number) < 1 :
		str_number = input("Enter a number for your choice--between 1 and 4, inclusive. ")
		if len(str_number) > 0 :
			if str_number.isdigit() :  # only digits in the string makes it an integer
				number = int(str_number)
				if number == 4 : 
					print ("It's been fun! See you next time.")
					time_to_exit = True
					play_again = False
				elif number > 4 :   # erase bad answer
					str_number = ""
					print("Your choice should be between 1 and 4, inclusive.")
				else :
					match number:
						case 1: 
							in_filename = "sitcoms.csv"
						case 2:
							in_filename = "places.csv"
						case 3:
							in_filename = "activities.csv"
						case _:
							str_number = ""
							print("Your choice should be between 1 and 4, inclusive.")
			else : 
				str_number = ""
				print("Your choice should be a number between 1 and 4, inclusive.")

	if time_to_exit :   # shortest clause first.  This may differ from the standard of True clause first
		play_again = False
		print("Thanks for playing! Goodbye, " + contestant + "!")
	else : 
		choices = -1
		puzzle = ""
		puzzle = read_file(in_filename,choices,puzzle)
		puzzle = str(puzzle).upper()
		str_puzzle = "".join(puzzle)   # convert from list to string
		str_puzzle = str_puzzle[2:-2]  # remove squotes and brackets
	
		puzzle_len = len(str_puzzle)
		
		answer = ['' for j in range(puzzle_len+1)]     # initialize user guess
			
		wheel = generate_entries(wheel)  # populate the wheel with prize money
		
		input("Now, spin the wheel by pressing enter: (a number between 1 and 24 tells us your prize)")
		prize_slot  = random.randrange(1,25) 
	
		prize = wheel[prize_slot]  # select the prize envelope from the bonus round wheel
		
		str_prize = prize  # prizes can be integers or strings
		int_prize = 0
		if isinstance(str_prize, str):
			if str_prize.isdigit() :  # only digits in the string makes it an integer
				int_prize = prize
		else :
			int_prize = prize
			
		print(str_prize,' ', int_prize)

		print("\nOk, I have the envelope.  You can't see what it is.")
		print("The category you chose was "+ str(categories[number-1]))
		
		print("\nOur beautiful assistant, ", end="")
		print(CGREEN + "Vanna Github" + CEND + ", will display the board for you.")
		
		# set up the board
		# this piece was originally intended to be code learned from Datacamp,
		# but during development it was changed to code learned from w3schools
		temp_answer = str_puzzle
		original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"  # replace the original text with text that 
		hidden = "__________________________"    # hides the letters on the screen
		mytable = str.maketrans(original,hidden)
		answer = temp_answer.translate(mytable)
		
		print("The board is ...")
		print_board(answer)
			
		print("\nWe will fill in the most popular letters in your puzzle. \nThey are: " +  str(initial_guess))
		used_letters = ["E","L","N","R","S","T"]

		answer = update_answer(initial_guess,str_puzzle,used_letters,answer)
		print_board(answer)

		guessarray = []
		guessarray = get_guesses(used_letters, vowels)

		answer = update_answer(guessarray,str_puzzle,used_letters,answer)
	
		print("OK, here are your guesses: " + str(guessarray))
		
		print_board(answer)
		
		tries = 0
		solved = False
		while tries < 5 and not solved :     	# 5 tries to guess a letter that has not been used:
			new_guess = input("Guess a letter or guess the answer:  ")
			new_guess = new_guess.upper()
			tries += 1
			if len(new_guess) == 1  :  # single letter	
				if new_guess in used_letters :
					buzz()
					print("You used that one already.")
				elif new_guess in str_puzzle :
					dingding()
					answer = update_answer(new_guess,str_puzzle,used_letters,answer)
					print_board(answer)
				else :
					print("No, that's not in the puzzle.")
					if new_guess not in used_letters :
						used_letters += new_guess
			elif new_guess == str_puzzle :   # this is a guess at the answer
				print("Your guess was " + str(new_guess))
				solved = True
			else :
				print("guess again")
				print("Your guess was " + str(new_guess) )
		
		if solved :
			dingding() 
			dingding() 
			dingding()
			print ("YAY! " + contestant + " You have solved the puzzle! You win the prize!")
			print("The prize is ", end="")
			import dingpy

			dingpy.ding()
			if isinstance(str_prize, str):
				if str_prize.isdigit() :  # only digits in the string makes it an integer
					print(f"${int_prize}") 
				else :
					print("a",str_prize)
			else : # print integer
				print(f"${int_prize}") 

			print("You realize of course, that ", end="")
			int_prize = prize_description (str_prize,int_prize  ) 
		
			salary = int_prize/tries
			print("That's " +  f"${int(salary):,.2f} per guess!!")
		else :  # too many tries
			buzz()
			print(contestant + ", " + CBLINK  + " You LOST! " + CEND)
			print("You ran out of time. The answer was " + str_puzzle)
			print("Your prize would have been ", end="")
			print(CBLINK + CGREEN , end="")
			if isinstance(str_prize, str):
				if str_prize.isdigit() :  # only digits in the string makes it an integer
					print(f"${int_prize}" , end="") 
				else :
					print(str_prize , end="")
			else : # print integer
				print(f"${int_prize}" , end="") 
			print( CEND)

			salary = 0
			int_prize = 0
			
		print("Now, let's have some fun with your money.\n ")
		# games that are primarily string handling are a little weak in the math department
		
		mathfun(int_prize, tries)
		print(contestant + ", that's pretty good. ")
		input("Hit enter.")
		print("\nDo you want to play again?")

print("Goodnight, everybody!!")