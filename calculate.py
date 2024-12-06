import math

def calc(figure, function, size):
    if figure == 'circle':
        if len(size) != 1:
            raise ValueError(f"Expected 1 arguments, got {len(size)}.")
        radius = size[0]
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        if function == 'area':
            return math.pi * radius ** 2
        elif function == 'perimeter':
            return 2 * math.pi * radius
        else:
            raise ValueError("Invalid function.")
    elif figure == 'square':
        if len(size) != 1:
            raise ValueError(f"Expected 1 arguments, got {len(size)}.")
        side = size[0]
        if side <= 0:
            raise ValueError("Side must be positive.")
        if function == 'area':
            return side ** 2
        elif function == 'perimeter':
            return 4 * side
        else:
            raise ValueError("Invalid function.")
    elif figure == 'triangle':
        if len(size) != 3:
            raise ValueError(f"Expected 3 arguments, got {len(size)}.")
        a, b, c = size
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("All sides must be positive.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides.")
        if function == 'area':
            s = (a + b + c) / 2
            return math.sqrt(s * (s - a) * (s - b) * (s - c))
        elif function == 'perimeter':
            return a + b + c
        else:
            raise ValueError("Invalid function.")
    else:
        raise ValueError("Invalid figure.")
