# 1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


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
    sair = 1
    while sair !=0:
        print("\n Digite um numero inteiro e veja se ele pertence a sequencia de Fibonacci: \n")
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

        print("Deseja continuar? (1 para sim, 0 para não): ")
        sair = int(input())

if __name__ == "__main__":
    main()