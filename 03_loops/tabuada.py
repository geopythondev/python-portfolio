# Exemplo 03 - Tabuada com loop for

# Solicita um número do usuário
numero = int(input("Digite um número para ver a tabuada: "))

# Loop for para calcular a tabuada de 1 a 10
print(f"\nTabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")