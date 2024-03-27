# # a=[1,7,-10,34,2,-8]
# # count=0
# # for i in a:
# #  count+=i
# # print(count)
# import random
#
# b=[3,4,5,4,7]
# mul=1
# for i in b:
#     mul*=i
#     print("The mutiplication of all elements in list are:",mul)
#
# c = [1, 7, 10, 34, 2, 8]
# print("max in list",max(c))
#
# d=[51,7,10,34,2,8]
# print("Minimum from d is",min(d))
#
# e=[51,2,10,2,2,734,2,8]
# dup=[]
# for i in e:
#   if i not in dup:
#     dup.append(i)
# print(dup)
#
#
# f=['abc', 'xyz', 'aba', '1221','pp']
# for i in f:
#     if len(i)==2 or len(i)>2:
#      if i[0]==i[-1]:
#          print(i)
#
# g=[1,2,3,7,2,1,5,6,4,8,5,4]
# dup=[];non=[]
# for i in g:
#  if i not in dup:
#   dup.append(i)
# print(dup)
#
# h=[3,52,46,87,9,2]
# if len(h)==0:
#     print("list is  empty")
# else:
#     print("list is not empty")
#
# i=[10, 22, 44, 23, 4]
# i1=i
# print(i1)
#
# # j="Find the List of Words that are Longer than n from a given List of Words"
# # n=3;new_list=[]
# # text=j.split(" ")
# # for x in text:
# #     if len(x) > n:
# #         new_list.append(x)
# # print(new_list)
#
# z1=[1,2,3,4,5]
#
# z2=[5,6,7,8,9]
# res=False
# for i in z1:
#     for j in z2:
#         if i==j:
#             res= True
#         print(res)
#
# if res:
#     print("list has atleat one comman element")
# else:
#     print("list don't has any common element")
#
# abc=[7,32,81,20,25,14,23,27]
# ab=[i for i in abc if i%2!=0]
# print(ab)
#
# pqr=["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# random.shuffle(pqr)
# print(pqr)
#
# lis1=['T','u','t','o','r',' ','J','o','e','s']
# x=''.join(lis1)
# print(x)
#
# y=[20, 70, 30, 90, 10, 30, 90, 10, 80]
# m=y.index(30)
# print(m)
#
# Number = [10, 20, 30, 40]
# animal = ["Cat", "Dog", "Lion", "Ponda"]
# final=Number+animal
# print(final)
#
# import random
# animal = ["Cat", "Dog", "Elephant", "Fox", "Tiger", "Lion", "Ponda"]
# print(random.choice(animal))
#
#
''''tuple'''
# tup=(1)
# print(tup)
#
# t = (10,40,50,70,90)
# l=list(t)
# l.append(100)
# print(l)
#
# t = ('T', 'u', 't', 'o', 'r', ' ', 'J', 'o', 'e', 's')
# s=''.join(t)
# print(s)
#
# c=('w', 3, 'r', 'e', 's', 'o', 'u', 'r', 'c', 'e')
# print(c[3])
# print(c[-4])
#
# t = (2,34,45,6,7,2,4,5,78,34,2)
# count=t.count(2)
# print(count)
#
# ac=('T', 'u', 't', 'o', 'r', ' ', 'J', 'o', 'e', 's',8)
# print(8 in t)
#
# s=[12, 45, 87, 54, 89, 4]
# x=tuple(s)
# print(x)
#
# bb=(23, 45, 56, 68, 10, 45, 7, 9)
# b=list(bb)
# b.remove(56)
# print(b)
#
# v=(23, 45, 67, 78, 89, 90, 34, 56)
# x=v.index(78)
# print((x))
#
# a = ("Lion","Cat","Dog","Panda","Tiger","Fox")
# print(len(a))
#
# zz=( ("Name", "Ram"), ("Age", 23), ("City", "Salem"), ("Mark", 422) )
# z=dict(zz)
# print(z)
#
# l = [(10,30), (60,90), (20,50)]
# print(list(zip(*    l)))
#
# a = (23,45,67,78,89,90,34,56)
# print(a[::-1])
# b=reversed(a)
# print(tuple(b))
#
# zz=(22,)
# print(type(zz))
#
# t = (11, 22, 33, 44, 55)
# m,n,o,p,r=t
# print(m)
# print(n)
# print(o)
# print(p)
# print(r)

'''set'''
a={'T', True, 45, 23, 56, 'Joes', 45.6}
print(type(a))
for i in a:
 print(a)

 abc={"Lion", "Cat"}
 abc.update(['deer','beer'])
 print(abc)

 abc= {50, 20, 70, 60, 30}
 abc.remove(50)
 print(abc)

 a = {30, 40, 70, 20}
 b = {20, 50, 60, 40}

 c=a & b
 print(c)

 d=a.union(b)
 print(d)

 A = {80, 50, 20, 70, 40, 30}

 B = {50, 20, 90, 40, 10, 60}
 zz=a-b
 print(zz)

 a = {"Tutoe", "Joes"}
 b = {"Joes", "Tutoe"}
 a=b.copy()
 print(a)

 s = "TutorJoes"
 new=set(s)
 p=list(new)
 print(type(p))

 x = {10, 20, 30, 40, 50}
 y = [60, 70, 80, 90, 100]
 x.update(y)
 print(x)

 str = "Tutor Joes"
 c=0
 vowel=set("aeoiuAEIOU")
 for i in str:
     if i in vowel:
         c=c+1
print(c)