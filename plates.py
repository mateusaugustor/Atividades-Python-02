def main():
    plate = input("Minha placa é: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(i):
    if len(i) != 6:
        return False

    if not i[:3].isalpha():
        return False

    if not i[3:].isdigit():
        return False

    if not i.isalnum():
        return False

    return True

main()