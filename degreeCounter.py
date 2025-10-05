import math

def bigA(m):
    Thing = -1
    for i in range(m+1):
        mod = m % 3**i
        if mod >= 3**(i-1) and mod <= 2*3**(i-1)-1:
            Thing = i
    return Thing

def getDegGen(m):
    a = bigA(m)
    if a>-1:
        #print(a)
        k = math.floor(m/(3**a))
        #print(k)
        b = (2*m+1-(3**a)*(2*k+1))/2
        if b<0:
            b=0
        #print(b)
        return (3*k+1)*(3**a)+6*b
    else:
        return 3*m+1

for m in range(50):
    print("("+str(m)+","+str(getDegGen(m))+")")

print("----------")

for m in range(50):
    print("("+str(m)+","+str(6*m+3-getDegGen(m))+")")
