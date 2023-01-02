def rec(a):
    if a==0:
        return 1
    else:
        return a*(rec(a-1))
c=int(input("  >>>>  "))
print(c)