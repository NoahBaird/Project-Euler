from math import sqrt

def checkIfDone(num):
    if num == 1:
        return True
    return False

def IsPrime(num):
    for i in range(2, int(sqrt(num))):
        if num % i == 0:
            return False
    return True

def findLargestPrimeFactor(num):
    done = False
    largestFactor = 1
    
    while num % 2 == 0:
        num = num / 2
        largestFactor = 2
        
    done = checkIfDone(num)

    while num % 3 == 0:
        num = num / 3
        largestFactor = 3
        
    done = checkIfDone(num)
    
    iterator = 1

    while not done:
        posPrime1 = iterator * 6 - 1
        posPrime2 = iterator * 6 + 1

        if IsPrime(posPrime1):
            while num % posPrime1 == 0:
                num = num / posPrime1
                largestFactor = posPrime1
        if IsPrime(posPrime2):
            if num % posPrime2 == 0:
                num = num/posPrime2
                largestFactor = posPrime2

        done = checkIfDone(num)
        iterator += 1

    return largestFactor


print findLargestPrimeFactor(600851475143)
