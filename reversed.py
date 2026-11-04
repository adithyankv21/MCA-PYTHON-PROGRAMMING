x=int(input("enter the reversed number"))
rev=0
while x>0:
    rev=(rev*10)+(x%10)
    x=x//10
