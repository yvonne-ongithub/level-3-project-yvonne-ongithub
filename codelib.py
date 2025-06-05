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
# dress this up with color and sound, if there is time
	print("BUZZZZZ!!!")
	return
	
def dingding():
	bell =  "\a"
# dress this up with color and sound
	print("DING DING DING!!!")
	print(bell + bell + bell)
	return
	
def music_play():
# dress this up with color and sound, if there is time
	bell =  "\a"
	i = 0
	for j in range(3):
		while i <  4 :
			print("DEE, DIT DEE, DIT DEE DIT")
			i +=1
		print(bell)
	return

def generate_entries(wheel) :
# prize money ranges from $40,000 to$100,000,in incrementsof$3000.  There is also a car, a boat, and a vacation to be given away.
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
	
	while val < wheelsize :  
		if wheel[val] == "" :
			wheel[val] = other_prizes[op]
			op +=1
		val +=1
		
	return (wheel)

def show_rules():
	print("Here's how to play Wheel of Fortune.")
	print("blah blah blah")
	return


def update_answer(guessarray,puzzle,used_letters,answer) :
	temp_answer = answer
	for letter in guessarray :
		locations = find_all_indexes(str(puzzle).upper(),letter)   # what are the indexes of the letter in puzzle?
		if len(locations) > 0 :
			if letter not in used_letters :
				used_letters += letter
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
	
	print(x + " Is how much you won, and " + y + " is how many tries it took to win.")
	
	print("Who says game show contestants don't need to do math?")
	next_text = input("Hit enter for a display of what your money can do!!")
	print("The square root of your money is not evil, it's "+ str(s_root))
	print("\nBetter than doubling your money, you can raise it to a power. ")
	print(str(x) + " to the " + str(y) + "th power is " + str(x_pow))
	print("\nInstead of folding it in half, you can divide your money by the number of tries.")
	print("Keeping the remainder and throwing away the rest gives you " + str(x_fmod))
	print("\nAnd, you can share it with friends and family by using the greatest common denominator!")
	print("The gcd between your money and the guesses it took to earn it is " + str(x_gcd))
	
	return

def replace_char_list(text, index, replacement):
    list_text = list(text)
    list_text[index] = replacement
    return "".join(list_text)

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
			searching = False  # Substring not found, exit loop
		else :
			indexes.append(index)
			start_index = index + 1  # Move to the next position after the found substring
	return indexes
