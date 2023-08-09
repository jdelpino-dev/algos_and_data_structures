from math import log10, floor


def karatsuba_mul(num1, num2):
    # Base cases
    if num1 < 10 or num2 < 10:
        return num1 * num2

    # Count digits
    digits1 = count_digits(num1)
    digits2 = count_digits(num2)
    max_digits = max(digits1, digits2)

    # If uneven digits, make it even
    if max_digits % 2:
        max_digits += 1
    cut_point = max_digits // 2

    # Split numbers
    a, b = split_number(num1, cut_point)
    c, d = split_number(num2, cut_point)

    # Recursively compute ac, bd and (a+b)(c+d)
    ac = karatsuba_mul(a, c)
    bd = karatsuba_mul(b, d)
    ab_cd = karatsuba_mul(a + b, c + d)

    # Compute adbc using Gauss's trick: (a+b)(c+d) - ac - bd
    ad_bc = ab_cd - ac - bd

    # Construct the result
    return (10 ** (2 * cut_point) * ac) + (10 ** cut_point * ad_bc) + bd


def count_digits(num):
    if num == 0:
        return 1
    return floor(log10(num)) + 1


def split_number(num, m):
    divisor = 10 ** m
    return num // divisor, num % divisor
