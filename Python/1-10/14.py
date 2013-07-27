import math

def Collatz(n,d):
    cur = n
    count = 0
    while cur > 1:
        if cur in d.keys():
            count += d[cur]
            break
        elif ((cur%2)==0):
            # print count, "EVEN", cur
            cur *= 0.5
        elif ((cur%2)==1): 
            # print count, "ODD", cur
            cur = 1 + (3*cur)
        count += 1
    return count

def isprime(n):
    primes = [2,3]
    for i in xrange(5,int(math.ceil(math.sqrt(n)))):
        composite = False
        for p in primes:
            if i%p==0:
                composite = True
                break
        if not composite:
            primes.append(i)
    for p in primes:
        if n%p==0:
            return False
    return True

def main():
    d = {}
    m = 0
    for i in xrange(500000,1000000):        
        if isprime(i):
            if (isprime(i%500)): print "...", str(100.0 * float(i) / float(1000000))+"%"
            current = Collatz(i,d)
            if (current > m):
                m = current
                print m
                d[i] = current
    print m

main()
