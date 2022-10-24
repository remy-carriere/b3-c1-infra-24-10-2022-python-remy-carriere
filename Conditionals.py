#Q2
# Assign True or False as appropriate on the lines below!

# Set this to True if 17 < 328 or to False if it is not.
bool_one = 17<328   # We did this one for you!

# Set this to True if 100 == (2 * 50) or to False otherwise.
bool_two = 100==(2*50)

# Set this to True if 19 <= 19 or to False if it is not.
bool_three = 19 <= 19

# Set this to True if -22 >= -18 or to False if it is not.
bool_four = -22 >= -18

# Set this to True if 99 != (98 + 1) or to False otherwise.
bool_five = 99 != (98 + 1)


#Q3
# Assign True or False as appropriate on the lines below!

# (20 - 10) > 15
bool_one = (20 - 10) > 15    # We did this one for you!

# (10 + 17) == 3**16
# Remember that ** can be read as 'to the power of'. 3**16 is about 43 million.
bool_two = (10 + 17) == 3**16

# 1**2 <= -1
bool_three = 1**2 <= -1

# 40 * 4 >= -4
bool_four = 40 * 4 >= -4

# 100 != 10**2
bool_five = 100 != 10**2


#Q4
# Create comparative statements as appropriate on the lines below!

# Make me true!
bool_one = 3 < 5  # We already did this one for you!

# Make me false!
bool_two = 5==3

# Make me true!
bool_three = 5!=3

# Make me false!
bool_four = 5==3

# Make me true!
bool_five = 3!=5


#Q5
bool_one = False and False

bool_two = -(-(-(-2))) == -2 and 4 >= 16 ** 0.5

bool_three = 19 % 4 != 300 / 10 / 10 and False

bool_four = -(1 ** 2) < 2 ** 0 and 10 % 10 <= 20 - 10 * 2

bool_five = True and True


#Q6
bool_one = 2 ** 3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or False

bool_three = 100 ** 0.5 >= 50 or False

bool_four = True or True

bool_five = 1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1


#Q7
bool_one = 2 ** 3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or False

bool_three = 100 ** 0.5 >= 50 or False

bool_four = True or True

bool_five = 1 ** 100 == 100 ** 1 or 3 * 2 * 1 != 3 + 2 + 1


#Q8
bool_one = not True

bool_two = not 3 ** 4 < 4 ** 3

bool_three = not 10 % 3 <= 10 % 2

bool_four = not 3 ** 2 + 4 ** 2 != 5 ** 2

bool_five = not not False

#Q9
bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)


#Q10
# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = True or True

# Make me false!
bool_three = True and False

# Make me true!
bool_four = True and True

# Make me true!
bool_five = not False

#Q11
response = 'Y'

answer = "Left"
if answer == "Left":
    print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    
# Will the above print statement print to the console?
# Set response to 'Y' if you think so, and 'N' if you think not.

#Q12
def using_control_once():
    if True:
        return "Success #1"

def using_control_again():
    if True:
        return "Success #2"

print using_control_once()
print using_control_again()


#Q13
answer = "'Tis but a scratch!"

def black_knight():
    if answer == "'Tis but a scratch!":
        return True
    else:             
        return False      # Make sure this returns False

def french_soldier():
    if answer == "Go away, or I shall taunt you a second time!":
        return True
    else:             
        return False       # Make sure this returns False


#Q14
def greater_less_equal_5(answer):
    if answer > 5:
        return 1
    elif answer < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


#Q15
# Complete the if and elif statements!
def grade_converter(grade):
    if grade >= 90:
        return "A"
    elif grade < 90 and grade >= 80:
        return "B"
    elif grade < 80 and grade >= 70:
        return "C"
    elif grade < 70 and grade >= 65:
        return "D"
    else:
        return "F"
      
# This should print an "A"      
print grade_converter(92)

# This should print a "C"
print grade_converter(70)

# This should print an "F"
print grade_converter(61)