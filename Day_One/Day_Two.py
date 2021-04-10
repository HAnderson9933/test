student={
    "name": "Sheker",
    "email": "s@gmail.com",
    "age": 20,
    "stacks":["Java", "Mean", "Mern"]
}
print(student)

print(student['name'])
print(student.get('name'))

print(student.items())
print(student.values())

for key,value in student.items():
    print(f"Key is {key} and value is {value}")

student['email']='somethingnew@gmail.com'
print(student)
print(dir(student))

def greet(name="Ninja", stack="Python", dojo="Chicago"):
    return(f"Greetings {name} Welcome to {stack}")


print(greet("Gus").upper())
print(greet())
print(greet("Caden", "MEAN"))
print(greet(stack="MERN"))
print(greet(name="", stack="C++"))