def gcd(u, v):
    if u < v:
        return gcd(v, u)

    if v == 0:
        return u

    return gcd(v, u % v)


def lcm(u, v):
    return (u * v) // gcd(u, v)


print(gcd(20, 30))
print(lcm(20, 30))
