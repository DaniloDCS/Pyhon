l1 = float(input("Digite a medida do lado 1: "));
l2 = float(input("Digite a medida do lado 2: "));
l3 = float(input("Digite a medida do lado 3: "));

if(l1 == l2 == l3):
    print("Triângulo Equilátero");
elif(l1 == l2 or l1 == l3 or l2 == l1 or l2 == l3 or l3 == l1 or l3 == l2):
    print("Triângulo Isóseles");
else:
    print("Triângulo Escaleno");
