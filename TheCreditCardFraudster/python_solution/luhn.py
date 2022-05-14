def checksum(string):
    """
    Compute the Luhn checksum for the provided string of digits.
    Note this assumes the check digit is in place.
    """
    digits = list(map(int, string))
    odd_sum = sum(digits[-1::-2])
    even_sum = sum([sum(divmod(2 * d, 10)) for d in digits[-2::-2]])
    return (odd_sum + even_sum) % 10


def verify(string):
    """
    Check if the provided string of digits satisfies the Luhn checksum.
    >>> verify('356938035643809')
    True
    >>> verify('534618613411236')
    False
    """
    return checksum(string) == 0


for i in range(5432100000001234, 5432109999991234, 10000):
    if i % 123457 == 0 and verify(str(i)):
        print("CTFlearn{" + str(i) + "}")
