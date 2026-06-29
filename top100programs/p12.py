# Palindrome number
number = int(input('Enter number: '))
original_num = number

reverse = 0
while(number>0):
    digit = number % 10
    reverse = reverse * 10 + digit
    number =  number //10

if reverse == original_num :
    print(f'{original_num} is Palindrome.') 
else:
    print('Not Palindrome')