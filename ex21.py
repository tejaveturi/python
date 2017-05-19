def add(a,b):
    print " ADDing %d + %d" %(a,b)
    return a + b
def sub (a,b):
    print " sub %f -%f" %(a,b)
    return a-b
def mul (a,b):
    print "multipling %d * %d " % (a, b)
    return a * b
def div (a,b):
    print "divide %f / %f " % (a , b)
    return a / b
age = add (20 , 5)
height = sub (5.6 , 0.1)
weight = mul(50 ,25)
iq =div(20, 3)

print " age; %d height: %f weight: %d iq : %f" %(age, height, weight, iq)

