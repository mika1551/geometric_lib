from circle import area as circle_area, perimeter as circle_perimeter
from square import area as square_area, perimeter as square_perimeter
from triangle import area as triangle_area, perimeter as triangle_perimeter


def calc(figure, function, size):
    def validate_size(expected, actual):
        if len(actual) != expected:
            raise ValueError(f"Expected {expected} arguments, got {len(actual)}.")
        if any(val <= 0 for val in actual):
            raise ValueError("All dimensions must be positive.")

    figures = {
        'circle': {
            'params': 1,
            'functions': {'area': circle_area, 'perimeter': circle_perimeter},
        },
        'square': {
            'params': 1,
            'functions': {'area': square_area, 'perimeter': square_perimeter},
        },
        'triangle': {
            'params': 3,
            'functions': {'area': triangle_area, 'perimeter': triangle_perimeter},
        },
    }

    if figure not in figures:
        raise ValueError("Invalid figure.")

    figure_data = figures[figure]
    validate_size(figure_data['params'], size)

    if function not in figure_data['functions']:
        raise ValueError("Invalid function.")

    return figure_data['functions'][function](*size)
