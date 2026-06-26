num = int(input('Enter number: '))
if num>0 :
    print("positive")
    if num%2 == 0:
        print('Even')
    else:
        print('Odd')
else:
    print('Negative Number')

user_name = input('Enter Username: ')
passwrd = input('Enter Password: ')
if user_name == 'admin':
    if passwrd == '1234':
        print('Login Successuful. ')
else:
    print('Please enter valid credentials.')
