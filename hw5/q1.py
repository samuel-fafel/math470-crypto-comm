def fastpow(base: int, power: int, mod: int) -> int:
    total: int = 1
    for i, bit in enumerate(reversed(bin(power))):
        if (bit == 'b'): break
        cur: int = (base ** (int(bit) * (2**i))) % mod
        total *= cur
        total = total % mod
        
    # print(f"  ∴ {base} ^ {power}\t≡ {total} \t\t(mod {mod})\n")
    return total

def inverse(): pass