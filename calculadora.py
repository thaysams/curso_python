# Calculadora fazendo uso de while


while True:
    numero_1 = input('Digite o primeiro numero: ')
    numero_2 = input('Digite o segundo numero: ')
    operador = input('Digite o operador: ')

    try:
        numero_1.isdigit()
        numero_2.isdigit()
        int_num1 = int(numero_1)
        int_num2 = int(numero_2)

        if operador not in '+-/*':
            print('Digite um operador válido')
            continue

        elif len(operador) > 1:
            print('Digite apenas um operador')
            continue
        
        elif operador == '+':
            soma = int_num1 + int_num2
            print(soma)

        elif operador == '-':
            subtracao = int_num1 - int_num2
            print(subtracao)

        elif operador == '*':
            multiplicacao = int_num1 * int_num2
            print(multiplicacao)

        elif operador == '/':
            divisao = int_num1 / int_num2
            print(divisao)

    except:
        print('Digite números válidos')
        continue    


    sair = input('Você deseja sair? ').startswith('s')

    if sair is True:
        break