import math


def calc(figure, function, size):
    def validate_size(expected, actual):
        if len(actual) != expected:
            raise ValueError(f"Expected {expected} arguments, got {len(actual)}.")
        if any(val <= 0 for val in actual):
            raise ValueError("All dimensions must be positive.")

    def calculate_area_or_perimeter(params, func, formulae):
        if func not in formulae:
            raise ValueError("Invalid function.")
        return formulae[func](*params)

    def circle(radius):
        return {
            'area': lambda r: math.pi * r ** 2,
            'perimeter': lambda r: 2 * math.pi * r,
        }

    def square(side):
        return {
            'area': lambda s: s ** 2,
            'perimeter': lambda s: 4 * s,
        }

    def triangle(a, b, c):
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides.")
        return {
            'area': lambda a, b, c: math.sqrt(
                (a + b + c) / 2 * ((a + b + c) / 2 - a) * ((a + b + c) / 2 - b) * ((a + b + c) / 2 - c)
            ),
            'perimeter': lambda a, b, c: a + b + c,
        }

    figures = {
        'circle': {'params': 1, 'functions': circle},
        'square': {'params': 1, 'functions': square},
        'triangle': {'params': 3, 'functions': lambda sides: triangle(*sides)},
    }

    if figure not in figures:
        raise ValueError("Invalid figure.")

    figure_data = figures[figure]
    validate_size(figure_data['params'], size)

    if function not in ['area', 'perimeter']:
        raise ValueError("Invalid function.")

    formulae = figure_data['functions'](size)
    return calculate_area_or_perimeter(size, function, formulae)
