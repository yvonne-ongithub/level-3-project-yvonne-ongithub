# Yvonne Richardson
# STEM 103
# Level 3: Final Project
#
# Wheel of Fortune, the Final Round

import csv
import emoji
import random
import math

from colors import *

def print_board(answer):
	answer = answer
	if len(answer) <=  0 :
		print("something wrong with answer in print_board")
	print(CGREENBG +CWHITE, end="")
	character_count = 0
	for letter in answer :
		print (letter + " ", end="")
		if letter == " " :
			character_count +=1
			if character_count > 2 :
				print()   # newline on screen
	print(CEND)
	return
			  
def buzz():
# contestant made a mistake, so this is the negative response 
	emoji_buzzer = emoji.emojize(":ogre:") # there is no emoji code for buzzer
	print(emoji_buzzer)
	print("BUZZZZZ!!!")
	return
	
def dingding():
	# This is dressed up with color and emojis, but sound is not available
	# through the standard Github Python setups.

	emoji_bell = emoji.emojize(":bell:") # Emoji code for bell
	print("DING DING DING!!!")
	print(emoji_bell + emoji_bell + emoji_bell)
	return
	
def music_play():
# emoji music characters are somewhat sparse. Large colored circles are a good substitute

	emoji_dee =  emoji.emojize(":green_circle:")
	emoji_deedee = emoji.emojize(":musical_note:")
	emoji_dit = emoji.emojize(":blue_circle:")
	emoji_deeee = emoji.emojize(":musical_notes:")
	emoji_trumpet = emoji.emojize(":trumpet:")
	emoji_saxophone = emoji.emojize(":saxophone:")

	for j in range(3):
		i = 0
		print(emoji_trumpet,end="")
		while i <  3 :
			# Play the Wheel of Fortune Song
			print(emoji_dee, emoji_dit, emoji_dee, emoji_dit,emoji_deedee,"    ",end="")
			i +=1
		print(emoji_deeee,emoji_saxophone)
	return

def generate_entries(wheel) :
# prize money ranges from $40,000 to $100,000,in increments of $3000.  
# There is also a boat, 2 cars, and a vacation to be given away.
	money = 40000
	increment = 3000
	val = 0
	
	wheelsize = len(wheel) # make sure the wheel is empty first.
	wheel = ['' for j in range(wheelsize)] # Creates a list with empty strings
	
	wheel_entry = random.randrange(1,wheelsize) # Functions -  random number generator
	
	amount = 0
	wheel_full = False
	while not wheel_full :    # 1..25
		if wheel[wheel_entry] == "" :
			val += 1
			amount = money + (val-1)*increment
			wheel[wheel_entry] = amount
			if amount >= 100000 : 
				wheel_full = True
		wheel_entry = random.randrange(1,wheelsize) # Functions -  random number generator
 
	val = 1
	other_prizes = ["SUV", "vacation", "sportscar","speedboat"]
	op = 0;
	
	while val < wheelsize :  # locate empty places in wheel for non-monetary prizes
		if wheel[val] == "" :
			wheel[val] = other_prizes[op]
			op +=1
		val +=1
		
	return (wheel)

def show_rules():
	print(CVIOLET + "Here's how to play Wheel of Fortune." + CEND )
	print(CBLUE)
	print("You can select your puzzle category from three (3) possible category options \n" 
	"that are disclosed at the beginning of the Bonus Round. You cannot change your choice "
	"\nonce made. ")
	print("\nThere are 24 wedges on the 'Bonus Wheel' - each wedge has its own envelope.\n")
	print("The value of the bonus wheel envelopes ranges from $40000 to $100000, and there")
	print("are non-cash prizes as well. You will spin the 'Bonus Wheel' and we will remove the")
	print("envelope which corresponds to the wedge on which the Bonus Wheel landed.\n")
	print("The category of the puzzle will be revealed and you will be shown the R, S, T, L, N and Es")
	print("in the puzzle, after which you will be instructed to choose three additional ")
	print("consonants and one additional vowel. (Note: If an 'E' is revealed initially, there ")
	print("may or may not be any additional vowels. However, we will not indicate one way or ")
	print("another and will still ask for an additional vowel.\n") 
	print("You will have 5 tries to solve the puzzle. You may give more than one answer. You ")
	print("can still type letters, or you can give the answer in its entirety without any ")
	print("additional words between the correct order of the words in the solution.\n ")
	print("Whether you solve the bonus puzzle or not, I will open the envelope to reveal ")
	print("what prize you played for in the round.\n")
	print("Then we will mathematically explore the amounts of money that are associated with ")
	print("your prize.")
	input("\nHit enter and we will start the game.  ")
	print(CEND)
	return

def update_answer(guess_array,puzzle,used_letters,answer) :
	# Update the lists with new letters, previous to populating the board
	temp_answer = answer
	for letter in guess_array :
		locations = find_all_indexes(puzzle,letter)   # what are the indexes of the letter in puzzle?
		if len(locations) > 0 :  # letter found in puzzle
			if letter not in used_letters :
				used_letters += letter   # add the letter to the list of letters that have been used
			for i in locations :
				temp_answer = replace_char_list(answer, i, letter)
				answer = temp_answer
				
	return	temp_answer
				
def mathfun(x,y):
# Exploration of built-in math functions
	x = int(x)
	y = int(y)

	s_root = math.sqrt(x)        # Returns the square root of x.
	x_pow = math.pow(x, y)       # Returns x raised to the power of y. 
	x_fmod = math.fmod(x, y)     # Returns the remainder of x/y. 
	x_gcd = math.gcd(x, y)       # Returns the greatest common divisor of x and y.
	
	print(f"${x}" , end="")
	print(" is how much you won, and " + str(y) + " is how many tries it took to win.\n")
	
	print("Who says game show contestants don't need to do math?")
	next_text = input("Hit enter for a display of what your money can do!!")
	print("The square root of your money is not evil, it's "+ str(s_root))
	print("\nBetter than doubling your money, you can raise it to a power. ")
	print(str(x) + " to the " + str(y) + "th power is " + str(x_pow))
	print("\nInstead of folding it in half, you can divide your money by the number of tries.")
	print("Keeping the remainder and throwing away the rest gives you " + str(x_fmod))
	input("Discouraged? NO! Keep going! Hit enter. ")
	print("\nAnd, you can share your prize with friends and family by using the greatest common denominator!")
	print("The GCD is the largest positive integer that divides two or more integers without leaving a remainder.")
	print("The greatest common denominator between your money and the guesses it took to earn it is " + str(x_gcd) + "\n")
	
	return

def replace_char_list(text, index, replacement):
	# updates the puzzle board with the letters that were correctly guessed
	# convert the information from a string to a list and back again
    list_text = list(text)
    list_text[index] = replacement
    return "".join(list_text)

def read_file(in_filename,choices,puzzle) :
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
	return puzzle	
	
def get_guesses(used_letters,vowels) :
	#  for user guesses - puzzle can fill in punctuation
	consos = ["B","C","D","F","G","H","J","K","L","M","N","P","Q","R","S","T","V","W","X","Y","Z"] 

	print("You get to guess three consonants and a vowel.")
	guessletters = 0 
	guess_array = []
	while guessletters <  3 :
		new_guess = input("Guess a consonant that has not been used:  ")
		new_guess = str(new_guess).upper()
		if new_guess in used_letters :
			buzz()
			print("You used that one already.")	
		elif new_guess in guess_array  :
			buzz()
			print("You used that one already.")	
		elif  new_guess in vowels :
			print("Not yet - just consonants.")
		elif new_guess in consos :
			guessletters +=1
			guess_array += new_guess
		else :
			buzz()
			print("That is not a consonant.")	
	
	good_guess = False
	while not good_guess :
		new_guess = input("Now, guess a vowel:  ")
		new_guess = str(new_guess).upper()
		if new_guess in used_letters :
			buzz()
			print("You used that one already.")	
		elif new_guess in guess_array  :
			buzz()
			print("You used that one already.")	
		elif  new_guess not in vowels :
			print("It has to be a vowel.")
		else :
			good_guess = True
			guess_array += new_guess   # add vowel to list of user letters
	return guess_array

def prize_description (str_prize, int_prize  ) :
	# print description on screen of prizes that are not monetary
	if isinstance(str_prize, str):
		if str_prize ==  "vacation" :
			print("this vacation is a charming visit to Acapulco, worth $30,000!! ")
			int_prize = 30000
		elif str_prize ==  "SUV" :
			print("this Ford Sports Utility Vehicle is worth $60,000!! ")
			int_prize = 60000
		elif "boat" in str_prize :
			print("this 6-passenger Tahoe sports boat is built to perform. Its POWERGLIDE® hull design and  7-inch GPS touch screen will bring a new dimension to all your waterskiing trips. This incredible speed boat is valued at $29,670.")
			int_prize=29760
		else :
			print("this Dodge " + str_prize + " is worth $58,000!!") 
			int_prize=58000
	else : 
		int_prize = int_prize
	return int_prize

def find_all_indexes(main_string, substring):
	"""
    Finds all starting indexes of a substring within a main string.

    Args:
        main_string: The string to search within.
        substring: The string to search for.

    Returns:
        A list of integers, representing the starting indexes of all occurrences of the substring in the main string. 
        Returns an empty list if the substring is not found.
	"""
	indexes = []
	start_index = 0
	
	searching = True
	while searching:
		index = main_string.find(substring, start_index)
		if index == -1:
			searching = False  # Substring not found
		else :
			indexes.append(index)
			start_index = index + 1  # Move to the next position after the found substring
	return indexes