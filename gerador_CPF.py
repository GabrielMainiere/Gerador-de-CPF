
import random

print('CPF gerado')
nove_digitos = '' 
for i in range(9): #gerando 9 dígitos aleatórios 
    nove_digitos += str(random.randint(0,9))

contagem_1 = 10
soma_1 = 0

#Algorítmo para encontrar o primeiro dígito de um CPF
for digito_1 in nove_digitos:
    multiplicacao_1 = int(digito_1) * contagem_1
    contagem_1 -= 1
    soma_1 +=multiplicacao_1

resultado_1 = (soma_1 *10) %11
if resultado_1 > 9:
    primeiro_digito = 0
else:
    primeiro_digito = resultado_1

#Algorítmo para encontrar o segundo dígito de um CPF
soma_2 = 0

dez_digitos = nove_digitos + str(primeiro_digito)
contagem_2 = 11
for digito_2 in dez_digitos:
    multiplicacao_2 = int(digito_2) * contagem_2
    contagem_2 -=1
    soma_2 += multiplicacao_2

resultado_2 = (soma_2 *10) % 11
if resultado_2 > 9:
    segundo_digito = 0
else:
    segundo_digito = resultado_2

cpf_gerado = f'{nove_digitos}{primeiro_digito}{segundo_digito}'
print(cpf_gerado)