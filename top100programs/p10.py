# Sum of digits of a number

number = int(input('Enter number:'))
originalnum=number
sum = 0
while(number>0):
    digit = number % 10
    sum = sum + digit
    number = number//10
print(f'{sum} is the sum of digits of the number {originalnum}')
