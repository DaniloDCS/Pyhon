salario = float(input("Valor do seu salário: "));
reajuste = 0;
percentual = 0;

                
if(salario <= 280):
    reajuste = salario + ((salario * 20) / 100);
    percentual = 20;
elif(salario > 280 and salario <= 700):
    reajuste = salario + ((salario * 15) / 100);
    percentual = 15;
elif(salario > 700 and salario <= 1500):
    reajuste = salario + ((salario * 10) / 100);
    percentual = 10;
elif(salario > 1500):
    reajuste = salario + ((salario * 5) / 100);
    percentual = 5;
    
print("O seu sálario era de",salario,
      "com o reajuste de",percentual,
      "% passou a ser de R$",reajuste,
      "aumento de R$", reajuste - salario);


