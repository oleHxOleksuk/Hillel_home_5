
inter = input('Для завершення обчислень натисніть "y": ')

while inter != 'y':

    first_operand = float(input('Введіть перше число: '))

    math_operation = input('Введіть  оператор +,-,*,/: ')

    second_operand = float(input('Введіть друге число: '))

    result_operation = 0

    if math_operation == '+':
        result_operation = first_operand + second_operand
        print('Результат операції додавання:', result_operation)

    elif math_operation == '-':
        result_operation = first_operand - second_operand
        print('Результат операції віднімання:', result_operation)

    elif math_operation == '*':
        result_operation = first_operand * second_operand
        print('Результат операції множення:', result_operation)

    elif math_operation == '/' and second_operand != 0:
        result_operation = first_operand / second_operand
        print('Результат операції множення:', result_operation)

    else:
        print("Можливо ви використовуєте відсутній оператор або ділите на 0")
    inter = input('Для завершення обчислень натисніть "y": ')