# Escreva um programa que verifique, em uma string, a existência da letra ‘a’, 
# seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def pegaletra(palavra):
    count = 0
    for i in range(len(palavra)):
        if palavra[i] in "aA":
            count+=1
    return count
        


def main():
    sair = 1
    while sair != 0:
        print("\n Contador de letras A \n")
        print("Digite uma palavra: \n")
        palavra = input()

        print("A letra 'a' aparece", pegaletra(palavra), "vezes na palavra.\n\n\n")
        print("Deseja continuar? (1 para sim, 0 para não): ")
        sair = int(input())


if __name__ == "__main__":
    main()