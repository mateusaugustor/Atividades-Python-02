def remover_vogais(texto):
    resultado = ""

    for char in texto:
        if char.lower() not in "aeiou":
            resultado += char

    return resultado

texto = input("Digite uma string de texto: ")

texto_sem_vogais = remover_vogais(texto)

print(f"Texto sem vogais: {texto_sem_vogais}")