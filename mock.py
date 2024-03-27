# def palin():
#     given_str=input("Enter the string")
#     reverse=""
#     for i in given_str:
#        reverse=reverse+i
#     if given_str==reverse:
#         print("the given string is palin")
#     else:
#         print("the given string in not palin")
# palin()

# r=[234,235,34,423,3442,[345,657,2342,6574],54,356,234,2]
# for i in r:
#     print(i)


# p='dfhdjfnkdmfvdncdbdhbcdggndkfkdmfcdm'
# c=0
#
# for num in range(1,11):
#     for i in range (1,11):
#         print(num*i,end='|')
#     print()

def f(x):
   x=x+1
   print('in f(x) : x=',x)
   return x

x=3
z=f(x)
print( 'scope of z=',z)
print( 'scope of x=',x)


# a_dict={1,2,3,4,5,6,7,8}
# x={i:i*i*i for i in a_dict}
# print(x)
name=['Asawari','Pooja','Mansi','Manisha','Kranti','Sakshi','Anuj','Asmita']
x={i:len(i) for i in name }
print(x)

p=[51,2065,98,63,54,75,95,'pooja','asawari','manisha']
print(lambda x: (x)==int,p)


