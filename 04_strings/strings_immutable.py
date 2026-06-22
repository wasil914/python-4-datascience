#case1
s1 = "Hello"
s2 = s1 +"World"
print(s1,id(s1))
print(s2,id(s2))

#case2
s1='Hello'
print(s1,id(s1))
s1= s1 + 'World'
print(s1,id(s1))

#case3
s1='Python'
s2='Python'
print(s1,id(s1))
print(s2,id(s2))
print(s1 is s2)