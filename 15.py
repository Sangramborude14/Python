def read_file(filename):
    """
    Opens and reads a file, counting the number of lines and words.
    
    Args:
        filename (str): The name/path of the file to be read.
        
    Returns:
        tuple: (line_count, word_count) or (None, None) if the file is not found.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            
            # Resetting pointer if needed, but we already have lines in memory
            # Word count: flattening all lines and splitting
            content = "".join(lines)
            word_count = len(content.split())
            
            return line_count, word_count
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None, None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None

# Example Usage
if __name__ == "__main__":
    test_filename = "example.txt"
    
    # Create a dummy file for testing if it doesn't exist
    import os
    if not os.path.exists(test_filename):
        with open(test_filename, "w", encoding='utf-8') as f:
            f.write("Hello world!\nThis is a test file.\nPython is great.")
            print(f"Created '{test_filename}' for testing.\n")

    lines, words = read_file(test_filename)
    
    if lines is not None:
        print(f"File: {test_filename}")
        print(f"Total Lines: {lines}")
        print(f"Total Words: {words}")
    
    # Test for non-existent file
    print("\nTesting for FileNotFoundError:")
    read_file("non_existent_file.txt")
