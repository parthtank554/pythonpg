#Write a program to count the total number of digits in a number using a while loop.
#For example, the number is 75869, so the output should be 5
# Program = 1.6

n=int(input("Enter number: "))
count=0

while n!=0:
    n//=10
    count+=1

print(count)
