# All the basic Python operations


# string concatinate

'''str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string: ")

print("Concatinated string is ", str1 + str2)

# string slicing

str = input("Enter the string: ")
n1 = int(input("Enter how many aplphabets to be sliced: "))

print("Sliced string is ", str[n1:])

# string reversing

str = input("Enter string to be reversed: ")
print("Reversed string is ", str[::-1])

# item accessing 

str = input("Enter a string: ")
for letter in str:
    print(letter)

# check whether letter is present

str = input("Enter a string: ")
letter = input("Enter a letter to check: ")

if letter in str:
    print("Letter ",letter, " is present in ", str)
else:
    print("Letter ",letter, " is not present in ", str)'''

# replace a string 

str = input("Enter string of your choice: ")
txt = input("Enter which string to be replaced: ")
rep = input("Enter the string to be replaced: ")

x = str.replace(txt,rep)
print("The final string is ", x)