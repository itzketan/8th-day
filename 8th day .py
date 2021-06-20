print("--------------------------------------------------------------------")
# Write a Python script to merge two Python dictionaries
A = {'Cat': 'black', 'Cow': 'Red ' }
N= {'Meow': 'Cat', 'Bark': 'Dog'}
C= A.copy()
C.update(N)
print(C)
print("--------------------------------------------------------------------")
# Write a program to sort the value from descending to ascending in list and convert it in to a set.
Numbers = [9,8,7,6,5,4,3,2,1,0]
print("Descending Numbers are : ", Numbers)
Numbers.sort()
print("Ascending Numbers are : ", Numbers)
K = set(Numbers)
print("List to Set : ", K)
print("--------------------------------------------------------------------")
# Write a Python program to list number of items in a dictionary key and sort the
# list with the help of a function & without the function.
d_dict = { 'ball': [2, 4, 6], 'apple': [8, 10, 12],'cat': [14,16,18] }
print("Given Dictionary : " + str(d_dict))
res = {key : sorted(d_dict[key]) for key in sorted(d_dict)}
print("The Sorted Dictionary : " + str(res))
# without the function.
new = sorted(d_dict)
print(new)
print("--------------------------------------------------------------------")
# Write a Python program to get a string from a given string (user input) and
# change the first occurrence of the word to a user specified input.
string = input("Please Enter your String : ")
char = input("Please Enter Word : ")
string2 = ''
length = len(string)
i = 0

while(i < length):
    if(string[i] == char):
        string2 = string[0:i] + string[i + 1:length]
        break
    i = i + 1
 
print("Original String :  ", string)
print("Final String :     ", string2)
print("--------------------------------------------------------------------")
# Write a Python program to get a string from a given string where all
# occurrences of its first char have been changed to capital letter.
# Take a string input
text = input("Enter a text\n")

# Split the text based on space
strList = text.split()

# Define a variable to store the converted string
newString = ''

# Iterate the list
for val in strList:
 newString += val.capitalize()+ ' '

# Print the original string
print('The original string is : %s' %text)

# Print the converted string
print('The converted string is : %s\n' %newString)
print("--------------------------------------------------------------------")
# Write a Python program to find the repeated items of a list
some_list = ['a','n','h','h','a','b','b']
print("List : ", some_list)
my_list = sorted(some_list)
 
duplicates = []
for i in my_list:
     if my_list.count(i) > 1:
         if i not in duplicates:
             duplicates.append(i)
 
print("Duplicates : ", duplicates)
print("--------------------------------------------------------------------")
# Write a Python program to check the sum of three elements and divided by a
# value which is given as an input by the user
x = int(input('Enter 1st Number : '))
y = int(input('Enter 2nd Number : '))
z = int(input('Enter 3rd Number : '))
sum = (x + y + z)
print("Sum : ", sum)
d = int(input('Enter Divide value : '))
A = sum / d
print('After Divide : ', A)
print("--------------------------------------------------------------------")
# Write a Python program to find the Mean,median,mode among three given numbers
a = int(input("1st Number : "))
b = int(input("2nd Number : "))
c = int(input("3rd Number : "))
mean = ((a + b + c) / 3)
print("Mean of Given Numbers : ", mean)
z = [a, b, c]
n = len(z) 
z.sort() 
  
if n % 2 == 0: 
    median1 = z[n//2] 
    median2 = z[n//2 - 1] 
    median = (median1 + median2)/2
else: 
    median = z[n//2] 
print("Median of Given Numbers : " + str(median))
# the Mode

z.sort()
L1 = []

i = 0
while i < len(z):
    L1.append(z.count(z[i]))
    i += 1
d1 = dict(zip(z, L1))

d2 = {k for (k, v) in d1.items() if v == max(L1)}

print("Mode(s) is/are :" + str(d2))


print("--------------------------------------------------------------------")
# Write a Python program to swap cases of a given string
def swap_case_string(str1):
   result_str = ""   
   for item in str1:
       if item.isupper():
           result_str += item.lower()
       else:
           result_str += item.upper()           
   return result_str

print(swap_case_string("Python Exercises"))
print(swap_case_string("Java"))
print(swap_case_string("NumPy"))
print("----------------------------------------------------------------------")
# Write a program to convert an integer to binary & octa decimal
# Take decimal number from user
dec = int(input("Enter an integer : "))
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
