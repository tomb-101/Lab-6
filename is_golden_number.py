def is_golden_number(n):
    # function implementation ...
    boolean=False
    while n>1 and n<1000:
        for a in range(1, n+1):
            b=n-a
            if ((a*b)/1000)==1:
                boolean=True
        break
    return boolean

print(is_golden_number(65))