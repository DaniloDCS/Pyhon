num1 = float(input("Digite o 1o numero: "));
num2 = float(input("Digite o 2o numero: "));
num3 = float(input("Digite o 2o numero: "));

if(num1 > num2 and num1 > num3):
    print(num1, " é maior");
elif(num2 > num1 and num2 > num3):
    print(num2, " é maior");
else:
    print(num3, " é maior");
