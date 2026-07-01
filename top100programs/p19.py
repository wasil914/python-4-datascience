# Find the Factors of a Number
number = int (input('Enter Number: '))
found = False

for i in range(2,number):
    if number%i==0:
        if not found:
            print("Factors are: ",end=' ')
            found = True
        print(i,end=' ')
if not found:
    print(f"{number} is prime i.e having 1 and {number} as factors only.")