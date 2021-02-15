from sys import argv

script, input_file = argv
# Takes a file object and prints it's content as a string
def print_all(f):
    print(f.read())
# Sets pointer to start of file
def rewind(f):
    f.seek(0)
# Prints the first variable and the current line of the file f
def print_a_line(line_count, f):
    print(line_count, f.readline())
# Saves input file in variable
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)  # current_line = 1

current_line += 1
print_a_line(current_line, current_file)  # current_line = 2

current_line += 1
print_a_line(current_line, current_file)  # current_line = 3

current_file.close()
