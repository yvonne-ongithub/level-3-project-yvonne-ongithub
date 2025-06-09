# Previous to running this program, you need to import a github module by using
#  the following line in the terminal:
#  pip install git+https://github.com/ChrisBuilds/terminaltexteffects.git
#  pip install emoji

import csv  
import emoji
import math
import random
import time 

from codelib import *

from colors import *
from datetime import datetime, timezone
from terminaltexteffects.effects.effect_spray import Spray



"""
The following is a list of topics that were covered in class, as described in Canvas.
It also describes how the topics were used in the program.

Input - Input the user's choice of categories and letters
Math -  Add special items to the list, like money based on length of puzzle.
Output - Display fun things on the screen to increase the feel of the game show experience
Variable - Store user guesses 
DataCamp - Python Logic, Control Flow and Filtering
Elif - Work through the user's puzzle guesses
For Loop - Fill in the blanks on the screen
Functions -  Random number generator, file handling, screen displays
If Else - Select consonants or select vowels
Lists - Store the choices for the puzzle categories
While - While the user has not completed guessing the puzzle answer and has not run out of guesses
CSV Files - Read in the choices for each puzzle category and store them in lists
"""


emoji_V = emoji.emojize(":grinning_face:")
emoji_bell = emoji.emojize(":bell:") # Emoji code for bell
emoji_buzzer = emoji.emojize(":ogre:") # there is no emoji code for buzzer
bell = "🛎️"  # another emoji bell
buzzer = "🚨"
spraytext = ""
randomchar = [" \n"]

for j in range(20) : # the text for the simple screen effect 
	spraytext += "WHEEL OF FORTUNE   "

wheel = ['' for j in range(26)] # Creates a list with 26 empty strings, indexed as 0..25

# initial letters of guess are NSTLR and E
initial_guess = ["N","S","T","L","R","E"]
vowels = ["A","E","I","O","U"]

#  for user guesses - puzzle can fill in punctuation
consos = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"] 
categories = ["Situation Comedies", "Top Places to Visit in America","Fun activities for students at college","Exit"]
		
music_play()

now = datetime.now(timezone.utc)
formatted_date = now.strftime("%Y-%m-%d")

print("Ladies and gentlemen, it's " + str(now.hour).zfill(2) + ":" + str(now.minute).zfill(2)  + " on " + str(formatted_date) + ", and it's time to play - ")
 
# call a function that I did not write that is not part of the usual Python libraries
effect = Spray(spraytext) 
with effect.terminal_output() as terminal:
    for frame in effect:
        terminal.print(frame)
print("And, the star of our show is . . .")  # Output - Display fun things on the screen 

print(CRED + ". . . YOU!  " + CEND) # from file that contains colors as constants

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

	number = -1      # Standard pre-loop initializations
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
			
		print("\nOk, I have the envelope.  You can't see what it is.")
		print("The category you chose was "+ str(categories[number-1]))
		
		print("\nOur beautiful assistant, ", end="")
		print(CGREEN + emoji_V + " Vanna Github " + emoji_V + CEND + ", will display the board for you.")
		
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

		guess_array = []
		guess_array = get_guesses(used_letters, vowels)

		answer = update_answer(guess_array,str_puzzle,used_letters,answer)
	
		print("OK, here are your guesses: " + str(guess_array))
		
		print_board(answer)
		
		tries = 0
		solved = False
		while tries < 5 and not solved :     	# The contestant has 5 tries to guess a letter that has not been used
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
					if answer == str_puzzle :
						solved = True
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
			emoji_lost = emoji.emojize(":disappointed_face:") # Emoji code 
			print(buzzer, emoji_lost , emoji_lost , emoji_lost, buzzer)
			print(contestant + ", " + CBLINK  + " You LOST! " + CEND)
			print(buzzer, emoji_buzzer , emoji_buzzer , emoji_buzzer, buzzer)
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