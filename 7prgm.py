#7a
list1=[1,2,4,3,8]
list2=[1,2,4,3,5]
print("the first list is:"+str(list1))
print("the second list is:",str(list2))
l1=len(list1)
l2=len(list2)
print("length of list1:",l1,"and length of list2:",l2)
if l1==l2:
    print("list are same length")
else:
    print("list are of different length")

#7b
list1=[1,2,4,3,8]
list2=[1,2,4,3,5]
print("the first list is:"+str(list1))
print("the second list is:",str(list2))
sum1=0
sum2=0
for x in range (0,len(list1)):
    sum1=sum2+list1[x]
print("sum of all elements in given list1:",sum1)
for x in range (0,len(list2)):
    sum2=sum2+list2[x]
print("sum of all elements in given list2:",sum2)
if(sum1==sum2):
    print("list sum to same value")
else:
    print("list are of different sum")


    #7c
list1=[1,2,4,3,8]
list2=[1,2,4,3,5]
print("the first list is:"+str(list1))
print("the second list is:",str(list2))
print("the values occur in both lists:")
for x in list1:
    if(x in list1 and x in list2):
        print (x)

