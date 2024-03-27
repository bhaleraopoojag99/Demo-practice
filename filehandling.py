
# fp=open('intro.txt','r')
# mob=[]
# email=[]
# data=fp.readlines()
# for line in data:
#     sep=line.split()
#     for i in sep:
#         if i.isnumeric():
#             fp1=open('new.txt','w')
#             fp1.writelines(i)

# import csv
# with open(r'C:\Users\ADMIN\Downloads\Bengaluru_House_Dataaws.csv')as fp:
#     re=csv.reader(fp)
#     for i in re:
#
#       with open('new.txt','w')as fp1:
#        we=csv.writer(fp1)
#        we.writerow(['abc','pqr'])
#        we.writerows([i])

# import csv
# marks=[('Seema',22,45),('Anil',21,56),('Mike',20,60)]
# fp=open('marks.csv','w')
# obj=csv.writer(fp)
# for i in marks:
#  obj.writerow(i)
# csvfile.close()

import csv
marks=[('Seema',22,45),('Anil',21,56),('Mike',20,60)]
fp=open('mm.csv','w')
we=csv.writer(fp)
for i in marks:
    we.writerows([i])
fp.close()