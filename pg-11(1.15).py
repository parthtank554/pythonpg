"""
Program = 1.15
Use a loop to display elements from a given list present at odd index
positions Given: my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
Expected output: 20 40 60 80 100
"""
lst1=[10, 20, 30, 40, 50, 70, 60, 80, 90, 100]

for i in lst1:
    if i % 2 == 0:
        print(i,end=" ")
