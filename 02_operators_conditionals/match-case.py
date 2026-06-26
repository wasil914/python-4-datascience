#Q1
day = int(input('Enter Day Number: '))
match day:

    case 2:
        print('Monday')
    case 3:
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5:
        print('Thursday')
    case 6:
        print('Friday')
    case 7:
        print('Saturday')
    case _:
        print('Invalid')
#Q2
user_input = input('Enter : ')
match user_input:
    case 'a':
        print('Add')
    case 'b':
        print('Browse')
    case 'c':
        print('Cancel')
    case _ :
        print('Invalid Option')
    