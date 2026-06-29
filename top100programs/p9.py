# Prime number within a given range:
start = int (input('Enter Start Range > 1:'))
end = int(input('Enter End Range:'))
for j in range(start , end +1):
    if j < 2:
        continue
         
         
    for i in range (2,j):
        if j % i == 0:
            break
    else:
            print(f'{j} is prime.')
    