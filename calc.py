def addition(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b


num1 = int(input("Enter 1st no: "))
num2 = int(input("Enter 2nd no: "))

print("Choose options:\n")
print("1. Additon\n2. Subtraction\n3. Multiply\n4. Division")
opt = int(input("Enter option: "))
while True:

    match(opt):
        case 1:
            add = addition(num1,num2)
            print("Addition is ",add)
            break
        case 2:
            sub = subtract(num1,num2)
            print("Subtraction is",sub)
            break
        case 3:
            mul = multiply(num1,num2)
            print("Multiplication is ",mul)
            break
        case 4:
            div = division(num1,num2)
            print("Division is ",div)
            break
        