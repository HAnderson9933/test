# 1. TASK: print "Hello World"
print("Hello World")

# 2. print "Hello Hope!"with the name in a variable
name = "Hope"
print("Hello", name) #with a comma
print("Hello " + name) #with a +

# 3. print out "Hello 9" with the number in a variable
name = 9
print("Hello", name) #with a comma
#print("Hello " + name) #with a +  -- this one should give us an error!

# NINJA BONUS: Figure out how to resolve the error from above, without changing the + to a comma
name = 9
print("Hello " + "9")

# 4. print "I love to eat sushi and pizza." with the food in variables
fav_food1 = "sushi"
fav_food2 = "pizza"
print("I love to eat {} and {}.".format(fav_food1, fav_food2)) # with .format()
print(f"I love to eat {fav_food1} and {fav_food2}.") # with an f string

#NINJA BONUS: Spend a few minutes playing around with other string methods to see what's out there

name = "hope"
print(name.upper()) # returns a copy of the string with all the charaters uppercase

name = "HELLO!"
print(name.lower()) #returns a copy of the string with all the charaters in lowercase.

quote = "To be, or not to be"
print(quote.count("be")) # returns the number of occurences of substring in string


txt = "A whole new world!"
x = txt.split()
print(x) # returns a list of values where string is split at the given charater

txt = "Hello, and how are you?"
x = txt.find("are")
print(x) # returns the index of the start of the first occurrence of "are" within the string

name ="Coding101"
x = name.isalnum()
print(x) # returns boolean depending on whether the string's length is > 0 and all charaters are alphanumeric

name = ("Hope", "Nicole", "Anderson")
x = "!".join(name)
print(x) #returns a string that is all strings within our set (in this case a list) concatenated.

txt = "The End!"
x = txt.endswith("!")
print(x) #returns a boolean based upon whether the last characters of string match substring.


