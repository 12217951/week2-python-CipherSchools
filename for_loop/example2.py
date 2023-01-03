#ask user a number and calculate the sum of digits
total=0
num=input("enter a number: ")
for i in range (0,len(num)):
    total+=int(num[i])

print(total)