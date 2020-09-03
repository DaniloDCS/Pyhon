n = [];

for x in range(0, 5):
    num = int(input("Digite o número: "));
    n.append(num);
    
maior = 0 
for b in n:
    if(b < maior):
        maior = maior; 
    else:
        maior = b;

print("O maior é ", maior);

