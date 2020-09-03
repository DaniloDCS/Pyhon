qtd = int(input("Digite a quatidade que deseja sacar entre R$10 e R$600: "));

if(qtd <= 600 and qtd >= 10):

    n100 = int(qtd/100);
    qtd = qtd - (n100 * 100);

    n50 = int(qtd/50);
    qtd = qtd - (n50 * 50);

    n10 = int(qtd/10);
    qtd = qtd - (n10 * 10);

    n5 = int(qtd/5);
    qtd = qtd - (n5 * 5);

    n1 = int(qtd/1);
    qtd = qtd - (n1 * 1);

    print("Notas 1:",n1, "\nNotas 5:", n5 ,"\nNotas 10: ", n10 ,"\nNotas 50: ", n50, "\nNotas 100: ", n100);
else:
    print("Valor não disponíevel para saque");
