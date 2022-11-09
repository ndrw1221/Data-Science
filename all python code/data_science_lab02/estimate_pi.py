import math
def estimate_pi():
    k = 0
    s = 0.0
    t = 0.0
    while True:
        t = (math.factorial(4*k)*(1103+26390*k))/(math.pow(math.factorial(k), 4)*math.pow(396, (4*k)))
        s += t
        k += 1
        if t < 1e-15:
            break
    
    s *= (2*math.sqrt(2))/9801
    return 1/s

if __name__ == '__main__':    
    print(estimate_pi() == math.pi)
    print(estimate_pi())
    print(math.pi)