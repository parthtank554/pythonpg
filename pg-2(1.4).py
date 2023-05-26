""""
Program = 1.4
Write a given output of the program in below:
if enter [2] = then output will be 2,4,6,8,10,12,14,16,18,20
"""
n = int (input("Enter Any Number: "))

no=n
for i in range (11):
    no = n * i
    if no == 0:
        print()
    else :
        print(no)