"""
Program - 1.17
Write a program to calculate the sum of series up to n term. For example, if n =5 the series will become
2 + 22 + 222 + 2222 + 22222 = 24690

"""
n=int(input("Enter the Term: "))
b=0
sum=0
for i in range(1,n+1):
        b=(b*10)+n-3
        sum+=b
        print(b,end=" ")
print()
        
print("sum is: ",sum)    
