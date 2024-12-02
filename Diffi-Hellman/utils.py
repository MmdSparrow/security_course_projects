import math

def __is_primitive_root(g, p):
    required_set = {num for num in range(1, p)}
    actual_set = {pow(g, power, p) for power in range(1, p)}
    return required_set == actual_set

def find_primitive_root(p):
    if p < 2:
        raise ValueError("The input must be a prime number greater than 1.")
    for g in range(p-1, 1, -1):
        if __is_primitive_root(g, p):
            return g
    return None

def mod_exp(base, exp, mod):
    return pow(base, exp, mod)

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

print(find_primitive_root(137))