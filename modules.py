def sum(y,d):
    return y + d


def subtraction(d,r):
    return d - r

def multiply(x,y):
    return x * y

def look(t):
    return t % 2

ans= look(int(input("t: ")))

if ans % 2==0:
 print("even")

elif ans != 0:

 print("odd")
