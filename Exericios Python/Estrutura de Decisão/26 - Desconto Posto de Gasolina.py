tipo = input("Qual tipo conbustivel você comprou?\nA - Álcool R$ 1.90\nG - Gasolina R$2.50\nQual? ");
qtd = float(input("Digite a quantidade de litros comprado: "));

if(tipo == "a" or tipo == "A"):
    if(qtd <= 20):
        desconto = (1.90 * 3) / 100;
        cutso = (qtd * 1.90) - (desconto * qtd);
    elif(qtd > 20):
        desconto = (1.90 * 5) / 100;
        cutso = (qtd * 1.90) - (desconto * qtd);
elif(tipo == "g" or tipo == "G"):
    if(qtd <= 20):
        desconto = (2.50 * 4) / 100;
        cutso = (qtd * 1.90) - (desconto * qtd);
    elif(qtd > 20):
        desconto = (2.50 * 6) / 100;
        cutso = (qtd * 1.90) - (desconto * qtd);


print(cutso);



