n1 = float(input("Digite a nota 01: "));
n2 = float(input("Digite a nota 02: "));
n3 = float(input("Digite a nota 03: "));

media = round((n1 + n2 + n3)/3, 1);

if(media >= 7 and media <= 9.9):
    print("APROVADO! Média =", media);
elif(media >=0 and media < 7):
    print("REPROVADO! Média =", media);
elif(media == 10):
    print("APROVADO com Distinação! Média =", media);
else:
    print("Não há possibilidade de ter essa media!");
