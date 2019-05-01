def calculate_2(a, b, operator="add"):
    functions = {
        'add': lambda x, y: x + y,
        'sub': lambda x, y: x - y,
        'mul': lambda x, y: x * y,
        'pow': lambda x, y: x ** y,
        'div': lambda x, y: x / y
    }
    fun = functions[operator]
    result = fun(a, b)
    return result



def calculate(a, b, operator="add"):
    if operator == 'add':
        return a + b
    elif operator == 'sub':
        return a - b
    elif operator == 'mul':
        return a * b
    elif operator == 'div':
        return a / b
    elif operator == 'pow':
        return a ** b


a, b = 10, 5
for opr in ['add', 'sub', 'mul', 'pow', 'div']:
    res = calculate(a, b, operator=opr)
    print(a, opr, b, '=', res)

