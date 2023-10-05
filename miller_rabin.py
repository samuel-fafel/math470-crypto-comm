import random
from eea import eea_gcd

def MillerRabin(n, a, k, q, verbose=True):
    if n % 2 == 0:
        if verbose: print(f"{n} is even --> Composite")
        return [2, n//2]
    
    d = eea_gcd(a, n, verbose=False)
    if 1 < d and d < n:
        if verbose: 
            print(f"1 < GCD({a}, {n}) = {d} < {n}")
            print(f"\t{n} / {a} = {n/a}")
            print(f"\t{n} is a composite of {a} and {n//a}")
        return [a, n//a] # n/a is an integer > 1
    
    a_new = pow(a, q, n)
    for i in range(k):
        if verbose: print(f"{a}^({q}*(2^{i})) \t = {a_new} mod {n}")
        if a_new == 1 or a_new == n-1:
            return [] # Not composite (of the numbers checked)
        a_new = pow(a_new, 2, n)

def isComposite(n, max_a, verbose=False):
    q = n-1
    k = 0
    while q % 2 == 0: # n-1 = 2^k * q
        q = q//2
        k += 1
    if verbose:
        print(f"n = {n}")
        print(f"n-1 = {n-1} = 2^{k} * {q}")
        print(f"k = {k}, q = {q}")

    composite = "Unknown"
    for a in range(2, max_a): # Test all numbers (2, 3, ... , max_a)
        composition = MillerRabin(n, a, k, q, verbose=verbose)
        if (composition):
            composite = f"Yes: {composition}"
            return composition
    if verbose:
        print(f"Is {n} composite? {composite}\n")
    return None

if __name__ == '__main__':
    n_list = [1105, 294409, 294439, 118901509, 118901521, 118901527, 118915387]
    for n in n_list:
        max_a = n//100 # Need to check a maximum of 25% of (2, 3, ... , n-1), so more than n//4 is unneccessary
        print("------------------")
        #print(f"Composition of {n} between 2 and {max_a}: {isComposite(n, max_a, False)}")

isComposite(69, 65*10, True)
        
