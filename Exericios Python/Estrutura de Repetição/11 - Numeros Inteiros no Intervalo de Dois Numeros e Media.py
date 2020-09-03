num1 = int(input("Digite um numero: "));
num2 = int(input("Digite um numero: "));
soma = 0;

for x in range(num1, num2+1):
    print(x);

for y in range(num1, num2+1):
    soma = soma + y;

    
print("\nSoma dos numeros = ", soma);
