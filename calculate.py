import math


def calc(figure, function, size):
    def validate_size(expected, actual):
        if len(actual) != expected:
            raise ValueError(f"Expected {expected} arguments, got {len(actual)}.")
        if any(val <= 0 for val in actual):
            raise ValueError("All dimensions must be positive.")

    def circle_functions(radius, func):
        if func == 'area':
            return math.pi * radius[0] ** 2
        if func == 'perimeter':
            return 2 * math.pi * radius[0]

    def square_functions(side, func):
        if func == 'area':
            return side[0] ** 2
        if func == 'perimeter':
            return 4 * side[0]

    def triangle_functions(sides, func):
        a, b, c = sides
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides.")
        if func == 'area':
            s = (a + b + c) / 2
            return math.sqrt(s * (s - a) * (s - b) * (s - c))
        if func == 'perimeter':
            return a + b + c

    figures = {
        'circle': {'params': 1, 'functions': circle_functions},
        'square': {'params': 1, 'functions': square_functions},
        'triangle': {'params': 3, 'functions': triangle_functions},
    }

    if figure not in figures:
        raise ValueError("Invalid figure.")

    figure_data = figures[figure]
    validate_size(figure_data['params'], size)

    if function not in ['area', 'perimeter']:
        raise ValueError("Invalid function.")

    return figure_data['functions'](size, function)
