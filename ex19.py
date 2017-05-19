def cnc(chees, crack):
    print("you have %s chees & %s crack") %(chees, crack)

print ("we can directly give argument values")
cnc(25, 30)
print("we can use variables to pass like argumets ")
ch = 2500
cr = 3000
cnc (ch, cr)
print ("we do math in arguments")
cnc(3*6, 20/5)
print("we can combine variable and math too")
cnc(ch+1000, cr+1000)
 
