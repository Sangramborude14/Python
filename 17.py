def print_student_info(**kwargs):
    """
    Prints student details provided as keyword arguments in a formatted manner.
    """
    print("-" * 30)
    print("STUDENT RECORD")
    print("-" * 30)
    
    # Capitalizing the keys for better formatting
    for key, value in kwargs.items():
        formatted_key = key.replace("_", " ").title()
        print(f"{formatted_key:10}: {value}")
    
    print("-" * 30 + "\n")

if __name__ == "__main__":
    # Calling with all expected fields
    print("Demo 1: Full Details")
    print_student_info(name="Sangram Borude", age=21, grade="A", city="Mumbai")
    
    # Calling with partial fields
    print("Demo 2: Partial Details")
    print_student_info(name="John Doe", age=22)
    
    # Calling with extra/different fields (demonstrating **kwargs flexibility)
    print("Demo 3: Variable Fields")
    print_student_info(name="Alice Smith", city="Delhi", hobby="Coding", course="Python")
