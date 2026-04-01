x = 10
def change():
    global x
    x = 50
    print(f"Inside function: {x}")
change()
print(x)

#local and global variable

text = "python"
print(text.upper())
print(len(text))
print(text)
print(text[::-1])
