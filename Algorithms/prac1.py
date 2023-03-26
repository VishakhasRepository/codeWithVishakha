

def compareTriplets(a, b):
    apoint = 0
    bpoint = 0
    for i in range(0,3):
        if a[i]>b[i]:
            apoint+=1
        elif b[i]>a[i]:
            bpoint+=1
    return [apoint,bpoint]



a = [17, 28, 30]
b = [99, 16, 8]
print(compareTriplets(a,b))