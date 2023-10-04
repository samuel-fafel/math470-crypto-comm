def EEA(Q:list[int], R:list[int], u:list[int], v:list[int]) -> None:
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

    # return EEA(b, r, u, v, i - 1)            # Recursive: Else, return EEA of `b` and the remainder of `a/b`

a: int = 1_021_763_679
b: int = 519_424_709
Q: list[int] = [0, 0]
R: list[int] = [max(a, b), min(a, b)]
U: list[int] = [1, 0]
V: list[int] = [0, 1]

EEA(Q, R, U, V)
