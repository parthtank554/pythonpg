""""
Program = 1.3 
Calculate the sum of all numbers from 1 to a given number
if enter 10 then output will be 55.
"""


n = int(input("Enter Any Number: "))
res = 0

for i in range (1, n+1):
    res = res + i

print(res)