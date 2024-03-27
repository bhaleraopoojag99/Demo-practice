with open('intro.txt','r+')as fp:
    data=fp.read()
    print(data)

with open('move_content.txt','w+')as fp1:
    fp1.write(data)
    fp1.truncate(0)


