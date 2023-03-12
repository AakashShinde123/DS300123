def prime(a):
    if a<2:
        return False
    for i in range (2,a):
        if a % i == 0:
            return False
    return True
def Twin(b):
    for i in range(b + 1):
        j = i+2
        if (prime(i) and prime(j)):
            print("{0} and {1}".format(i,j))
Twin(20)            
