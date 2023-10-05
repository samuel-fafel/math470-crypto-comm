#a = 50
#b = 19

def eea_gcd(a, b, verbose=True):
    x = max(a,b)
    y = min(a,b)

    u = [1,0]
    v = [0,1]
    q = [0,0]
    r = [x,y]

    if verbose:
        print("q r u v")
        print(f"_ {x} {u[0]} {v[0]}")
        print(f"_ {y} {u[1]} {v[1]}")

    i = 2
    while r[i-1] > 0:
        q.append(r[i-2] // r[i-1])
        r.append(r[i-2] % r[i-1])
        u.append(u[i-2] - q[i]*u[i-1])
        v.append(v[i-2] - q[i]*v[i-1])

        if verbose: print (f"{q[i]} {r[i]} {u[i]} {v[i]}")
        if r[i] == 0:
            break
        i += 1

    u_final = u[-2]
    v_final = v[-2]
    gcd = x * u_final  +  y * v_final

    if verbose:
        print("---")
        print(f"u = {u_final}, v = {v_final}")
        print(f"gcd({e1}, {e2} = {x * u_final  +  y * v_final})")
    
    return gcd

if __name__ == "__main__":
    e1 = 1021763679
    e2 = 519424709
    eea_gcd(e1, e2)
    
