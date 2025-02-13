# To find the factorial of a number in Python

no = int(input("Enter the number: "))
fact = 1
for i in range(1,no+1):
    fact*=i

print("The factorial of", no, "is", fact)