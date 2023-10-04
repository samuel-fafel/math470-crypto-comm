def fastpow(base: int, power: int, mod: int) -> int:
    total: int = 1
    for i, bit in enumerate(reversed(bin(power))):
        print(i)
        if (bit == 'b'): break
        cur: int = (base ** (int(bit) * (2**i))) % mod
        total *= cur
        total = total % mod
        
    print(f"  ∴ {base} ^ {power}\t≡ {total} \t\t(mod {mod})\n")
    return total

def EEA(a: int, b: int) -> tuple[int,int]:
    Q: list[int] = [0, 0]
    R: list[int] = [max(a, b), min(a, b)]
    U: list[int] = [1, 0]
    V: list[int] = [0, 1]
    i:int = 2
    print("it\tq\tr\tu\tv")
    print(f"{0}\t{Q[0]}\t{R[0]}\t{U[0]}\t{V[0]}")
    print(f"{1}\t{Q[1]}\t{R[1]}\t{U[1]}\t{V[1]}")
    while True:
        Q.append(R[i-2] // R[i-1])
        R.append(R[i-2] % R[i-1])
        U.append(U[i-2] - (Q[i] * U[i-1]))
        V.append(V[i-2] - (Q[i] * V[i-1]))
        if (R[i] == 0): break
        print(f"{i}\t{Q[i]}\t{R[i]}\t{U[i]}\t{V[i]}")
        i += 1
    print(f"u = {U[i-1]}\nv = {V[i-1]}")

    return (U[i-1], V[i-1])

    # return EEA(b, r, u, v, i - 1)            # Recursive: Else, return EEA of `b` and the remainder of `a/b`

a: int = 1_021_763_679
b: int = 519_424_709
u: int
v: int
u, v = EEA(a, b)

# Decrypt C1 and C2 -> m = c1^u * c2^v
c1: int = 1244183534
c2: int = 732959706
N: int = 1889570071

m: int = (pow(c1, u, N)  * pow(c2, v, N)) % N

print(f"Message = {m}")