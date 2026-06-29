# Armstrong number

number = int(input('Enter input: '))

original_num = number
num_len = len(str(original_num))
total = 0

while number > 0:
    digit = number % 10
    total = total + digit ** num_len
    number = number // 10

if total == original_num:
    print(f'{original_num} is an Armstrong number.')
else:
    print(f'{original_num} is not an Armstrong number.')