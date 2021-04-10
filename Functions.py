#The def keyword signifies the declaration of a function. This indicates that the following code is a function and assigns a name to that function, so we can call it later. Parameters are inputs the function is expecting and appear inside the parenthesis that follow the function name.

def add (a,b): # function name: "add", parameters: a and b
    x = a + b # process
    return x   # returns value: x

#We have declared a function with the def keyword, named it add, and specified that it takes two inputs (parameters). If this is all we have in our file, nothing would actually appear to happen if we ran it. To actually run the function, we must execute it by invoking or calling it. This is done outside of the function using the function name followed by (). Inside the parenthesis are any values (arguments) the function is expecting as input.

new_val = add(3, 5) #calling the add function, with arguments 3 and 5
print(new_val) #the result of the add function gets sent back to and saved into the new_val, so we will see 8

#Once invoked, a function can give us an output. Some functions take an input and some functions don't give us an output. Even if no output is produced, the code inside the function can alter the program - this is called a side effect. Based upon what we learned above, a function that doesn't return anything would produce no output!

#Parameters and Arguments

#We define the input of functions using parameters. Functions can have as many parameters as we need, including 0. Here we've defined the say_hi function with one parameter called name:
def say_hi(name):
    print("Hi, " +name)

#Now we can invoke this function by calling its name and passing in the correct number of arguments:
#invoking the function 3 times by calling its name and passing in one argument each time
say_hi('Michael')
say_hi('Ana')
say_hi('Eli')

#Wait, but what's the difference between a parameter and an argument? These two words get mixed up a lot in programming. In this example 'name' is a parameter while "Michael", "Anna", and "Eli", are arguments. We define parameters. We pass in arguments into functions.

#Returning Values

#So far none of our functions had any value that we could hold onto. In many cases, we would want our function to return some sort of value that we can use later in our program. The following concept is critical in understanding how to use functions correctly in your code:

#It is very important to remember the following: a function call is equal to whatever that function returns. This might not make sense until we see it in action.

#Let's modify our original say_hi function and observe the differences:
def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting) #this will output 'Hi Michael'

#Going back to our add function, recall that it takes two parameters and returns the sum of the parameters.

def add(a,b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

#What do you think the values of sum1, sum2, and sum3 would be?

#If you guessed 10, 5, and 15, respectively, good job! sum1 was set to the return value of the add function invoked with 4 and 6 as arguments. Similarly, sum2 was set to the return value of invoking add with 1 and 4. The variable sum3 contains the sum of sum1 and sum2 which is 15. Storing these return values in variables allows us to use the results of our functions throughout the rest of our program.

#In our examples you may have noticed that our functions were returning values of different data types. Functions can return any of the data types - strings, numbers, lists, tuples, dictionaries and even other functions!
