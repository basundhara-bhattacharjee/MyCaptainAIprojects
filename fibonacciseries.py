n=int(input("Please enter the number of terms: "))
i=0
j=1
count=0
if n<=0:
    print("Please enter a whole number")
elif n==1:
    print("The fibonacci series is: ",i)
else:
    print("The fibonacci series is:")
    while count<n:
        print(i)
        m=i+j
        i=j
        j=m
        count=count+1
