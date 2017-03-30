from sys import argv
from os.path import exists

script, from_file, to_file = argv

print ("copy from %s to %s") % (from_file, to_file)
infile = open(from_file,'r')
indata = infile.read()
print (" the input file is %s long") % len(indata)
print ("Does output file exists %s")% exists(to_file)
print (" you want to continu press enter else CTL+C")
raw_input()
outfile = open(to_file,'w')
outfile.write(indata)
outfile.close()
infile.close()
print ("all done check file THANK YOU")
