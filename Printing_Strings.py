#String Literals
print("this is a sample string")

#Concatening Strings and Variables with the Print Function
name = "Zen"
print("My name is", name)
name = "Zen"
print("My name is " + name)

#String Interpolation
#F-Strings(Literal String Interpolation)
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"My name is {first_name} {last_name} and I am {age} years old.")

#string.format()
first_name = "Zen"
last_name = "Coder"
age = 27
print("My name is {} {} and I am {} years old.".format(first_name, last_name, age))
print("My name is {} {} and I am {} years old.".format(age, first_name, last_name))

#%-formating
hw = "Hello %s" % "world"
py = "I love Python %d" % 3
print(hw, py)
name ="Zen"
age = 27
print("My name is %s and I'm %d" % (name, age))

#Built-in String Methods
x = "Hello world"
print(x.title())