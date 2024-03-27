#serializatio
import json
name={'eid':101,'ename':'pooja'}
data=json.dumps(name)
print(data)


name="""{'eid':101,'ename':'pooja'}"""
with open('ser_des.json','w')as fp:
    d1=json.dump(name,fp)
    print(d1)

name='''{"eid":1001,"ename":"abc"}'''
dd=json.loads(name)
print(dd)

with open('ser_des.json','r')as fp:
    daa=json.load(fp)
    print(daa)