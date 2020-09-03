print("TABELA DE PREÇOS");
print("Produt o     Até 5 Kg            Acima de 5 Kg");
print("Morango      R$ 2,50 por Kg      R$ 2,20 por Kg");
print("Maçã         R$ 1,80 por Kg      R$ 1,50 por Kg");

qtd1 = int(input("\nQual a quantidade em Kg de Morango: "));
qtd2 = int(input("Qual a quantidade em Kg de Maçã: "));


kgT = qtd1 + qtd2;

if(kgT <= 5):
    valUni1 = 2.50;
    valUni2 = 1.80;
    pagar = (qtd1 * valUni1) + (qtd2 * valUni2);
    desconto = "0.00";
elif(kgT > 5):
    valUni1 = 2.20;
    valUni2 = 1.50;
    pagar = (qtd1 * valUni1) + (qtd2 * valUni2);
    desconto = "0.00";
    if(kgT > 8 or pagar > 25.0):
        pagar = pagar - ((pagar * 10)/100);
        desconto = round((pagar * 10)/100, 2);

print("\n\n****** NOTA FISCAL ******");
print("Produto    Kg     Valor 1Kg    Valor Total");
print("Morango   ", qtd1  ,"     R$", valUni1,"      R$ ",(qtd1 * valUni1));
print("Maçã      ", qtd2  ,"     R$", valUni2,"      R$ ",(qtd2 * valUni2));
print("\nDescontos: R$",desconto);
print("Total a pagar: R$",pagar);
print("****** *********** ******");
