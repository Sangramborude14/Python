first_name = input("Enter your first name")
last_name = input("Enter your last name")
full_name = first_name + " " + last_name

print(full_name)
l = len(full_name)
s = str(full_name)

print(s)
print(l)
u = full_name.upper()
print(u)

swap = full_name.swapcase()
print(swap)

replace = full_name.replace(full_name, "Darth Vader")
print(replace)

case = full_name.casefold()
print(case)





