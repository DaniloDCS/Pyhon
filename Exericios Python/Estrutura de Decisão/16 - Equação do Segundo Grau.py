import math;
a = int(input("Digite o valor de A: "));

if(a != 0):
    b = int(input("Digite o valor de B: "));
    c = int(input("Digite o valor de C: "));
    
    delta = (b**2) - (4 * a * c);
    
    if delta < 0:
        print("A equacao não possuí raízes.");
    elif(delta == 0):
        print("A equacao possuí uma raíz.");
        raiz = ((b * -1) + math.sqrt(delta)) / (2 * a);
        print("x =", raiz);
    else:
        print("A equacao possuí duas raízes.");
        raiz1 = ((b * -1) + math.sqrt(delta)) / (2 * a); 
        raiz2 = ((b * -1) - math.sqrt(delta)) / (2 * a);
        print("x1 =", raiz1, "x2 =", raiz2);

