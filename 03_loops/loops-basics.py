number = int(input('Enter Number: '))
if number>0:
    print('Positive Number')

passing_marks = int(input('Enter Marks Obtained: '))
if passing_marks>=40 :
    print('Passed!')

input_num = int(input('Enter any number: '))
if input_num % 2 == 0 :
    print('Even number')
else:
    print('Odd number')

eligible_age = int(input('Enter Age: '))
if eligible_age>=18:
    print('Eligible to vote')
else:
    print('Not eligible')

student_marks = int(input('Enter marks obtained: '))
if student_marks>= 90:
    print('A')
elif 89>=student_marks>=75:
    print('B')
elif 74>=student_marks>=60:
    print('C')
else:
    print('fail')

side1 = float(input('Enter side 1: '))
side2 = float(input('Enter side 2: '))
side3 = float(input('Enter side 3: '))

if (side1 == side2 == side3):
    print('Equilateral Triangle ')
elif (side1==side2 or side2==side3 or side3==side1):
    print('Isosceles Triangle ')
elif (side1 != side2 and side2 != side3 and side3!=side1):
    print('Scalene Triangle')

num1 = int(input('Enter 1st number :'))
num2 = int(input('Enter 2nd number :'))
num3 = int(input('Enter 3rd number :'))

if num1>=num2 and num1>=num3 :
    print('Greatest:',num1)
elif num2>=num1 and num2>=num3:
    print('Greatest:',num2)
else:
    print('Greatest:',num3)

