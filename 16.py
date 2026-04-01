def square(x):
    """Calculates the square of a number."""
    return x * x

def cube(x):
    """Calculates the cube of a number."""
    return x * x * x

def double(x):
    """Calculates double of a number."""
    return x * 2

# Storing functions in a list (Functions as data)
functions_list = [square, cube, double]

def demonstrate_functions_as_data():
    number = 5
    print(f"Number to process: {number}")
    print("-" * 25)
    
    # Loop through the list and call each function
    for func in functions_list:
        # func.__name__ gets the name of the function
        result = func(number)
        print(f"Calling {func.__name__:8}: {result}")

if __name__ == "__main__":
    demonstrate_functions_as_data()
