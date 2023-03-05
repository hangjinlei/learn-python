from array import array

x = 42
y = 206
if x == y:
    print("Success")

try:
    a = 10 / 0
except ZeroDivisionError as e:
    print("division by zero")
else:
    print("Success")

arr = array("d")
arr.append(1.0)
arr.append(2.0)
print(arr)
