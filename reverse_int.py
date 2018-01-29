def reverse(self, n):
    """
    :type x: int
    :rtype: int
    """
    x = 0
    t = abs(n)    
    # Check if overflow or not
    if t > (2 ** 31 - 1):
        return 0
    while t > 0:
        d = t % 10
        x = x * 10 + d
        t //= 10
    if x > (2 ** 31 - 1):
        return 0
    if n > 0:
        return x
    else:
        return -1 * x

n = -120
res = reverse(n)
print(res)
