#code block
x = 10
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50") 

#pass
class EmptyClass:
    pass

#for val in my_string:
    #pass

#Data Types

#Primitive Data Types

#Boolean Values
is_hungry = True
has_freckles = False

#Numbers 
age = 35 # Storing and int
weight = 160.57 # storing a float

#Strings 
name = "Joe Blue"

#Composite Types

#Tuples- data that is immutable(can't be modified after creation) holds a group of values. Can contain mixed data types.
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0]) #Output: Bruce
dog[1] = 'dachshund' #error: cannot be modified ('tuple' object does not support item assignment)

#Lists- data that is mutable and can hold a group of values. Usually ment to store a collection of related data.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) #Output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas) #Output:['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas) #Output:['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas) #Output['Francis', 'Oliver']

#Dictionaries- A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to acceess values. 
empt_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack' #updates if the key exists
new_person['hobbies'] = ['climbing', 'coding'] #adds a key value pair if the key doesnt exist
print(new_person)
#output:{'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight') #removes the specified key and returns the value
print(w) #output: 160.2
print(new_person)
#output {'name': 'Jack', 'age': 38,'has_glasses': False, 'hobbies': ['climbing', 'coding']}

#Common Funtions
#type function for values and variable data types
print(type(2.63)) #output: <class 'float'>
print(type(new_person)) #output: <class 'dict'>

#len function for data types that have a length attribute (eg lists, dictionaries, tuples, strings)
print(len(new_person)) #output: 4(the number of key-value pairs)
print(len('Coding Dojo')) #output: 11

#Type Casting or Explicit Type Coversion
#print("Hello" + 42) #output: TypeError
print ("Hello " + str(42)) #output: Hello 42

#receiving a string input from a user that we want to treat as a number
total = 35
user_val ="26"
#total = total + user_val #output: TypeError
total = total + int(user_val) #total will be 61

#Condtional Statements
#if, elif, else
x = 12
if x > 50:
    print("bigger than 50")
else:
    print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute

x = 55
if x > 10:
    print("bigger than 10")
elif x > 50:
    print("bigger than 50")
else:
    print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
if x < 10:
    print("smaller than 10")
    # nothing happens, because the statement is false   

#For loops with range
for x in range(0, 10, 1):
for x in range(0, 10):	# increment of +1 is implied
for x in range(10):	# increment of +1 and start at 0 is implied

#Note: if you need to specify an increment other than +1, all three arguments are requeired
for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

#For Loops through Lists
my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

#For Loops throgh Dictionaries
#When we iterate through a dicitonary, the iterator is each of the keys of the dictionary
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(k)
# output: name, language

#When we want values of the dictionary
my_dict = { "name": "Noelle", "language": "Python" }
for k in my_dict:
    print(my_dict[k])
# output: Noelle, Python

#another way to iterate through the keys
# another way to iterate through the keys
for key in capitals.keys():
    print(key)
#to iterate through the values
for val in capitals.values():
    print(val)
#to iterate through both keys and values
for key, val in capitals.items():
    print(key, " = ", val)

#While Loops
count = 0
while count < 5:
    print("looping - ", count)
    count += 1

#Basic sytax for while loop:
while <expression>:
    # do something, including progress towards making the expression False. Otherwise we'll never get out of here!

#Else
#what if the condition was not met and we still would like to do something if that happens?
y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

#Loop Control
#Loops, breaks, and continues are all a part of control flow as well.
#When you want finer control over your loops, use the following statements to do so.
#When loops are nested, a break will only exit from the innermost loop.
for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

#Continue immediately returns control to the beginning of the loop. The continue statement rejects, or skips, all the remaining statements in the current iteration of the loop, and continues normal execcution to the top of the loop. Is very useful when you want to skip spcific iteration(s), but still keep looping to the end
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
    print("Final else statement")
# output: 3, 2, 1












