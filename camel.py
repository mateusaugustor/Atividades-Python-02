def camel_to_snake(camel_case):

    snake_case = " "
    for caractere in camel_case:
        if caractere.isupper():
            snake_case += "_" + caractere.lower()

        else:
            snake_case += caractere
    return snake_case.lstrip("_")

name = input("Qual é o seu nome em CamelCase?")

snake_name = camel_to_snake(name)

print(f"Nome da variável em snake_case:{snake_name}")
