a = input ("구구단 몇단 : ")
a  = int(a)
for i in range(1, 10):
    res = a * i
    print ("{0} x {1} = {2} ".format(a, i, res ) )
    print (a, " x ", i, " = ", a*i)
