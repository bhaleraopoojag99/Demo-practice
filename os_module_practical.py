import os
print(os.getcwd())
print(os.chdir("D://"))
print(os.getcwd())
print(os.listdir("D://"))
print(os.chdir(r"C:\Users\ADMIN\PycharmProjects\pythonProject"))
print(os.getcwd())
# os.mkdir('pooja')
var=os.listdir("/")
print(var)
print(os.chdir(r"PycharmProjects\pythonProject\pooja"))
print(os.path.exists(r'C:\Users\ADMIN\PycharmProjects\pythonProject'))