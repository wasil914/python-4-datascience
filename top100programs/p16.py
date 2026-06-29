# Find the Nth Term of the Fibonacci Series 
term = int(input('Enter which term:')) 
n1 , n2 = 0 ,1

if term <=0:
    print('Please enter positive integer.')
elif term == 1:
    print(f'{term}st of fibonacci series is {n1}')
elif (term >1):
    for i in range(term-1):
        n = n1+n2
        n1=n2
        n2=n
print(n1)