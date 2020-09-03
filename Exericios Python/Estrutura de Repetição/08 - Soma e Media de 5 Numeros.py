nums = [];
soma = 0;

for x in range(0, 5):
    num = int(input("Digite um numero: "));
    nums.append(num);

for y in nums:
    soma = soma + y;

    
print("\nSoma dos numeros = ", soma, "\nMédia =", soma/5);
