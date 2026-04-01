def outer():
    msg = "Hello"
    def inner():
        print(msg)
    inner()

outer()

text = "racecar"

if text == text[::-1]:
    print(f"is a pallidrome")
else:
    print(f"not a pladinfrime")


