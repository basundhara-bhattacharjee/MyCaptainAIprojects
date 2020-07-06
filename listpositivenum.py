list=[]
n=int(input("Enter the number of elements:"))
for i in range(0,n):
    ele=int(input("Enter element "))
    list.append(ele)
print("list1:",list)
p=[]

for j in list:
    if j>0:
        p.append(j)
print("The positive numbers present in the above list :",p)
        
