import math
def mCounterexample(m):
    bound = math.floor(math.log(m,3)+1)
    for a in range(bound+1):
        mod = m % 3**a
        if mod >= 3**(a-1) and mod <= 2*3**(a-1)-1:
            return True, a
    return False, 0

for m in range(1,100):
    print("------------" + str(m) + "------------")
    counter, a = mCounterexample(m)
    if counter:
        print(a)
    else:
        print("nah")
    
