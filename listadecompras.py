'''
Faça uma lista de compras
O usuário deve conseguir inserir, apagar e listar
Não permita que o programa quebre com valores de indices
'''

lista_de_compras = []

while True:

    entrada = input('Você deseja [i]nserir , [l]istar ou [a]pagar? ')

    if entrada == 'i':
        item = input('Digite o item que deseja adicionar: ')
        lista_de_compras.append(item)
        print('Item adicionado com sucesso! ')
        continue
    
    if entrada == 'l':
        if len(lista_de_compras) == 0:
            print('A lista está vazia!')
            continue
        else:
            for ordem, produto in enumerate(lista_de_compras):
                print(ordem, produto)
                continue
    
    if entrada == 'a':
        rem = input('Digite o indice que voce quer apagar: ')
        try:
            rem.isdigit()
            int_rem = int(rem)
            del lista_de_compras[int_rem]
            print('Indice deletado com sucesso! ')
            continue
        except ValueError:
            print('Por favor digite número. ')
            continue
        except IndexError:
            print('Índice não existe na lista. ')
            continue