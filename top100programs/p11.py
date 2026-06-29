# Reverse of a number 

number = int(input('Enter number: '))
original_number = number
reverse = 0
while(number>0):
    digit = number%10
    reverse = reverse * 10 + digit
    number = number //10

print(f'{reverse} is the reverse of {original_number}')
