s = 'kodnest'
#-7-6-5-4-3-2-1
# k o d n e s t
# 0 1 2 3 4 5 6
 
'''Positive slicing'''

print(s[0:3])#kod
print(s[:3])#kod

print(s[3:7])#nest
print(s[3:8])#nest
print(s[3:])#nest
'''Negative Slicing'''

print(s[-7:-4])#kod
print(s[:-4])#kod

print(s[-4:],"Negative Slicing")#nest
print(s[-4:7])
print(s[-4:100])


#stepcount
'''
   c a m p u s x
   0 1 2 3 4 5 6
  -7-6-5-4-3-2-1
  '''


str = "campusx"
print(str[::3]) #cpx
print(str[0::2])#cmux
print(str[2:5:2])#mu

print(str[::-1])#xsupmac
print(str[5:0:-2])#ampus aps ->spa

