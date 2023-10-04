def gcd(a:int, b:int) -> int:
    if (b == 0): return a           # Base Case: When one arg is 0, the other is the gcd
    if (b > a): return gcd(b, a)    # Swap Case: When `b` is larger than `a`, swap the args
    return gcd(b, a % b)            # Recursive: Else, return gcd of `b` and the remainder of `a/b`


def powers(g: int, p: int) -> None:
    for i in range(1, p):
        cur_pow: int = (g ** i) % p
        print(f"{g}^{i} \t= {cur_pow} \t(mod {p})  O({cur_pow})\t= {order(cur_pow, p)}")

def order(order_of: int, p: int) -> int | None:
    for x in range(1, p):
        test: int = (order_of ** x) % p
        if ((test) == 1): return x

# powers(2, 13)

# print(12 / gcd(10, 12))
print(order(11, 71))