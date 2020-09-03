salario = float(input("Valor do salário: "));
              
if(salario <= 900):
    ir = 0;
    fgts  = (salario * 11) / 100;
    sindicato = (salario * 3) / 100;
    inss = (salario * 10) / 100;
    descontos = inss + ir;
    salarioLiquido = salario - descontos;
elif(salario > 900 and salario <= 1500 ):
    ir = (salario * 5) / 100;
    fgts = (salario * 11) / 100;
    inss = (salario * 10) / 100;
    sindicato = (salario * 3) / 100;
    descontos = inss + ir;
    salarioLiquido = salario - descontos;
elif(salario > 1500 and salario <= 2500 ):
    ir = (salario * 10) / 100;
    fgts = (salario * 11) / 100;
    inss = (salario * 10) / 100;
    sindicato = (salario * 3) / 100;
    descontos = inss + ir;
    salarioLiquido = salario - descontos;
elif(salario > 2500):
    ir = (salario * 20) / 100;
    fgts = (salario * 11) / 100;
    inss = (salario * 10) / 100;
    sindicato = (salario * 3) / 100;
    descontos = inss + ir;
    salarioLiquido = salario - descontos;

print("Salario Bruto: ", salario);
print("IR: ", ir);
print("FGTS: ", fgts);
print("INSS: ", inss);
print("Sindicato: ", sindicato);
print("Descontos: ", descontos);
print("Salario Liquido: ", salarioLiquido);



