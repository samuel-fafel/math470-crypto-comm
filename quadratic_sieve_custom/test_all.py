import time
import math
import functions470 as f470
import random
# 221,      11,     15,     30      = 13,   17
# 493,      11,     23,     38      = 17,   29
# 61063,    5,      1880,   1900    = 227,  269
# 52907,    5,      100,    1000    = 277,  191
# 198103,   11,     1000,   3000    = 499,  397
# 2525891,  11,     1000,   20000   = 1637, 1543

def primes_up_to_B(B):
    """Get all primes up to B using the Sieve of Eratosthenes"""
    print("Finding Primes")
    sieve = [True] * (B + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(B**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, B + 1, i):
                sieve[j] = False
    return [i for i, val in enumerate(sieve) if val]

def compute_non_residues(primes):
    print("Computing Non-Residues")
    non_residues = {}
    for p in primes:
        Z = random.randint(1, math.isqrt(p)+1)
        while f470.quadratic_residue(Z, p) != p - 1:
            #print(f"finding NR for {p}")
            Z = random.randint(1, math.isqrt(p)+1)
        non_residues[p] = Z
    return non_residues

def factor_N(N, B, interval, primes, non_residues, verbose):
    alternate = 0
    if not verbose: print(f"Factoring {N}")
    while interval < 10**10:
        factor = f470.quadratic_sieve(N, B, interval, primes, non_residues, verbose)
        if factor:
            return factor
        else:
            if not verbose: print(f"Unable to find enough relations with factor base at B = 10**{int(math.log10(B))} and interval of 10**{int(math.log10(interval))} [{alternate}]")
            if alternate % 3 == 0:
                interval *= 10
                alternate += 1
            else:
                B *= 10
                alternate += 1
    
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(c, p, q):
    modulus = (p - 1) * (q - 1)
    gcd, inverse, _ = extended_gcd(c, modulus)
    
    if gcd != 1:
        raise ValueError(f"The inverse does not exist since gcd({c}, {modulus}) != 1")
    
    # The modular inverse might be negative, so convert it to the positive equivalent
    return inverse % modulus

if __name__ == "__main__":
    print("----------------------------------------------------------------------------------")
    N1  = 221
    N2  = 493
    N3  = 61063
    N4  = 52907
    N5  = 198103
    N6  = 2525891
    N20 = 35437391370189380023 # 10**3, 10**6
    N30 = 403903264686388453744794079313 # 10**4, 10**7
    N40 = 6754910601769419708731690214821789355427 # 10**6, 10**8
    N50 = 60529141009038413034423166889017301527837910258131
    N60 = 133523995803370205942225812853710227025177081936429644652483
    crazy_N = 3426473875287793756703750981622962137419589116424756456135570641437827

    N_list = [N1, N2, N3, N4, N5, N6, N20, N30, N40, N50, N60, crazy_N]
    B_dict = {N1: 10**2,    N2: 10**2,  N3:10**2,   N4:10**3,   N5:10**4,   N6:10**4,
              N20:10**3,    N30:10**4,  N40:10**5,  N50:10**1,  N60:10**1,  crazy_N:10**1}
    
    I_dict = {N1: 10**2,    N2: 10**2,  N3:10**5,   N4:10**5,   N5:10**5,   N6:10**5,
              N20:10**6,    N30:10**7,  N40:10**8,  N50:10**1,  N60:10**1,  crazy_N:10**1}
    factor_dict = {}
    time_dict = {}
    primes = primes_up_to_B(10**7)
    non_residues = compute_non_residues(primes)
    print("----------------------------------------------------------------------------------")
    with open("factor_timing.csv", 'w') as file:
        header = "N, Factors, Time\n"
        file.write(header)
        for N in N_list[6:8]:
            B = B_dict[N]
            I = I_dict[N]
            
            start_time = time.time()
            factor_dict[N] = factor_N(N, B, I, primes, non_residues, verbose=True)
            end_time = time.time()
            
            runtime = end_time - start_time
            time_dict[N] = runtime
            
            file.write(f"{N}, {factor_dict[N]}, {time_dict[N]}\n")
            print(f"Factors: {factor_dict[N][0]} * {factor_dict[N][1]} == {N} = N --> {factor_dict[N][0] * factor_dict[N][1] == N}")
            print(f"\tFactoring {N} took {runtime:.4f} seconds to complete. (B=10**{int(math.log10(B))}, I=10**{int(math.log10(I))})")
            print("----------------------------------------------------------------------------------")

    p, q = factor_dict[N30]
    c = 65537
    inverse_c = mod_inverse(c, p, q)
    print(f"The inverse of {c} mod {(p-1)*(q-1)} is {inverse_c}")
