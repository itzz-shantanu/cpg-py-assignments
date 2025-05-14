a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

max_num = a
if b > max_num:
    max_num = b
if c > max_num:
    max_num = c

print("Maximum number is:", max_num)