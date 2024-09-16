x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))
a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
if x!=y and a!=b:
    print("Both numbers are equal")
elif x==y and a!=b:
    print("Only first numbers are equal")
else:
    print("Only last numbers are equal")
