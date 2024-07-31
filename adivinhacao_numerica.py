import random

print("Seja muito bem-vindo ao Guess Number do Iury!")
numero_teto = input("Digite o número teto do desafio: ")

if numero_teto.isdigit():
    numero_teto = int(numero_teto)
else:
    print("Erro: valor informado não é numérico. Favor execute novamente e informe um número!")
    quit()

numero_aleatorio = random.randint(0, numero_teto)

n_tentativas = 0

while True:
    resposta_usuario = input("Advinhe o número: ")

    if resposta_usuario.isdigit():
        resposta_usuario = int(resposta_usuario)
    else:
        print("Erro: valor informado não é numérico. Favor informe um número!")
        continue
    
    n_tentativas = n_tentativas + 1
    if resposta_usuario == numero_aleatorio:
        print("Acertou!")
        break
    elif resposta_usuario > numero_aleatorio:
        print("Chutou alto, o número aleatório é menor que isso..")
    else:
        print("Chutou baixo, o número aleatório é maior que isso..")

print("N° de tentativas: " + str(n_tentativas))
