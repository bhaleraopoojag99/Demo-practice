import json
emp={'eid':101,'ename':'pooja','phone':45231}
js=json.dumps(emp)
print(js)

with open('emp1.json','w')as fp:
    json.dump(emp,fp)