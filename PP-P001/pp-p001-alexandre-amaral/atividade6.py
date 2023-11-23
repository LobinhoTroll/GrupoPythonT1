#ATIVIDADE 6.1

L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Imprime a lista de forma ao contrário: {L[::-1]}")
print("Imprime o último elemento: {L[-1::]}")
print("Imprime todos, menos o último elemento: {L[:-1:]}")
print("Imprime a lista ao contrário, pulando de 2 em 2: {L[::-2]}")
print("Imprime a lista do penultimo até o final: {L[-2::]}")
print("imprime todos, exceto os dois últimos: {L[:-2:]}")

#ATIVIDADE 6.2

L2 = ["Macaco", "Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Carneiro"]

userInput = input("Escolha o ano de seu nascimneto: ")

# Verifica se a entrada é um número inteiro válido
if userInput.isdigit():
    index = int(userInput)

    # Verifica se o índice está dentro dos limites
    if 0 <= index < len(L2):
        sign = L2[index]
        print(f"Signo: {sign}")
    else:
        print("Ano de nascimento fora do intervalo permitido.")
else:
    print("Ano de nascimento inválido.")
