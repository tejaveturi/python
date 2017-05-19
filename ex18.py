def inf(*a):
    a1, a2, a3 = a
    print ("a1: %s, a2: %s, a3: %s") %(a1, a2, a3)
def two(a, b):
    print ("a: %s, b: %s") %(a, b)
def one(a):
    print ("only one %s") %a
def none():
    print ("no arguments here sorry")
inf("hello", "world", "whatsup")
two(234, 324)
one("haha")
none()
