"""
Task 1: Read a File and Handle Errors
Filename: task1_read_file.py
"""

def read_sample_file(filepath='sample.txt'):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            print(f"Contents of '{filepath}':\n")
            for lineno, line in enumerate(f, start=1):
                print(f"{lineno}: {line.rstrip()}" )
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found. Please make sure it exists in the script directory.")
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")


if __name__ == '__main__':
    # You can change the filename here if needed
    read_sample_file('sample.txt')
