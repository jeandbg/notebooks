print("\n--------------")
print("com loop for ficamos limitados a um número arbitrario de vezes")

numero = -1
for _ in range(3):  # Supondo um número máximo de tentativas (3) arbitrário
    numero = int(input("Digite um número positivo: "))
    if numero > 0:
        break

print("Você digitou:", numero)

print("--------------")
print("agora com loop while")

numero = -1
while numero <= 0:
    numero = int(input("Digite um número positivo: "))

print("Você digitou:", numero)

# o código quebra se digitar qualquer coisa que não sejam números