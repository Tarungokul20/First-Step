def arithmetic_arranger(problem, disp_answers=False):
    if len(problem) > 5:
        return 'Error: Too many problems.'

    line1 = []
    line2 = []
    line3 = []
    line4 = []

    for i in problem:
        num1, operator, num2 = i.split()

        if operator not in ['+', '-']:
            return 'Error: Operator must be \'+\' or \'-\'.'
        if not num1.isdigit() or not num2.isdigit():
            return 'Error: Numbers must only contain digits.'
        if len(num1) > 4 or len(num2) > 4:
            return 'Error: Numbers cannot be more than four digits.' 

        width = 2 + max(len(num1), len(num2))
        line1.append(num1.rjust(width))
        line2.append(operator + num2.rjust(width - 1))
        line3.append('-' * width)  
        if disp_answers:
            result = int(num1) + int(num2) if operator == '+' else int(num1) - int(num2)
            line4.append(str(result).rjust(width))

    arranged = '    '.join(line1) + '\n' + '    '.join(line2) + '\n' + '    '.join(line3)
    if disp_answers:
        arranged += '\n' + '    '.join(line4)
    return arranged
print(arithmetic_arranger(["3801 - 2", "123 + 49"]))