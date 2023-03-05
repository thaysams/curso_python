# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

acertos = 0
erros = 0
resposta_correta = ''

for item in perguntas:
    print(item['Pergunta'])
    
    for indice, opcoes in enumerate(item['Opções']):
        print(indice, ')', opcoes)

        if opcoes == item['Resposta']:
            resposta_correta = indice

    resposta_usuario = int(input('Digite sua resposta: '))
    if resposta_usuario == resposta_correta:
        print('Parabéns, você acertou! ✅ \n')
        acertos += 1
    else:
        print('Você errou! ❌ \n')
        erros += 1

print(f'Você acertou {acertos} perguntas 👏👏')