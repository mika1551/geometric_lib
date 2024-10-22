import circle
import square


figs = ['circle', 'square']
funcs = ['perimeter', 'area']
sizes = {}
def calc(fig, func, size):
	assert fig in figs
	assert func in funcs
'''Две предыдущие строчки проверяют, есть ли фигура figs в списке figs и функция func в списке funcs'''
    result = eval(f'{fig}.{func}(*{size})')
'''Вычисляет результат функции func из модуля fig'''
    print(f'{func} of {fig} is {result}')
'''Выводит на экран результат вычислений'''
if name == "main":
'''Этот блок кода выполняется только тогда, когда файл запущен как основная программа'''
    func = ''
'''Инициализирует переменную func пустой строкой'''
    fig = ''
'''Инициализирует переменную fig пусой строкой'''
    size = list()
'''Создает пустой список size'''
    while fig not in figs:
       fig = input(f"Enter figure name, avaliable are {figs}:\n")
'''Цикл выполняется пока пользователь не введет корректное название фигуры, запрашивает название фигуры и сохраняет ее в переменную fig'''
    while func not in funcs:
       func = input(f"Enter function name, avaliable are {funcs}:\n")
'''Цикл выполняется пока пользователь не введет корректное название функции, запрашивает название функции и сохраняет ее в переменную func'''
    while len(size) != sizes.get(f"{func}-{fig}", 1):
       size = list(map(int, input("Input figure sizes separated by space, 1 for circle and square\n").split(' ')))
'''Цикл повторяется, пока пользователь не введет корректное количество параметров для выбранной фигуры и функции, запрашивает у пользователя размеры фигуры, разделенные пробелами и преобразует их в целые числа'''
    calc(fig, func, size)