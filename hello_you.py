#!/urs/bin/env python3

# Ask for user name
name = input("what is your name?: ")
print(name)

# ask user for age
age = input("What is your age?: ")
print(age)

# Ask user for city
city = input("What city do you live in?: ")
print(city)

# Ask user what they enjoy.
love = input("What do you love doing?: ")
print(love)

string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name, age, city, love)

# Print output to screen.
print(output)
