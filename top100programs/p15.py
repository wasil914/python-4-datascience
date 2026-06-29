# Fibonacci Series upto nth term 

terms = int(input('Enter terms :'))
n1,n2 = 0,1
if terms<=0:
    print('Enter a positive interger.')
elif terms == 1:
    print('Fibonacci Sequence:',n1)
else:
    for _ in range(terms):
        print(n1,end=' ')
        n = n1+n2
        n1=n2
        n2=n
