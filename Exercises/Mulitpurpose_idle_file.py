from sys import argv

script, filename = argv

print(f"We're going to read {filename}.")
print("If you don't want that, it CTRL-C (^C).")
print("If you do want that, hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'r')


print("Now I'm going to read and print three lines.")


print(target.read())
target.seek(6)
print(target.read(10))


print("And finally, we close it.")
target.close()
