num1 = 12 
num2 = 11
num3 = 10
num4 = 4

#Arithmetic Operators
print('Addtition: +\t',num1+num2)
print('Subtraction: -\t',num1-num4)
print('Multiplication: *\t',num1*num3)
print('Floor Division: /\t',num1/num4)
print('Float division: //\t',num3//num4)
print('Modulus: %\t',num2%num4)
print('Exponentiation: **\t',num3**num4)

print('***************************************')
#Assignment Operators
x = 10
print('\nStarting value : x =',x)

x += 5
print('\nAfter +=5 : x =',x)

x -= 3
print('\nAfter -=3 : x =',x)

x *= 2
print('\nAfter *=2 : x =',x)

x /= 4
print('\nAfter /=4 : x =',x)

x //= 4
print('\nAfter // = 4 : x =',int(x))

x **= 5
print('\nAfter **= : x =',x)

x %= 1
print('\nAfter %= : x =',x)

x = 7

x &= 2
print('\nAfter &= : x =',x)#2

x |= 5
print('\nAfter |= : x =',x)#7

x ^= 4
print('\nAfter ^= : x =',x)#3

x <<= 4
print('\nAfter <<= : x =',x)#48

x >>= 3
print('\nAfter >>= : x =',x)#6

x = ~x
print('\nAfter ~x: x =',x) #-7



#Bitwise Operators
x = 7 #0000 0111
y = 3 #0000 0011
print()

#bitwise and -> &

print(x&y) #0000 0011 = 3
print()

#bitwise or -> |

print(x|y) #0000 0111 = 7
print()

#bitwise not  -> ~

print(~x)#-(8)
print(~y)#-(4)
print()

#bitwise xor -> ^

print(x^y) #0000 0100 = 4
print()

#bitwise Left shift -> <<
print(x<<y) #7*(2**3) =56
print()

#bitwise Right shift -> >>
print(x>>y) #7//(2**3) = 0

#Comparison Operators / relational operators
x = 3
y = 7  

print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x<=y)
print(x>=y)

#Chaining Comparison Operators
x = 45
print(x>40 and x<50)
print(40<x<50)


#logical operators
a = True
b = False 
print('a and b:',a and b)
print('a or b:\t',a or b)
print('not b:\t',not b)
print('not a:\t',a and b)

#Relational & logical operators used together 

x = 10
y = 5
print('\n(x>5) and (y<10) =',(x>5) and (y<10)) # true
print('\n(x<5) and (y>10) =',(x<5) and (y>10)) # false

print('\n(x>5) or (y<10) =',(x>5) or (y<10)) # true
print('\n(x<5) or (y>10) =',(x<5) or (y>10)) # false

print('\nnot(x==10) =',not(x==10) ) # False
print('\nnot(y==3) =',not(y==3) ) # True



#Identity Operators
x = ['apple','banana']
y = ['apple','banana']
z = x

print('x is z',x is z)
print('x is y',x is y)
print('x == y',x == y)

#Membership Operators

x = 'HelloMyLord'
print('He' in x)
print('Llm' not in x )

fruits = ['f1','f2','f3']
print('f4' in fruits)
print('f2' not in fruits)




