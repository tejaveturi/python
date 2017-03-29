from sys import argv
script, filename = argv
f1= open(filename)
print "here is your file %s:" % filename
print f1.read()

file_again= raw_input("type file name again \n")
f2=open(file_again)
print f2.read()


