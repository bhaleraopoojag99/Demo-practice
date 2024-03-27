p = [34,78,634,8,74,5,867,45,876,45,86,45]
even=[]
for i in p:
  if i%2==0:
      even.append(i)
print(even)

var=[i for i in p if i%2==0]
print(var)

abc=[10,20,20,30,45,60,20,10]
dup=[]
for i in abc:
    if i not in dup:
        dup.append(i)
print(dup)

# dupl=[dup.append(item) for item in abc if item not in dup]
# print(dupl)

var1=['asdfasdf', 546456, 6546, 876, 345, 876, 34, 856, 'sdfg', 'fdg', 'sdgfd', 54457546]
lst=[i for i in var1 if str(i).isnumeric()]
lst1=[i for i in var1 if isinstance(i,int)]
print(lst1)
print(lst)
print()

p = ['python','java','hadoop','pyspark','ml']
showp=[len(p) for i in p]
print(showp)

show2={i:len(i)for i in p}
print(show2)


p = [{'name':'keshav','id':101},{'name':'Rakesh','id':205},{'name':'Rahul','id':250}]
dis=[i.get('name') for i in p]
print(dis)

'''Lambda function'''
print((lambda x,y:x+y)(2,3))
#x2+2xy+y2

print((lambda x,y:x**2+2*x*y+y**2)(2,3))

'''map function'''
p = [34,7,4,5,76,345,786,34,78,64,5]
def srq(e):
    return e**2
v1=list(map(srq,p))
print(v1)

email = ['test@gmail.com','python@yahoo.com','ml@rediffmail.com']
def user(e):
    val=e.split('@')[0]
    return val
v2=list(map(user,email))
print(v2)

print(tuple(map(lambda e:e.split('@'),email)))

p = ['arun.patil@gmail.com','suresh.sharma@yahoo.com']
def sep(p):
    p1=p.split('@')[0]
    return p1
print(list(map(sep,p)))

p = [34,7,4,5,76,345,786,34,78,64,5]
def even(n):
    if n%2==0:
        return n
print(list(filter(even,p)))

print(list(filter(lambda x:x%2,p)))


empids = ['sdfsdf',545,'sadfsd',654654,546,345,87,345,8,3456,'dfgd','sdgfdf']

def sep_int(n):
    if str(n).isnumeric():
        return n

print(list(filter(sep_int,empids)))

print(filter(lambda lett:str(lett).isnumeric(),empids))

p = ['345','654','6354','325','7654','345','654','3456']
print(list(map(lambda x:int(x),p)))


p = ['arun.patil@gmail.com','suresh.sharma@yahoo.com']
def fname(e):
    ret=e.split('@')[0]
    return ret
print(list(map(fname,p)))
print(list(map(lambda x:str(x).split('@')[0],p)))

'''generator'''
def generator():
    for i in range(11):
        yield i
print(generator())