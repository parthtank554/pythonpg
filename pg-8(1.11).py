"""
Program - 1.11
Write a program to display all prime numbers within a range:
"""

lower = int(input("Enter any number: "))
higher = int(input("Enter any number: "))
print("Prime number between",lower,"And",higher,"Are: ")

for i in range(lower,higher+1):
    if i > 1:
        for j in range(2, i):
            if(i%j)==0:
                break
            else:
                print (i)