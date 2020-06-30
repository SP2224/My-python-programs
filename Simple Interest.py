def si(p,t,r):
    print("the principal value is ",p)
    print("the rate of interest is ",r)
    print("the time is ",t)
    si=(p*t*r)/100
    print("the simple interest is",si)
    return si
si(80,5,6)