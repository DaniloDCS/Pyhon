n1 = int(input("Digite a nota: "));
n2 = int(input("Digite a nota: "));

media = (n1 + n2 ) /2;

if(media >= 9 and media <= 10):
    print("Nota 1: ", n1, "\nNota 2: ", n2, "\nMedia: ", media, "\nConceito: A \nAPROVADO");
elif(media >= 7.5 and media < 9):
    print("Nota 1: ", n1, "\nNota 2: ", n2, "\nMedia: ", media, "\nConceito: B \nAPROVADO");
elif(media >= 6 and media < 7.5):
    print("Nota 1: ", n1, "\nNota 2: ", n2, "\nMedia: ", media, "\nConceito: C \nAPROVADO");
elif(media >= 4 and media < 6):
    print("Nota 1: ", n1, "\nNota 2: ", n2, "\nMedia: ", media, "\nConceito: D \nREPROVADO");
elif(media >= 0 and media < 4):
    print("Nota 1: ", n1, "\nNota 2: ", n2, "\nMedia: ", media, "\nConceito: E \nREPROVADO");








