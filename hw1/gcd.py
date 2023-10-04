def gcd(a:int, b:int) -> int:
    if (b == 0): return a           # Base Case: When one arg is 0, the other is the gcd
    if (b > a): return gcd(b, a)    # Swap Case: When `b` is larger than `a`, swap the args
    return gcd(b, a % b)            # Recursive: Else, return gcd of `b` and the remainder of `a/b`


def main() -> None:
    a = 1234567890123456789012345678901234567890123456789012345678901234567890123456789
    b = 234567890123456789012345678901234567890123456789012345678901234567890123456789
    print("Given:\n\n\ta = %d\n\tb = %d\n\nGCD(a,b) = %d" % (a, b, gcd(a,b)) )
    print("\nWhere:")
    print("\ngcd(a:int, b:int) -> int:")
    print("\tif b == 0 return a")
    print("\tif b > a return gcd(b,a)")
    print("\treturn gcd(b, a rem b)")


if __name__ == "__main__": main()