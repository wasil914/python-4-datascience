#Positive or Negative number

number = int(input('Enter a number : '))

if number == 0 :
    print(f"You entered Zero!")

if number > 0 :
    print(f'You entered {number} which is a Positive Number. ')
elif number < 0 :
    print(f'You entered {number} which is a Negative number. ')