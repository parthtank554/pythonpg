#Program - 1.12
#Display Fibonacci series up to 10 terms

n=int(input("Enter terms: "))
n1=0
n2=1
count=0

if n<=0:
    print("Please enter positive values only")
else: 
    print("Fibonacci series are: ")
    for i in range(0,n):
        print(n1)
        n=n1+n2
        n1=n2
        n2=n
        count+=1
