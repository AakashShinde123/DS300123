a = [(2,5),(1,2),(4,4),(2,3),(2,1)]
for i in range(len(a)):
    for j in range(len(a)):
        if a[i][1]<a[j][1]:
            a[i],a[j] = a[j],a[i]
print(a)            
