# Jogo de letras que mais aparece

frase = 'Leaving like a father. '\
        'Running like water'.lower()


i = 0
qtd_mais_vezes = 0
letra_mais_apareceu = ''


while i < len(frase):
    letra = frase[i]
    qtde_atual = frase.count(letra)
    
    if qtd_mais_vezes < qtde_atual and letra != ' ':
        qtd_mais_vezes = qtde_atual
        letra_mais_apareceu = letra
    

    i += 1

print(f'{letra_mais_apareceu} apareceu {qtd_mais_vezes} vezes, sendo a maior qtde')