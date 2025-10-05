import math

def getDegGen(m):
    a = math.floor(math.log(2*m+1,2))
    if a%2==0:
        return 2**(a+1)
    if a%2==1:
        return 6*m+3-2**(a+1)

for m in range(50):
    print("("+str(m)+","+str(getDegGen(m))+")")

print("----------")

for m in range(50):
    print("("+str(m)+","+str(6*m+3-getDegGen(m))+")")
