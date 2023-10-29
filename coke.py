def main():
    valor_pag = int(input("Qual moeda deseja colocar? "))
    valor_falta = 50 - valor_pag

    while valor_falta > 0:
        print(f"Ainda falta {valor_falta} centavos")
        resto_pag = int(input(f"Insira mais {valor_falta} centavos: "))
        
        if resto_pag not in [25, 10, 5]:
            print("Moeda não aceita. Insira uma moeda de 25, 10 ou 5 centavos.")
            continue  
        
        valor_falta -= resto_pag 

        if valor_falta == 0:
            print("Obrigado pela sua compra.")

        elif valor_falta < 0:
            troco = abs(valor_falta)
            print(f"Seu troco é {troco} centavos.")

        else:
            print(f"Valor devido: {valor_falta} centavos")

main()