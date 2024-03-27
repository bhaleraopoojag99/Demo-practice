'''Decorators are those take a function  adds some functionality to it and returns it'''

# def make_pretty(fun):
#     def inner():
#         print("*"*20)
#         fun()
#         print("*" * 20)
#     return inner
# @make_pretty
# def ordinary():
#     print("I am in ordinary ")
#
# ordinary()


# def smart(fun):
#         def inner(x,y):
#             print("I am going to divide", x ,"&", y)
#             if y==0:
#                 print("oops we can't divide")
#             return fun(x,y)
#         return inner
#
#
#
# @smart
# def divide(a,b):
#     return(a/b)
#
# divide(2,0)

#swapping of numbers


# def outer(div):
#     def inner(x,y):
#         if x<y:
#             x,y=y,x
#             return div(x,y)
#     return inner
#
# @outer
# def div(a,b):
#     print(a/b)
#
# div(2,3)


# def decor(fun):
#     def inner():
#         print("*"*100)
#         fun()
#         print("*"*100)
#     return  inner
#
# @decor
# def show():
#     print("welcome")
# @decor
# def disp():
#     print("normal display")
#
# show()
# disp()



def decor(fun):
    def inner():
        print("*"*10)
        fun()
        print("*"*10)
    return inner
@decor
def show():
    print("show")

show()
