base = int(input("Digite a base: "));
expoente = int(input("Digite o expoente: "));
result = 1;

for x in range(1, expoente+1):
    result = result * base;

print(result);


