# 1. Operadores Matemáticos
numero_um = 20
numero_dois = 15

soma = numero_um + numero_dois
print(soma)

numero_três = 50
numero_quatro= 60

subtração = numero_três - numero_quatro
print(subtração)

divisao = numero_três / numero_quatro
print(divisao)

multiplicao = numero_três * numero_quatro
print(multiplicao)

subtração = numero_três - numero_quatro
print(f"A subtração entre {numero_um} - {numero_dois} = {subtração}")

# 2. Estruturas de repetição
# if (se) -> Verifica se uma condição é true (verdadeira). Se for, ele excuta o código.
# elif (senão se) -> é usado para testar várias condições. Ele só executa se todas as condições anteriores forem falsas
# else (senão) -> Executa o código se a condição if for false (falso).


# idade_usuario= 15
# # Se o usuário for maior de 18, eu vou passar a informação: Você é maior de idade; se não você é menor de idade.
# if idade_usuario >= 18:
#     print("você é maior de idade.")
# else:
#     print ("Você é menor de idade")

idade = 73
if idade >=18:
    print ("Você é maior de idade")
elif idade >= 0 and idade < 18:
    print ("Você é jovem de idade")
elif idade >= 70:
    print ("Você é experiente de idade")
else:
    print ("Você é menor de idade")