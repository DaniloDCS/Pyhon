gh = float(input("Digite o valor da hora trabalhada: "));
ht = float(input("Digite o quantas horas vc trabalhou: "));

salarioBruto = gh * ht;
inss = (salarioBruto * 8) / 100;
ir = (salarioBruto * 11) / 100;
sindicato = (salarioBruto * 5) / 100;
salarioLiquido = salarioBruto - (inss + ir + sindicato);

print("salario Bruto: R$%s " % salarioBruto);
print("Imposto de Renda: R$%s " % ir);
print("INSS: R$%s " % inss);
print("Sindicato: R$%s " % sindicato);
print("salario Liquido: R$%s " % salarioLiquido);
