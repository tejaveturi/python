from sys import argv
script, input_file = argv
def print_all (f):
    print f.read()

def rewind (f):
    f.seek(0)

def print_a_line(lcount, f):
    print lcount, f.readline()

current_file = open(input_file)

print "printing the whole file:\n"
print_all(current_file)

print "\n now let's rewind, back to starting\n"

rewind (current_file)

print "\nprinting 3 lines\n"
current_line = 1

while (current_line<=3):
    print_a_line(current_line, current_file)
    current_line = current_line + 1





