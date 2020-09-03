n1 = float(input("Digite a 1o nota: "));
n2 = float(input("Digite a 2o nota: "));

media = (n1 + n2) / 2;

if(media >= 7 and media <= 9.9):
    print("A media é ",media," e está Aprovado");
elif(media == 10):
    print("A media é ",media," e está Aprovado com Distinação");
else:
    print("A media é ",media," e está Reprovado");
