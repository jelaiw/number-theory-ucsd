def gcd(a, b):
    assert a >= b and b >= 0 and a + b > 0
    return gcd(b, a % b) if b > 0 else a

print(gcd(1849639579327, 790933790547))
