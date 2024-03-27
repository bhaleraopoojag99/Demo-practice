# list=[10,20,30,40,50,60,70,80,90]
# new=[1,2,3,4]
# list.insert(0,new)
# print(list)
#
# list.insert(6,new)
# print(list)


#swapping 1st and last element
list1=[10,20,30,40,50,60,70,80,90]
list1[0],list1[-1]=list1[-1],list1[0]

print(list1[0])
print(list1[-1])

# swapping two list
l1=[10,20,30,40,50,60]
l2=[1,2,3,4,5,6]
print("before l1 was",l1)
print("before l2 was",l2)

l1,l2=l2,l1
print("after",l1)
print("after",l2)

#sum of all elements from list
l1=[10,20,30,40,50,60]
def add(l):
    c = 0
    for i in l1:
     c=c+i
    print(c)
add(l1)

#reverse the list
print(l1[::-1])


# number present or not in list
def exist_or_not(l):
    n=int(input("Enter the number"))
    for i in l1:
        if i == n:
            print("the given number exist")
            break
        else:
            print("the number is absent")
            break

exist_or_not(l1)

# count occurances
# def occurences(n):
#     occ=0
#     for i in l1:
#         if i==n :
#             occ+=1
#     return occ
# occurences(l1)


