A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}

print(A & B)#intersection
print(A | B)#union
print(A - B)#diffrence
print(A ^ B)#symmetric difference

d1 = {'name': 'Alice', 'age': 20, 'city': 'Delhi'}
d2 = {'age': 22, 'grade': 'A', 'city': 'Mumbai'}

merged_dict = d1 | d2
print(f"Merged Result: {merged_dict}")

