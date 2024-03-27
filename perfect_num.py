def perfect_no():
    num=int(input("Enter the number you want to check"))
    s=0
    for i in range(1,num+1):
        if num%i==0:
            s=s+i
    if s==num:
        print(num,"is perfect number")
    else:
        print(num,"not perfect number")

perfect_no()
