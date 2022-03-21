def fix(n):
    if(n>=0 and n<=9):
        return n
    else:
        sum=0
        while(n!=0):
            r=(n%10)
            sum=sum+r
            n=(n//10)
        return sum
num=int(input("enter the number:"))
d=fix(num)
if(d>=0 and d<=9):
    print(d)
else:
    m=fix(d)
    print(m)

