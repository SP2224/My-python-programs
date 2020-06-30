def ci(p,r,t):
    print("the principal value is",p)
    print("the rate of interest is",r)
    print("the time required is",t)
    ci=p*(pow((1+r/100),t))
    print("the compund interest is ",ci)
ci(1200,2,5.4)