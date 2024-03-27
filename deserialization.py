import json

emp="""{"eid":101,"enmae":"pooja"}"""
d=json.loads(emp)
print(d)

with open(r'C:\dwsample1-json.json','r') as fp:
    data2=json.load(fp)
    print(data2)