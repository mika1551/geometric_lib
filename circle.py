def area(a):
    if (a < 0):
        raise ValueError("Can't use '-' numbers")

    return a * a


def perimeter(a):
    if (a < 0):
        # added verification of borders cuz them cant be below zeros
        raise ValueError("Can't use '-' numbers")
    return 4 * a
