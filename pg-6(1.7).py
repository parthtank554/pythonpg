#Program = 1.7 
#Write a program to use for loop to print the following reverse number pattern.
""""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
n = int (input("Enter Any Number : "))

for i in range (0, n+1):
    for j in range (n-i,0,-1):
        print(j, end=" ")
    print()