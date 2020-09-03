print("TABELA DE PREÇOS");
print("Produtos/Tipo      Até 5 Kg           Acima de 5 Kg");
print("File Duplo - 1     R$ 4,90 por Kg     R$ 5,80 por Kg");
print("Alcatra - 2        R$ 5,90 por Kg     R$ 6,80 por Kg");
print("Picanha - 3        R$ 6,90 por Kg     R$ 7,80 por Kg");

prod = int(input("\nQual a o produto comprado: "));
qtd = float(input("Qual a quantidade em Kg: "));

formPag = int(input("\nForma de Pagamento?\nCratão   - 1 - 5% de desconto\nDinheiro - 2 - 0% de desconto\nQual? "))

if(qtd <= 5):
    if(prod == 1):
        valKg = 4.90;
        pagar = (qtd * valKg);
        prodT = "File Duplo";

        if(formPag == 1):
            pagar = pagar - ((pagar * 5)/100);
            desconto = round((pagar * 5)/100, 2);
        else:
            desconto = "0.00";
            
    elif(prod == 2):
        valKg = 5.90;
        pagar = (qtd * valKg);
        prodT = "Alcatra";
        
        if(formPag == 1):
            pagar = pagar - ((pagar * 5)/100);
            desconto = round((pagar * 5)/100, 2);
        else:
            desconto = "0.00";
            
    elif(prod == 3):
        valKg = 6.90;
        pagar = (qtd * valKg);
        prodT = "Picanha";

        if(formPag == 1):
            pagar = pagar - ((pagar * 5)/100);
            desconto =  round((pagar * 5)/100, 2);
        else:
            desconto = "0.00";
        
elif(qtd > 5.0):
    if(prod == 1):
        valKg = 5.80;
        pagar = (qtd * valKg);
        prodT = "File Duplo";
        
        if(formPag == 1):
            pagar = pagar - ((pagar * 5)/100);
            desconto = round((pagar * 5)/100, 2);
        else:
            desconto = "0.00";
    elif(prod == 2):
        valKg = 6.80;
        pagar = (qtd * valKg);
        prodT = "Alcatra";

        if(formPag == 1):
            pagar = pagar - ((pagar * 5)/100);
            desconto = round((pagar * 5)/100, 2);
        else:
            desconto = "0.00";
    elif(prod == 3):
        valKg = 7.80;
        pagar = (qtd * valKg);
        prodT = "Picanha";

        if(formPag == 1):
            pagar = pagar - ((pagar * 5)/100);
            desconto = (round(pagar * 5)/100, 2);
        else:
            desconto = "0.00";



print("\n\n****** NOTA FISCAL ******");
print("Produto        Qtd.     Valor 1Kg    Valor Total");
print(prodT, "      ",qtd  ,"Kg     R$", valKg,"      R$ ",round((qtd * valKg), 2));
print("\nDescontos: R$", desconto);
print("Total a pagar: R$",round(pagar, 2));
print("****** *********** ******");
