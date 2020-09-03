num = int(input("Digite um numero para saber o fatorial: "));
a = 1;
b = 1;
c = 1;
fatorial = 1;

for x in range(1, num+1):
    c = num + 1;
    a = c - x;
    b = a - 1;
    if(a != 0 and b != 0):
        print(a, b);
        fatorial = (a * b);
        
print(fatorial);
