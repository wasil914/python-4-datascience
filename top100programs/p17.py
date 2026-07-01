#Factorial of a number 
number = int(input('Enter number: '))
product = 1

for i in range (1,number+1):
    product = product * i

print(f"Factorial of {number} is {product}.")
