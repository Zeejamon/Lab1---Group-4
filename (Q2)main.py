filename = input("Enter the name of the file: ")

with open(filename, 'r') as f:
    lines = f.readlines()

num_lines = len(lines)

while True:
    print(f"The file has {num_lines} lines.")
    line_num = input("Enter a line number (or 0 to quit): ")
    line_num = int(line_num)

    if line_num == 0:
        break
    elif 1 <= line_num <= num_lines:
        print(f"Line {line_num}: {lines[line_num-1]}")
    else:
        print(f"Invalid line number. Enter a number between 1 and {num_lines}.")