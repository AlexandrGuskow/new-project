def contr_input(oper):
    if oper == '+' or oper == '-' or oper == '/' or oper == '*':
        return oper
    else:
        print('Ошибка! Возможные операции: +, -, *, /')
        oper = input('Введите операцию: ')
        return contr_input(oper)

def operation(answer, oper, operand):
    if oper == '+':
        return answer + operand
    elif oper == '-':
        return answer - operand
    elif oper == '*':
        return answer * operand
    else:
        return answer / operand


def operand(oper, numb_operand):
    operand = float(input('Введите операнд 1: '))
    answer = operand
    formula = str(operand)
    for numb in range(2, numb_operand + 1):
        operand = float(input('Введите операнд ' + str(numb) + ': '))
        formula += oper + str(operand)
        answer = operation(answer, oper, operand)
    return answer, formula


oper = input('\nВведите операцию: ')
oper = contr_input(oper)
numb_operand = int(input('Сколько будет операндов? '))
answer, formula = operand(oper, numb_operand)

print(formula, "=", answer)
