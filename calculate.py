import circle
import square
import triangle

sizes = {
    'circle-area': 1,
    'circle-perimeter': 1,
    'square-area': 1,
    'square-perimeter': 1,
    'triangle-area': 3,
    'triangle-perimeter': 3,
}
figs = ['circle', 'square', 'triangle']
funcs = ['perimeter', 'area']

def calc(fig, func, size):
    if fig not in figs:
        raise ValueError("Invalid figure.")
    if func not in funcs:
        raise ValueError("Invalid function.")
    
    key = f'{fig}-{func}'
    expected_args = sizes.get(key)
    if expected_args is None:
        raise ValueError("Invalid function-figure combination.")
    
    if len(size) != expected_args:
        raise ValueError(f"Expected {expected_args} arguments, got {len(size)}.")
    
    if any(s < 0 for s in size):
        raise ValueError("Size values must be non-negative.")
    
    if fig == 'triangle':
        a, b, c = size
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides")
    
    if fig == 'circle':
        if func == 'area':
            return circle.area(*size)
        if func == 'perimeter':
            return circle.perimeter(*size)
    elif fig == 'square':
        if func == 'area':
            return square.area(*size)
        if func == 'perimeter':
            return square.perimeter(*size)
    elif fig == 'triangle':
        if func == 'area':
            return triangle.area(*size)
        if func == 'perimeter':
            return triangle.perimeter(*size)
