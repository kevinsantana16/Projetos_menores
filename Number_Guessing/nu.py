from random import randint

print("Jogo: adivinhe o número")
print("Você tem 5 tentativas")

tentativas = 0 
acertos = 0
erros = 0

while tentativas != 5:
    num = randint(1, 50)
    user = int(input("Escolha um número entre 1 e 50: "))

    if num == user:
        print("Número correto!!!")
        print(f"Número gerado: {num}")
        print(f"Número que você escolheu: {user}")
        tentativas += 1
        acertos += 1
        erros += 1
        print("#"*45) 
    
    else:
        print("Número Incorreto")
        print(f"Número gerado: {num}")
        print(f"Número que você escolheu: {user}")
        tentativas += 1
        acertos += 1
        erros += 1
        print("#"*45)
print("Jogo finalizado")
print(f"Acertos: {acertos}; Erros: {erros}")

