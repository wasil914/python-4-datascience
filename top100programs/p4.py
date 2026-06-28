#Sum of numbers in a given range

#for loop
s = int(input('Enter start range:'))
e = int(input('Enter end range:'))
sum = 0
for i in range(s,e+1):
    sum = sum + i
print(f"The sum of numbers from range {s} to {e} is {sum}.")


#while loop
s = int(input('Enter start range:'))
e = int(input('Enter end range:'))
sum = 0
i=s
while(i<=e):
    sum = sum + i
    i+=1
print(f"The sum of numbers from range {s} to {e} is {sum}.")

