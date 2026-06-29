# Armstrong number in a given range : 
start = int(input('Enter Start Range:'))
end = int(input('Enter End Range:'))


for i in range(start,end+1):
    number = i
    original_num = number

    l_num = len(str(number))
    total = 0
    while (number>0):
        digit = number%10
        total = total + digit**l_num
        number = number//10

    if (total == original_num):
        print(f'{original_num} is an armstrong number')

    