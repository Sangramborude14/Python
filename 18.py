def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            line_count = len(lines)
            
            content = "".join(lines)
            word_count = len(content.split())

            return line_count, word_count
    
    except FileNotFoundError:
        print(f"the file was not found")
        return None, None
    except Exception as e:
        print(f"an unexpected error occured: {e}")
        return None, None

if __name__ == "__main__":
    test_filename = "example1.txt"

    import os
    if not os.path.exists(test_filename):
        with open(test_filename, "w", encoding='utf-8') as f:
            f.write("hello world")

    lines, words = read_file(test_filename)

    if lines is not None:
        print(f"Lines: {lines}")
        print(f"Words: {words}")
