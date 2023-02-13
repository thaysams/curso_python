import re # método que permite substituições
import sys # método de sair do python


entrada = input('Digite seu cpf conforme exemplo: [746.824.890-70]: ')
cpf_digitado_user = re.sub(
    r'[^0-9]',   #substituindo tudo que não for um número de 0 a 9
    '',
    entrada
)

entrada_e_repeticao = entrada == entrada[0] * len(entrada)

if entrada_e_repeticao:
    print('Você enviou dados repetidos sequencialmente.')
    sys.exit()

nove_digitos = cpf_digitado_user[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_digitado_user == cpf_gerado_pelo_calculo:
    print(f'{cpf_digitado_user} é válido')
else:
    print('CPF inválido')