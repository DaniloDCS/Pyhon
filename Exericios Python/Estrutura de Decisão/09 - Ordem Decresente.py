num1 = float(input("Digite o 1o numero: "));
num2 = float(input("Digite o 2o numero: "));
num3 = float(input("Digite o 3o numero: "));

if(num1 >= num2 and num1 >= num3):
    print(num1);
elif(num2 >= num1 and num2 >= num3):
    print(num2);
elif(num3 >= num1 and num3 >= num1):
    print(num3);

if(num1 > num2 and num1 < num3):
    print(num1);
elif(num1 < num2 and num1 > num3):
    print(num1);
elif(num1 < num2 and num1 < num3):
    print(num1);
elif(num2 > num1 and num2 < num3):
    print(num2);
elif(num2 < num1 and num2 > num3):
    print(num2);
elif(num2 < num1 and num2 < num3):
    print(num2);
elif(num3 > num1 and num3 < num1):
    print(num3);
elif(num3 < num1 and num3 > num1):
    print(num3);
elif(num3 < num1 and num3 < num1):
    print(num3);


if(num1 <= num2 and num1 <= num3):
    print(num1);
elif(num2 <= num1 and num2 <= num3):
    print(num2);
elif(num3 <= num1 and num3 <= num1):
    print(num3);
