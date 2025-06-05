import csv
import datetime
import math
import random
import time
from codelib import *
from colors import *
from playsound3 import playsound

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

wheel = ['' for j in range(26)] # Creates a list with 26 empty strings, indexed as 0..25

# initial letters of guess are NSTLR and E
initial_guess = ["N","S","T","L","R","E"]
vowels = ["A","E","I","O","U"]
categories = ["Situation Comedies", "Top Places to Visit in America","Fun activities for students at college","Exit"]
		
music_play()
print("Ladies and gentlemen, the star of our show is . . .")  # Output - Display fun things on the screen 

print(CRED + ". . . YOU!  " + CEND) # from file that contains constant colors

contestant = input("Your name, please: ")

tries = 0
display_rules = input("Would you like to see the rules (Yes or No)? ")
display_rules = display_rules[0].upper()

while display_rules == "N" :
	tries += 1 
	if tries <= 3  :
		print("Answer yes or no.") 
		display_rules = input("Would you like to see the rules (Yes or No)? ")
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
	for k, category_name in enumerate(categories) : # Datacamp
		c_index = k+1
		if c_index == 4 :
			print(CRED, end="")
		print(str(c_index)+ ". " + category_name)
		if c_index == 4 :
			print(CEND)

	number = -1
	in_filename = ""
	time_to_exit =  False

	while number < 1 or number > 4 :
		number = int(input("Enter a number for your choice--between 1 and 4, inclusive. "))
		
		if number == 4 : 
			print ("It's been fun! See you next time.")
			time_to_exit = True
			play_again = False
		else :
			match number:
				case 1: 
					in_filename = "sitcoms.csv"
				case 2:
					in_filename = "places.csv"
				case 3:
					in_filename = "activities.csv"
					
	if not time_to_exit :
	# CSV Files - read in the choices for the puzzle category and store them the list named data
		# Read the CSV file
		with open(in_filename, mode='r') as infile: # Functions -  file handling
			reader = csv.reader(infile)
			data = list(reader)

	# 	Lists - store the choices for the puzzle categories
		header = data[0]
		choices = len(data)   # number of entries in the array
		puzzle_number = random.randrange(1,choices) # Functions -  random number generator
		
		puzzle = data[puzzle_number]  	# Variable - Store user guesses 
		puzzle = str(puzzle).upper()
		puzzle_len = len(puzzle)

		answer = ['' for j in range(puzzle_len+1)]     # initialize user guess
			
		wheel = generate_entries(wheel)  
		
		input("Now, spin the wheel by pressing enter: (a number between 1 and 24 tells us your prize)")
		prize_slot  = random.randrange(1,25) 
	
		prize = wheel[prize_slot]  # select the prize envelope from the bonus round wheel
	
		print("Ok, I have the envelope.  You can't see what it is.")
		print("The category you chose was "+ str(categories[number-1]))
		
		print("\nOur beautiful assistant, ", end="")
		print(CGREEN + "Vanna Github" + CEND + ", will display the board for you.")
		
		# set up the board
		# this piece was originally intended to be code learned from Datacamp,
		# but during development it was changed to code learned from w3schools
		temp_answer = str(puzzle)
		original = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		hidden = "__________________________"
		mytable = str.maketrans(original,hidden)
		answer = temp_answer.translate(mytable)
		
		print("The board is ...")
		print_board(answer)
			
		print("\nWe will fill in the most popular letters in your puzzle. \nThey are: " +  str(initial_guess))
		used_letters = ["E","L","N","R","S","T"]

		answer = update_answer(initial_guess,puzzle,used_letters,answer)
		print_board(answer)   	  
		
		print("You get to guess three consonants and a vowel.")
		guessletters = 0 
		guessarray = []
		while guessletters <  3 :
			new_guess = input("Guess a consonant that has not been used:  ")
			new_guess = str(new_guess).upper()
			if new_guess in used_letters :
				buzz()
				print("You used that one already.")	
			elif new_guess in guessarray  :
				buzz()
				print("You used that one already.")	
			elif  new_guess in vowels :
				print("Not yet - just consonants.")
			else :
				guessletters +=1
				guessarray += new_guess
		
		good_guess = False
		while not good_guess :
			new_guess = input("Now, guess a vowel:  ")
			new_guess = str(new_guess).upper()
			if new_guess in used_letters :
				buzz()
				print("You used that one already.")	
			elif new_guess in guessarray  :
				buzz()
				print("You used that one already.")	
			elif  new_guess not in vowels :
				print("It has to be a vowel.")
			else :
				good_guess = True
				guessarray += new_guess   # add vowel to list of user letters

		answer = update_answer(guessarray,puzzle,used_letters,answer)
	
		print("OK, here are your guesses: " + str(guessarray))
		
		print_board(answer)
		print("*** "+ str(puzzle))
		tries = 0
		solved = False
		while tries < 4 and not solved :     	#guess a letter that has not been used:
			new_guess = input("Guess a letter or guess the answer:  ")
			new_guess = new_guess.upper()
			tries += 1
			if len(new_guess) == 1  :  # single letter	
				print("single letter "+ new_guess)		
				if new_guess in used_letters :
					buzz()
					print("You used that one already.")
				elif new_guess in puzzle :
					print(new_guess + " in puzzle")		
					dingding()
					answer = update_answer(new_guess,puzzle,used_letters,answer)
					print_board(answer)
				else :
					print("No, that's not in the puzzle.")
					if new_guess not in used_letters :
						used_letters += new_guess
			elif new_guess == puzzle :   # this is a guess at the answer
				print("Your guess was " + str(new_guess) + " and the puzzle was " + str(puzzle))
				solved = True
			else :
				print("guess again")
				print("Your guess was " + str(new_guess) + " and the puzzle was " + str(puzzle))
				
				print("No, keep guessing")
		
		if solved :
			dingding() 
			dingding() 
			dingding()
			print ("YAY! " + contestant + " You have solved the puzzle! You win the prize! The prize is ", end="")
			str_prize =  str(prize)                         # prize started out being a part of a list. Now it is a string
			int_prize = int(str_prize)                      # prize ia also an integer now
			if str_prize.isnumeric() : 
				print(f"${int_prize:,.2f}") 
			else :
				print(str_prize)

			print("You realize of course, that ", end="")
			# games that are primarily string handling are a little weak in the math department
			if str_prize.isnumeric() :
				salary = int_prize / tries
				print("A prize of " + f"${int_prize:.2f} means you made " + f"${int(salary):.2f}  per guess!!")
			elif str_prize ==  "vacation" :
				print("this vacation is a charming visit to Acapulco, worth $30,000!! ")
				salary = 30000 / tries
				print("That's " +  f"${int(salary):.2f} per guess!!")
			elif "boat" in str_prize :
				print("this 6-passenger Tahoe sports boat is built to perform. Its POWERGLIDE® hull design and  7-inch GPS touch screen will bring a new dimension to all your waterskiing trips. This incredible speed boat is valued at $29,670.")
				salary = 29670 / tries
				print("That's " +  f"${int(salary):.2f} per guess!!")
			else :
				print("this Dodge " + str_prize + " is worth $58,000!!")  
				salary = 58000/tries
				print("That's $" +  f"${int(salary):,.2f} per guess!!")
		else :  # too many tries
			buzz()
			print(contestant + ", " + CBLINK  + " You LOST! " + CEND)
			print("You ran out of time. The answer was " + puzzle)
			print("Your prize would have been ", end="")
			print(CBLINK + CGREEN  + str_prize + CEND)
			salary = prize = 0
			
		print("Now, let's have some fun with your money. ")
		mathfun(salary, tries)
		print(contestant + ", that's pretty good.")
	else :  #  time to exit
		play_again = False
		print("Thanks for playing! Goodbye, " + contestant + "!")
	
print("Goodnight, everybody!!")
