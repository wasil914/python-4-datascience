#Sum of First N Natural numbers: 

#for loop

N = int(input('Enter N : '))
sum = 0
for i in range(1,N+1):
    sum = sum + i
print(f"The sum of First {N} Natural numbers is {sum}.")
 
#while loop

N = int(input('Enter N : '))
sum = 0
i = 1
while(i<=N):
    sum = sum+i
    i+=1                # i = i +1
print(f"The sum of First {N} Natural numbers is {sum}.")