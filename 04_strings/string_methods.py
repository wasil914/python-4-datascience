s1 = "hello world"

s2 = "  Python Programming  "

s3 = "CAMPUSX"

s4 = "data_science_2026"

s5 = "welcome,TO,the,jungle"

s6 = "apple,banana,mango,grapes"

s7 = "12345Python67890"

s8 = "email@example.com"

s9 = "Learning Python is Fun!"

s10 = "    kodnest academy    "
s11 = ['apple','banana','mango','grapes']

print("upper() : ",s1.upper())
print("lower() : ",s3.lower())
print("capitalize() : ",s1.capitalize())
print("title() : ",s6.title())
print("strip() : ",s10.strip())
print("replace() : ",s9.replace("Fun","Simple & Easy"))

print("spilt() : ",s5.split(','))

print("'+'.join() : ", '+'.join(s11))

print("find() : ",s9.find('s'))

print("in :" , ('data' in s4))


print("count() : ",s9.count('n'))

print("startswith() : ",s7.startswith('12345'))
print("endswith() : ",s7.endswith('890'))

print("isdigit() : ",s3.isdigit())
print("isalpha() : ",s9.isalpha())
print("isalnum() : ",s7.isalnum())

