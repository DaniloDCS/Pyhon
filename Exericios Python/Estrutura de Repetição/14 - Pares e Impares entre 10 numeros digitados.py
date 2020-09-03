nums = [];
for x in range(1, 11):
    num = int(input("Digite um número: "));
    nums.append(num);
    
pares = 0;
impares = 0;

for y in nums:
    if(y % 2 == 0):
        pares = pares + 1;
    else:
        impares = impares + 1;


print(pares, "Pares e",impares,"Impares");
