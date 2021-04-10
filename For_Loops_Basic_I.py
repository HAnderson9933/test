#Basic - Print all integers from 0 to 150.

def basic():
    for i in range(0, 151):
        print(i)

basic()

#Multiples of Five - Print all the multiples of 5 from 5 to 1,000

def multiples_of_five():
    for i in range(5, 1001,5):
        print(i)

multiples_of_five()

#Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

def the_dojo_way():
    for i in range(1, 101):
        if i % 10 == 0:
            print("Coding Dojo")
        elif i % 5 == 0:
            print("Coding")
        else:
            print(i)

the_dojo_way()

#Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

def the_final_sum():
    final_sum = 0
    for i in range(1, 500000, 2):
        final_sum += i
    print(final_sum)

the_final_sum()

#Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

def positive_nums():
    for i in range(2018, 0, -4):
        print(i)

positive_nums()

#Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def flex_counter(low_num, high_num, mult):
    for i in range(low_num, high_num +1):
        if i % mult == 0:
            print(i)

flex_counter(2, 9, 3)
