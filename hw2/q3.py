def f(m: int, y: int):
    print("x^2 ≡ %x (mod %d)" % (y, m))
    print("{")
    for x in range(0, m):
        if ((x**2 % m) == y):
            print(f"  {x}")
    print("}\n")


f(11, 3)
f(13, 2)
f(51, 19)