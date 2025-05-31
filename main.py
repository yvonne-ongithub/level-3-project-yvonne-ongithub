import csv
import datetime
import random
import math
import time
from codelib import *

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

wheel = ['' for j in range(26)] # Creates a list with 26 empty strings, indexed as 0..25

print(wheel) # Output: ['', '', '', '', '']

# initial letters of guess are NSTLR and E
initial_guess = ["N","S","T","L","R","E"]
vowels = ["A","E","I","O","U"]
		
music_play()
print("Ladies and gentlemen, the star of our show is . . .")  # Output - Display fun things on the screen 
print(". . . YOU!  ")
contestant = input("Your name, please: ")

tries = 0
display_rules = input("Would you like to see the rules (Yes or No)? ")
display_rules = display_rules[0].upper()

while display_rules == "N" :
	tries += 1 
	if tries <= 3  :
		print("Answer yes or no.") 
		display_rules = input("Would you like to see the rules (Yes or No)? ")
	
if tries >=3 or display_rules == "Y" :
	show_rules()  # Functions - screen displays
	
print("Ready for the final and bonus round", end="")	
dots = 0
while dots < 3: 
	dots +=1
	print(". ", end="")
	time.sleep(1)
	
print("The categories are: ")
print("1. Situation Comedies")
print("2. Top Places to Visit in America")
print("3. Fun activities for students at college")
print("4. Exit")

number = -1
in_filename = ""
time_to_exit =  False

while number < 1 or number > 4 :
	number = int(input("Enter a number for your choice--between 1 and 4, inclusive. "))
	
	if number == 4 : 
		print ("It's been fun! See you next time.")
		time_to_exit = True;
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
	print(puzzle_number + " is the index for " + data[puzzle_number])  ##### TAKE THIS OUT AFTER TESTING
	
	puzzle = data[puzzle_number]  	# Variable - Store user guesses 
	puzzle_len = len(puzzle)

	answer = ['' for j in range(puzzle_len+1)]     # initialize user guess
		
	generate_entries(wheel)  
	
	print("Now, spin the wheel: (a number between 1 and 24 tells us your prize)")
	prize_slot  = random.randrange(1,25) 
	
	prize = wheel[prize_slot]  # select the prize envelope from the bonus round wheel
	print("Ok, I have the envelope.  You can't see what it is.\nOur beautiful assistant, Vanna Github, will display the board for you.")
	
	# set up the board
    
	for char_answer, i in enumerate(puzzle):    	# Datacamp enumerator
		
		if puzzle[i] == " " :     # fill in the blanks in the puzzle
			answer[i] = puzzle[i]    
		else :
			answer[i] = "_"
	
	print_board(answer)
		
	print("We will fill in the most popular letters in your puzzle. They are: " +  initial_guess)

	for letter in initial_guess :
		locations = find_all_indexes(puzzle,letter)   # what are the indexes of the letter in puzzle?
		if locations.len > 0 :
			for i in locations :
				answer[i] = letter
			  
	print(answer)    ##### TAKE THIS OUT AFTER TESTING		  
			  
	used_letters = ["E","L","N","R","S","T"]

	print("You get to guess three consonants and a vowel.")
	guessletters = 0 
	guessarray = []
	while guessletters <  4 :
		new_guess = input("Guess a consonant that has not been used:  ")
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

	new_guess = input("Now, guess a vowel.")
	good_guess = False
	while not good_guess :
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
			guessarray += new_guess   # add vowel to list user letters


	for letter in guessarray :
		locations = find_all_indexes(puzzle,letter)   # what are the indexes of the letter in puzzle?
		if locations.len > 0 :
			used_letters += letter
			for i in locations :
				answer[i] = letter

	print("OK, here are your guesses: " + guessarray)

	print_board(answer)
		
	tries = 0
	solved = False
	while tries < 4 or not solved :     	#guess a letter that has not been used:
		new_guess = input("Guess a letter or guess the answer:  ")
		tries += 1
		if len(new_guess) == 1  # single letter
			if new_guess in used_letters :
				buzz()
				print("You used that one already.")
			elif new_guess in puzzle :
				dingding()
	
				locations = find_all_indexes(puzzle,new_guess) 
				if locations.len > 0 :
					used_letters += new_guess
					for i in locations :
						answer[i] = letter
					print_board(answer)
		elif new_guess == puzzle :  # this is a guess at the answer
			print("Your guess was " + new_guess + " and the puzzle was " + puzzle)
			solved = True
		else :
			print("No, keep guessing")
			
	if solved :
		dingding() 
		dingding() 
		dingding()
		print ("YAY! " + contestant + " You have solved the puzzle! You win the prize! The prize is ", end="")
		print(prize)
		print("You realize of course, that ", end="")
		# games that are primarily string handling are a little weak in the math department
		if isnumeric(prize) :
			salary = prize / tries
			print("a prize of " + prize " means you made $" + str(salary) + " per guess!!")
		elif prize ==  "vacation" :
			print("this vacation is a charming visit to Acapulco, worth $30,000!! ")
			salary = 30000 / tries
			print("That's $" + str(salary) + " per guess!!")
		elif "boat" in prize :
			print("this 6-passenger Tahoe sports boat is built to perform. Its POWERGLIDE® hull design and  7-inch GPS touch screen will bring a new dimension to all your waterskiing trips. This incredible speed boat is valued at $29,670.")
			salary = 29670 / tries
			print("That's $" + str(salary) + " per guess!!")
		else :
			print("this Dodge " + prize + " is worth $58,000!!")  
			salary = 58000/tries
			print("That's $" + str(salary) + " per guess!!")
	else :  # too many tries
		buzz()
		print(contestant + ", You LOST! You ran out of time. The answer was " + puzzle)
		print("Your prize would have been ", end="")
		print(prize)
		salary = prize = 0
		
	print("Now, let's have some fun with your money. ")
	mathfun(salary, tries)
	print(contestant + ", that's pretty good.")
else :  #  time to exit
	print("Thanks for playing! Goodbye, " + contestant + "!")
	
print("Goodnight, everybody!!")
	
	
	
print("play again?")