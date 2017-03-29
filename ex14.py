from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s I am %s" % (user_name, script)
print" where do you live %s" %user_name
live = raw_input(prompt) 
print " do you like me %s " % user_name
like = raw_input(prompt)
print "what computer do you have %s" % user_name
computer = raw_input(prompt) 

print """ your name is %s,
you said %s about liking,
you live in %s, 
you have %s computer""" % (user_name, like, live, computer)

