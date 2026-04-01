length = int(input("no of numbers"))
tuple1 = tuple()
for x in range(1,length + 1):
    char = int(input("enter the number"))
    tuple1 += (char,)

add  = 0
for char in tuple1:
    add += char
print(f"addition : {add}")
print(f"maximum: {max(tuple1)}")
print(f"minimum: {min(tuple1)}")

