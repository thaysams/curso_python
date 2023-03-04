'''
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro
'''

def multiplicacao(equacao):
    def funcao(numero):
        if equacao == 'duplicar':
            resultado = 2*numero
            return f'O resultado da duplicação é {resultado}'
        if equacao == 'triplicar':
            resultado = 3*numero
            return f'O resultado da triplicação é {resultado}'
        if equacao == 'quadruplicar':
            resultado = 4*numero
            return f'O resultado da quadruplicação é {resultado}'
    return funcao

duplicacao = multiplicacao('duplicar')
triplicar = multiplicacao('triplicar')
quadruplicação = multiplicacao('quadruplicar')

for num in [6]:
    print(duplicacao(num))
    print(triplicar(num))
    print(quadruplicação(num))


