import test_all as ta
import functions470 as f470
#  N        B      start  finish       factors
# 221,      11,     15,     30      = 13,   17
# 493,      11,     23,     38      = 17,   29
# 61063,    5,      1880,   1900    = 227,  269
# 52907,    5,      100,    1000    = 277,  191
# 198103,   11,     1000,   3000    = 499,  397
# 2525891,  11,     1000,   20000   = 1637, 1543

N, B, I = 6754910601769419708731690214821789355427, 10**5, 10**9

primes = ta.primes_up_to_B(B)
non_residues = ta.compute_non_residues(primes)

factors = f470.quadratic_sieve(N, B, I, primes, non_residues, verbose=True)
print(factors)