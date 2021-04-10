
#Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
#Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

def biggie_size(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i]="big"
    return arr
print(biggie_size([-1,3,5,-5]))

#Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).

def positive_values(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count = count + 1
    arr[len(arr)-1]=count
    return arr
print(positive_values([-1,3,5,-5]))


#Sum Total - Create a function that takes a list and returns the sum of all the values in the array.
#Example: sum_total([1,2,3,4]) should return 10
#Example: sum_total([6,3,-2]) should return 7

def sum_total(lst):
    sum=0
    for i in range(len(lst)):
        sum += lst[i]
    return sum
print(sum_total([1,2,3,4,]))

#Average - Create a function that takes a list and returns the average of all the values.
#Example: average([1,2,3,4]) should return 2.5

def average(lst):
    sum= 0
    for i in range(len(lst)):
        sum += lst[i]
        average = sum / len(lst)
    return average
print(average([1,2,3,4]))

#Length - Create a function that takes a list and returns the length of the list.
#Example: length([37,2,1,-9]) should return 4
#Example: length([]) should return 0

def length(lst):
    count=0
    for i in range(len(lst)):
        count = count + 1
    return count
print(length([37,2,1,-9]))

#Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
#Example: minimum([37,2,1,-9]) should return -9
#Example: minimum([]) should return False

def minimum(lst):
    if len(lst) == 0:
        return False
    for i in range (len(lst)):
        if lst[i] < 0:
            return lst[i]

print(minimum([]))
print(minimum([37,2,1,-9]))

#Maximum - Create a function that takes a list and returns the maximum value in the array. If the list is empty, have the function return False.
#Example: maximum([37,2,1,-9]) should return 37
#Example: maximum([]) should return False

def maximum(lst):
    if len(lst) == 0:
        return False
    
    max = lst[0]    
    for i in lst: 
        if i > max:
            max = i
    return max

print(maximum([]))
print(maximum([37,2,1,-9]))

#Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
#Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

def ultimate_analysis(lst):
    dictionary = {
        'sum_total': None,
        'maximum': None,
        'minimum': None,
        'average': None,
        'length': 0
    }
    if len(lst) == 0:
        return dictionary
    else: 
        dictionary['sum_total'] = 0
        dictionary['maximum'] = lst[0]
        dictionary['minimum'] = lst[0]

    for i in lst:
        if i > dictionary['maximum']:
            dictionary['maximum'] = i
        elif i < dictionary['minimum']:
            dictionary['minimum'] = i

        dictionary['sum_total'] += i
        dictionary['length'] += 1
    dictionary['average'] = dictionary['sum_total'] / len(lst)

    return dictionary 

print(ultimate_analysis([37,2,1,-9]))
print(ultimate_analysis([]))


#Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
#Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

def reverse_list(list):
    length = len(list)-1
    x = length
    for i in range (len(list)//2):
        list[i], list[x-i]= list[x-i], list[i]
    return list
y = reverse_list([37,2,1,-9,])
print(y)











