def print_board(answer):
    character_count = 0
    for letter in answer :
        print (letter + " ", end="")
		
	    if letter == " " :
	       character_count +=1
		   if character_count > 3 :
		      print()   # newline on screen
	return
			  
def buzz():
# dress this up with color and sound, if there is time
	print("BUZZZZZ!!!")
	return
	
def dingding():
# dress this up with color and sound, if there is time
	print("DING DING DING!!!")
	return
	
def music_play():
# dress this up with color and sound, if there is time
	i = 0;
	for j in range(3):
		while i <  4 :
		
			print("DEE, DIT DEE, DIT DEE DIT")
			i +=1
		print("DEEEE!!")
	return

def generate_entries(wheel) :
# prize money ranges from $40,000 to$100,000,in incrementsof$3000.  There is also a car, a boat, and a vacation to be given away.
	money = 40000
	increment = 3000
	val = 0
	
	wheelsize = len(wheel)
	for j in range(wheelsize):  # make sure the wheel is empty first.
		wheel = ""
		
	wheel_entry = random.randrange(1,wheelsize) # Functions -  random number generator
	while val < wheelsize+1  or money <= 100000 :    # 1..25
		if wheel[wheel_entry]=="" :
			val += 1
			wheel[wheel_entry] = money + (val-1)*increment
		wheel_entry = random.randrange(1,wheelsize) # Functions -  random number generator
 
	val = 1
	other_prizes = ["SUV", "vacation", "sportscar","speedboat"]
	op=0;
	
	while val <= wheelsize :
		if wheel{val} = "" :
			wheel[val] = other_prizes[op]
			op +=1
		val +=1
		
	print(wheel)   ##### TAKE THIS OUT AFTER TESTING
	return (wheel)

def show_rules():
	print("Here's how to play Wheel of Fortune.")
	print("blah blah blah")
	return
	
def mathfun(x,y):
# Exploration of built-in math functions
	s_root = math.sqrt(x)        # Returns the square root of x.
	x_pow = math.pow(x, y)       # Returns x raised to the power of y. 
	x_fmod = math.fmod(x, y)     # Returns the remainder of x/y. 
	x_gcd = math.gcd(x, y)       # Returns the greatest common divisor of x and y.
	
	print("Who says game show contestants don't need to do math?")
	next_text= input("Hit enter for a display of what your money can do!!")
	print("The square root of your money is not evil, it's "+ str(s_root))
	print("\nBetter than doubling your money, you can raise it to a power. ")
	print(str(salary) + " to the " + str(tries) + "th power is " + str(x_pow))
	print("\nInstead of folding it in half, you can divide your money by the number of tries.")
	print("Keeping the remainder and throwing away the rest gives you " + str(x_fmod))
	print("\nAnd, you can share it with friends and family by using the greatest common denominator!")
	print("The gcd between your money and the guesses it took to earn it is " + str(x_gcd))
	
	return

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
    while True:
        index = main_string.find(substring, start_index)
        if index == -1:
            break  # Substring not found, exit loop
        indexes.append(index)
        start_index = index + 1  # Move to the next position after the found substring
    return indexes
