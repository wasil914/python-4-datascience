# end parameter in print function is used to specify what to print at the end of the output. 
# By default, it is a newline character (\n), which means that each print statement will be printed on a new line.
#  However, you can change this behavior by setting the end parameter to a different value.
print("Hello, consistency",end="\t ")
print("beats talent")
print("Artificial \nIntelligence")
print("Python supports",end=" + \n")
print("multiple paradigms of programming")
print("SQL Database")
print("SQL \nDatabase")
print("SQL\n Database")
print("SQL","Database")

#sep parameter in print function is used to specify what to print between the items that are being printed. 
# By default, it is a space character, which means that the items will be separated by a space when printed.
#  However, you can change this behavior by setting the sep parameter to a different value.
print("Hi","Guido van rossum","Python founder",sep="\n")
print("14","09","2002",sep="/")
print("Vowels","a,e,i,o,u",sep=":")


#variables in python are used to store data. They are created by assigning a value to a name.
#data types in python are used to specify the type of data that a variable can hold.
#multiple variables can be assigned values in a single line using comma separation. This is called multiple assignment.

emp_name ="CodeWithHarry"
emp_sal = 1000000
emp_yoe = 2.5
emp_fav_data_type = 3+2j
emp_is_cool = True
emp1_name , emp1_sal , emp1_yoe = "LoveBabbar" , 500000 , 5.5
print(emp1_name, emp1_sal, emp1_yoe ,"\n",emp_name, emp_sal, emp_yoe, emp_fav_data_type, emp_is_cool)


#type() function is used to check the data type of a variable. It returns the type of the variable as a string.
print(emp_name, type(emp_name))
print(type(emp_sal))
print(type(emp_yoe))

#formatted string is a string that contains placeholders for variables.
# The placeholders are replaced with the values of the variables when the string is printed.
print(f"This is a formatted string.My employee name is {emp_name} and his salary is {emp_sal}")

name = 'Wasil'
age = 23
print(f"My name is {name} and my age is {age}") 

name = 'ali'
marks = 95
print(f"{name} scored {marks}")

price = 49.9999
print(f"Price: {round(price):.2f}")

avg = 83.413333333
print(f"Average score: {avg:.2f}")

pi = 3.14159265359
print(f"Pi Value: {pi:.2f}")
print(f"Pi Value: {pi:.4f}")


#round() function
num1 = 123.100
print(round(num1))