L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Imprime a lista de forma ao contrário: {L[::-1]}")
print("Imprime o último elemento: {L[-1::]}")
print("Imprime todos, menos o último elemento: {L[:-1:]}")
print("Imprime a lista ao contrário, pulando de 2 em 2: {L[::-2]}")
print("Imprime a lista do penultimo até o final: {L[-2::]}")
print("imprime todos, exceto os dois últimos: {L[:-2:]}")

def determinar_zodiaco_chines(ano_de_nascimento):

    animais = ["Macaco", "Galo", "Cão", "Porco", "Rato", "Boi", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Cabra"]

    indice_animal = (ano_de_nascimento - 1924) % 12

    print(f"Seu signo no zodíaco chinês é {animais[indice_animal]}.")

ano_de_nascimento = int(input("Digite o ano de nascimento: "))
determinar_zodiaco_chines(ano_de_nascimento)
