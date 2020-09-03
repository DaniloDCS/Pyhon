op1 = float(input("Digite o 1o numero: "));
op2 = float(input("Digite o 2o numero: "));
oper = input("Qual operação  deseja realizar? \n+ = Soma\n- = Subtração\n* = Multiplicação\n/ = Divisão\n\nQual? ");

if(oper == '+'):
    result = round(op1 + op2, 1);
elif(oper == '-'):
    result = round(op1 - op2, 1);
elif(oper == '*'):
    result = round(op1 * op2, 1);
elif(oper == '/'):
    result = round(op1 / op2, 1);
else:
    print("Opção inválida!");


if(result > 0 and (result / result == 1) and (result % 2 == 0)):
    print("Resultado:",result, "Postivo, Inteiro e Par");
elif(result < 0 and (abs(int(result)) / abs(result) == 1) and (abs(result) % 2 == 0)):
    print("Resultado:",result, "Negativo, Inteiro e Par");
elif(result > 0 and (int(result) / result == 1) and (result % 2 != 0)):
    print("Resultado:",result, "Postivo, Inteiro e Impar");
elif(result < 0 and (abs(result) / int(abs(result)) == 1) and (result % 2 != 0)):
    print("Resultado:",result, "Negativo, Inteiro e Impar");
elif(result > 0 and (result / int(result) != 1)):
    print("Resultado:",result, "Positivo e Decimal");
elif(result < 0 and (result / int(result) != 1)):
    print("Resultado:",result, "Negativo e Decimal");







