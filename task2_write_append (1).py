"""
Task 2: Write and Append Data to a File
Filename: task2_write_append.py
"""

import datetime
import sys

def write_and_append(output_path='output.txt', input_text=None):
    try:
        # If no input text provided, prompt user
        if not input_text:
            input_text = input('Enter some text to write to output.txt: ').strip()

        # Write initial content (this will overwrite existing file)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('--- File created by task2_write_append.py ---\n')
            f.write(f'User input: {input_text}\n')

        # Append additional content
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with open(output_path, 'a', encoding='utf-8') as f:
            f.write('--- Appended content ---\n')
            f.write(f'Appended on: {timestamp}\n')
            f.write('Thank you for using the program.\n')

        # Read and display final content
        print('\nFinal contents of output.txt:\n')
        with open(output_path, 'r', encoding='utf-8') as f:
            for lineno, line in enumerate(f, start=1):
                print(f"{lineno}: {line.rstrip()}")

    except Exception as e:
        print(f"An error occurred while writing/appending to {output_path}: {e}")


if __name__ == '__main__':
    # Support optional command-line argument for input text
    if len(sys.argv) > 1:
        input_text = ' '.join(sys.argv[1:])
    else:
        input_text = None
    write_and_append('output.txt', input_text)
