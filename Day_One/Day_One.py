print("Greetings")
student="Baron"
print(f"Greetings {student}")
stacks=["Java", "Python"]
score=8
if score>8:
    print("pass")
elif score==8:
    print("Barely Passed")
else:
    print("Better luck next time")

#for i in range(0,11,1):
    #print(i)

#print(len(stacks))

for i in range(0,len(stacks),1):
    print(stacks[i])

for item in stacks:
    print(item)
print(dir(stacks))

stacks.append("C++")
print(stacks)

def sumPlusLength(lst)
    return lst[0] + len(lst)

print)sumPlusLength([5,4,3,2,1]))

num = 12
if num % 2 == 0:
    print ("I am even")

#[12,3,4,5,6]

lst=[12,3,4,5,6]
for i in range(len(lst)):
    if lst[i] % 2 != 0:
        lst[i] = "odd"
print(lst)

students = ["bob", "jeff","bob","wallace","bob", "gromet"]
new_students=[]
list_memory = 0
for i in range(0,len(students),1):
    if students[i] != "bob":
        #new_students[list_memory] = students[i]
        list_memory += 1
print(new_students[i])



