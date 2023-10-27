import math
import sympy as sp
from sympy import isprime
import numpy as np
from itertools import combinations
import helpers as hp
import random

def quadratic_residue(a,N):
    Q = (N-1) // 2
    x = 1
    a = a % N
    while Q != 0:
        if Q % 2 == 0:
            a = (a**2) % N
            Q //= 2
        else:
            Q -= 1
            x = (x*a) % N
    return x

def factor_base(N, B, prime_list):
    """Returns B-smooth factor base if one exists"""
    limit = int(B/math.log(B))
    primes = prime_list[:limit]
    base = []
    
    for p in primes:
        if quadratic_residue(N, p) == 1:
            base.append(p)
    return base

def Shanks_Tonelli(n, p, Z):
    """ Shanks-Tonelli Algorithm"""
    if quadratic_residue(n, p) != 1:
        print("not a quadratic residue (mod p)")
        return None
    q = p - 1
    s = 0
    
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        r = pow(n, (p + 1) // 4, p)
        return r, p-r
    elif s == 2:
        if pow(n, q, p) == 1:
            r = pow(n, (q + 1) // 2, p)
            return r, p-r
        else:
            R = pow(n*Z*Z, (q+1)//2, p)
            r = R * pow(Z, -1, p) % p
            return r, p-r
            
    z = Z
    x = pow(z, q, p)
    y = pow(n, (q + 1) // 2, p)
    z = pow(n, q, p)

    t2 = 0
    while (z - 1) % p != 0:
        t2 = (z * z) % p
        for i in range(1, s):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(x, 1 << (s - i - 1), p)
        y = (y * b)
        x = (b * b)
        z = (z * x)
        s = i
    
    y = y % p
    x = x % p
    z = z % p

    return (y,p-y)

def find_smooth(N, interval, base, non_residues, verbose=True):
    """Finds B-smooth numbers using sieve"""
    start = math.isqrt(N)
    finish = start + interval
    if verbose: print("Generating Sieve Start")
    sieve = [(t*t - N) for t in range(start, finish)]
    length = len(sieve)
    if verbose: print("Copying Sieve")
    sieve_preserve = sieve.copy()

    x_vars = []
    smooths = []
    if verbose: print ("Sieving")
    for p in base:
        Z = non_residues[p]
        while p - 1 != quadratic_residue(Z, p):
            if verbose: print("Finding new NR")
            Z = random.randint(1,p)
        residues = Shanks_Tonelli(N, p, Z)
        #if verbose: print(f"Found residues: {residues}")
        for r in residues: # Implement sieve
            for i in range((r-start) % p, length, p): # Skip every p terms 
                while sieve[i] % p == 0: # Keep dividing until no more prime powers
                    sieve[i] //= p
                if sieve[i] == 1:
                    x_vars.append(i + start)
                    smooths.append(sieve_preserve[i])

    return smooths, x_vars
               
def quadratic_sieve(N,B,interval, primes, non_residues, verbose=True):
    if isprime(N): # N is prime
        if verbose: print(f"{N} is prime")
        return ()
    
    if isinstance(math.sqrt(N), int): # N is a perfect square
        return math.isqrt(N)
    
    # Otherwise...
    if verbose: print(f"Factor N = {N}\tB = 10**{int(math.log10(B))}\tI = 10**{int(math.log10(interval))}")
    
    if verbose: print(f"Generate {B}-smooth factor base")
    base = factor_base(N, B, primes)

    if verbose: print(f"Find {len(base)} {B}-smooth relations")
    smooths, x_vars = find_smooth(N, interval, base, non_residues, verbose)
    
    # If number of relations < size of the factor base, not enough smooth numbers
    print(f"Size of Base: {len(base)}, Size of Smooths: {len(smooths)}")
    if len(smooths) < len(base):
        print(f"Unable to find enough relations with factor base at B = 10**{int(math.log10(B))} and interval of 10**{int(math.log10(interval))}")
        return ()
    
    if verbose: print("Building matrix from exponents")
    square, E = hp.build_matrix(smooths, base)

    if square: # If the matrix is square, E is returned as int from build_matrix()
        x = smooths.index(E)
        factor = math.gcd(x_vars[x] + math.isqrt(E), N)
        factors = (factor, N//factor)
        if verbose: print(f"Found a  Square! Factors: {factor} * {N//factor} == {N} --> {factor * N//factor == N}")
        return factors
    
    if verbose: print("Gaussian Elimination")
    sol_rows, marks, M = hp.gauss_elim(E) #solves the matrix for the null space, finds perfect square
    if verbose: print("Solve Rows")
    solution_vec = hp.solve_row(sol_rows, M, marks, 1)
    
    if verbose: print("Congruence of Squares")
    factor = hp.solve(solution_vec, smooths, x_vars, N) #solves the congruence of squares to obtain factors

    for col_index in range(1,len(sol_rows)):
        if (factor == 1 or factor == N):
            if verbose: print("Didn't work. Trying different solution vector...")
            solution_vec = hp.solve_row(sol_rows, M, marks, col_index)
            factor = hp.solve(solution_vec, smooths, x_vars, N)
        else:
            factors = (factor, N//factor)
            if verbose: print(f"Found factors: {factor} * {N//factor} == {N} --> {factor * N//factor == N}")
            return factors
            

    
    
    
    
    