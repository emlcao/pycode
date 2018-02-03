"""
Q: Count the number of prime numbers less than a non-negative number
Input: non-negative integer n
Output: int - number of prime numbers
Edge cases:
n < 0, output = None
n = 0, output = 0
A:

"""
def count_prime(n):
    # create an array with value 0 as non-prime, 1 as prime
    a = [0] * 2 + [1] * (n - 2)
    i = 2
    while i * i < n:
        if i:
            j = i
            while i * j < n:
                prod = i * j
                a[prod] = 0
                j += 1
        i += 1
    return sum(a)

# def count_prime(n):
#     # create an array with value 0 as non-prime, 1 as prime
#     a = [0] * 2 + [1] * (n - 2)
#     for i in range(2, n):
#         for j in range(2, n):
#             prod = i * j
#             if prod >= n:
#                 break
#             a[prod] = 0
#     return sum(a)

n = 999983
# n = 10
# output = 3
res = count_prime(n)
print(res)
# assert(output == res)
