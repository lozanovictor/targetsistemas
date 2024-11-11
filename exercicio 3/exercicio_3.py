#Observe o trecho de código abaixo: int INDICE = 12, SOMA = 0, K = 1; 
# enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } imprimir(SOMA);
#Ao final do processamento, qual será o valor da variável SOMA?

#Resultado: 77

def main():
    INDICE = 12
    SOMA = 0
    K = 1
    
    while K < INDICE:
        K = K + 1
        SOMA = SOMA + K
    
    print(SOMA) ## O resultado é 77

if __name__ == "__main__":
    main()