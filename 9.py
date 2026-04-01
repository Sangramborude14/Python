items = ["cat", "dog", "cat", "bird", "dog", "cat"]

unique = {}
for item in items:
    if item in unique:
        unique[item]  += 1
    else :
        unique[item] = 1

print(unique)