import copy

global new



def findCoeff(dimens):
    if dimens==0:
        print("wffda" + str(dimens))
        newer = copy.copy(new)
        lis.append(newer)
        print(lis)

    elif dimens!=0:
        for i in range(3):
            new.append(i)
            print("wffda" + str(dimens))
            print(new)
            findCoeff(dimens-1)
            new.pop(len(new)-1)
            
    return lis

new = []
lis=[]
print(findCoeff(3))
