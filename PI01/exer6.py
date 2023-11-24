ano_nascimento = int(input("Digite o ano de nascimento: "))
signo_zodiaco_chines = ano_nascimento % 12

signos = {
    0: "Macaco",
    1: "Galo",
    2: "Cão",
    3: "Porco",
    4: "Rato",
    5: "Boi",
    6: "Tigre",
    7: "Coelho",
    8: "Dragão",
    9: "Serpente",
    10: "Cavalo",
    11: "Carneiro"
}

print(f"Seu signo do zodíaco chinês é: {signos[signo_zodiaco_chines]}")
