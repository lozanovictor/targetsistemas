def fibo (numero):
    sequencia = 1
    anterior = 0
    while sequencia <= numero:    
        if numero == sequencia:
            print(f"O número informado ({numero}) pertence à sequência de Fibonacci")
            return
        
        # Atualiza os valores para o próximo número da sequência
        anterior, sequencia = sequencia, sequencia + anterior
            
    print(f"O número informado ({numero}) não pertence à sequência de Fibonacci \n")

def main():
    print("Digite um numero inteiro e veja se ele pertence a sequencia de Fibonacci: \n")
    try:
        numero = int(input())
        if numero < 0:
            print(f"O número informado ({numero}) é negativo e não pertence a sequencia de Fibonacci \n")
        elif numero == 0:
            print(f"O número informado ({numero}) pertence a sequencia de Fibonacci \n")
        elif numero == 1:
            print(f"O número informado ({numero}) pertence a sequencia de Fibonacci \n")
        else:
            fibo(numero)
    except ValueError:
        print("O valor informado não é um número inteiro \n")

if __name__ == "__main__":
    main()