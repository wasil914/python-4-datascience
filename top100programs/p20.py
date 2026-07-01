# Finding Prime Factors of a number

number = int(input('Enter number:'))

for i in range(2,number+1):
    for j in range(2,i):
        if i%j!=0:
            i=j
        print(j)

