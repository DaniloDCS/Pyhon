num = input("Digite um número menor que 1000: ");

if(len(num) == 3):
    centena = int(num[0]);
    dezena = int(num[1]);
    unidade = int(num[2]);
    if(centena < 2 and  dezena < 2 and unidade < 2):
        print(centena, "centena,", dezena, "dezena e", unidade, "unidade");
    elif(centena > 1 and dezena > 1 and unidade > 1):
        print(centena, "centenas,", dezena, "dezenas e", unidade, "unidades");
    elif(centena > 1 and dezena < 2 and unidade < 2):
        print(centena, "centenas,", dezena, "dezena e", unidade, "unidade");
    elif(centena < 2 and dezena > 1 and unidade < 2):
        print(centena, "centena,", dezena, "dezenas e", unidade, "unidade");
    elif(centena < 2 and dezena < 2 and unidade > 1):
        print(centena, "centena,", dezena, "dezena e", unidade, "unidades");
    elif(centena > 1 and dezena < 2 and unidade > 1):
        print(centena, "centenas,", dezena, "dezena e", unidade, "unidades");
    elif(centena > 1 and dezena > 1 and unidade < 2):
        print(centena, "centenas,", dezena, "dezenas e", unidade, "unidade");
    elif(centena < 2 and dezena > 1 and unidade > 1):
        print(centena, "centena,", dezena, "dezenas e", unidade, "unidades");
    elif(centena > 1 and dezena > 2 and unidade < 1):
        print(centena, "centenas,", dezena, "dezenas e", unidade, "unidade");
elif(len(num) == 2):
    dezena = int(num[0]);
    unidade = int(num[1]);
    if(dezena < 2 and unidade < 2):
        print(dezena, "dezena e", unidade, "unidade");
    elif(dezena > 1 and unidade > 1):
        print(dezena, "dezenas e", unidade, "unidades");
    elif(dezena > 1 and unidade < 2):
        print(dezena, "dezenas e", unidade, "unidade");
    elif(dezena < 2 and unidade > 1):
        print(dezena, "dezena e", unidade, "unidades");
elif(len(num) == 1):
    unidade = int(num[0]);
    if(unidade <= 1):
        print(unidade, "unidades");
    else:
        print(unidade, "unidade");
else:
    print(num, "não é menor que 1000");









    
