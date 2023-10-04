import math

def order(order_of: int, p: int) -> int:
    for x in range(1, p):
        test: int = (order_of ** x) % p
        if ((test) == 1): return x
    return -1

def fastpow(base: int, power: int, mod: int) -> int:
    total: int = 1
    for i, bit in enumerate(reversed(bin(power))):
        if (bit == 'b'): break
        cur: int = (base ** (int(bit) * (2**i))) % mod
        total *= cur
        total = total % mod
        
    # print(f"  ∴ {base} ^ {power}\t≡ {total} \t\t(mod {mod})\n")
    return total

def fltinv(a: int, p: int) -> int:
    return fastpow(a, p - 2, p)


# ##################################################################################
# Shanks Babystep-GiantStep. AKA Collision Alg
def getn(g: int, mod:int) -> int:
    # Find n = ⌊√N⌋ + 1     where N = O(g)  ->   N is the order of g   (mod p)
    return math.floor(math.sqrt(order(g, mod))) + 1

def list1(g:int, n:int, mod: int) -> list[int]:
    l1: list[int] = []
    for i in range(n + 1):
        # g ^ i     (mod p)
        l1.append((g**i) % mod)
    return l1

def list2(h:int, g: int, n:int, mod: int) -> list[int]:
    l2: list[int] = []
    for i in range(n + 1):
        # h * (g ^ -(i*n))      (mod p)
        l2.append((h * fltinv(fastpow(g, i*n, mod), mod)) % mod)
    return l2

def match(l1:list[int], l2:list[int]) -> tuple[int,int]:
    for idx, it in enumerate(l1):
        if (it in l2): return idx, l2.index(it)
    raise Exception("No Match")

def collision(g:int, h:int, mod:int) -> int:
    # Step 1:   get n
    n: int = getn(g, mod)

    # Step 2:   get List 1 and 2
    L1: list[int] = list1(g, n, mod)
    print(L1)
    L2: list[int] = list2(h, g, n, mod)
    print(L2)

    # Step 3:   Find the indeces of the matching element
    i: int
    j: int
    (i, j) = match(L1, L2)

    # Step 4:   Calculate x, where x = i + jn
    x: int = i + (j * n)
    return x


# ##################################################################################
def main() -> None:
    # Given
    g: int = 11
    h: int = 21
    mod: int = 71

    # Use Shank's Babystep-Giantstep (Collision Algorithm) to solve the DLP
    x:int = collision(g, h, mod)
    print(f"{g} ^ {x} = {h}\t(mod {mod})")

if __name__ == "__main__": main()