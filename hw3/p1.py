def fastpow(base: int, power: int, mod: int) -> int:
    total: int = 1
    for i, bit in enumerate(reversed(bin(power))):
        if (bit == 'b'): break
        cur: int = (base ** (int(bit) * (2**i))) % mod
        if (cur != 1): print(f"({base} ^ 2) ^ {i}\t≡ {cur} \t\t(mod {mod})")
        total *= cur
        total = total % mod
        
    print(f"  ∴ {base} ^ {power}\t≡ {total} \t\t(mod {mod})\n")
    return total

def fltinv(a: int, p: int) -> int:
    print(f"By FLT a ^ -1\t≡ a ^ (p - 2) \t(mod p)")
    print(f"Thus, {a} ^ -1\t≡ {a} ^ {p - 2} \t(mod {p})\n")
    inv: int = fastpow(a, p - 2, p)
    print(f"  ∴ {a} ^ -1\t≡ {inv} \t\t(mod {p})")
    return inv


g: int = 2
p: int = 1373

b: int = 716
B: int = (g ** b) % p

a: int = 947
A: int = (g ** a) % p

m: int = 583

gab:int =  (g ** (a*b)) % p

x: int = fltinv(gab, p)
c2: int = gab * m

print((x * c2) % p)
# fltinv(345, 587)
