N = int(input('Enter Number : '))
factorial_p = 1
for i in range(1,N+1):
    factorial_p = factorial_p * i
print(f"The factorial of {N} is {factorial_p}")