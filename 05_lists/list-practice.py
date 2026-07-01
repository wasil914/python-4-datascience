student_list = ['Rajesh','Darshar','Megha']
print(student_list)
student_list.append('Nikhil')
print(student_list)
student_list.append('Rajesh')
print(student_list)
student_list.insert(1,'Rahul')
print(student_list)
student_list.pop(2)
print(student_list)
student_list.pop()
print(student_list)
student_list.append('Rajesh')
print(student_list)
student_list.remove('Rajesh')
print(student_list)
student_list[1]='Rahil'
print(student_list)

student_list.sort()
print(student_list)
student_list.reverse()
print(student_list)
print(len(student_list),type(student_list))


nums = [1,2,3,6,7,4,87]
nums.sort(reverse=True)
print(nums)

list1= [1,2,3]
list2 =['a','e','r']
l3 = list1 +list2
print(l3)
for num in l3:
    print(num)
list4 = l3
print(l3,"\n",list4)
list5 = l3.copy()
print(list5)
list5.clear()
print(list5)
del list5
# print(list5)

#unpacking a list
nums = [ 1,2,3,4,56,66]
a,b,c,d,e,f = nums
print(a,b,c,d,e,f)

a,b,*c=nums
print(a,b,c)

a ,*b,c ,d = nums
print(a,b,c,d)

a,*b,c,d = nums
print(a,b,c,d)