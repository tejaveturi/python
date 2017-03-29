from sys import argv
script, file_name = argv

print "erasing the file data %s" % file_name
print "for yes = ENTER :\t no = ^+c"
raw_input("?")
f1 = open(file_name, "r+")
f1.truncate()

l1=raw_input(" your name: ")
l2=raw_input("your age:" )
l3=raw_input("number: ")

f1.write(l1)
f1.write("\n")
f1.write(l2 )
f1.write("\n")
f1.write(l3 )



print " your info is stored in the file"
print " opening the file "

f1.close()

f2=open(file_name,"r")
print f2.read()
