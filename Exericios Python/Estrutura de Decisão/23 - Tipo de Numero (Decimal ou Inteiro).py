num = float(input("Digite um número: "));

if(round(num, 1) % int(num) != 0):
    print("Decimal")
else:
    print("Inteiro");
