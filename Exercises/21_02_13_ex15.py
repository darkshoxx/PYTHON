# Importing the argv function from the sys module
from sys import argv
# Unpack argv into 2 variables
script, filename = argv
# Put file in variable called txt
txt = open(filename)
# Printing file name in a formatted string
print(f"Here's your file {filename}:")
# Printing the content of the file as a string
print(txt.read())
# Printing a string
print("Type the filename again:")
# Prompting the filename of a file that is to be printed
file_again = input('> ')
# Saving file in new variable
txt_again = open(file_again)
# Printing content of new file as string
print(txt_again.read())
txt.close()
txt_again.close()
