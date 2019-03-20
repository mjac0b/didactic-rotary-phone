#"If" Statements

def maxMin(a,b,c):
    if a > b or b == int(c):
        print(str(c) + " is the max")

    elif b > a and b < int(c):
        print(str(b) + " is the median value")

    else:
        print(str(a) + " is the min value")

maxMin(10, 20, "25")