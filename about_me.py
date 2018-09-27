#!/urs/bin/env python3

# First, create a variable called start, and set it equal to "I am ".
# Remember the space after the word "am" !
start = "I am "

# Next, create a variable called age and set it equal to your age in years.
# This must be a number
age = 46

# Next, create a variable called end, and set it equal to " years old".
# Remember the space before the word "years"
end = "years old"

# Next, create a variable called output, and use the format() function to add
# together the start, age and end variables. 
output = "{0}{1} {2}".format(start, age, end)
# An example output string would be "I am 15 years old"


# Finally, print the output to the screen using the print() function.
print(output)
