data = input("Digite uma data no formato dd/mm/aaaa: ");

dia = int(data[0]+data[1]);
mes = int(data[3]+data[4]);
ano = int(data[6]+data[7]+data[8]+data[9]);

if(dia > 0 and dia <= 31 and mes > 0 and mes <= 12 and ano > 0):
    if(dia < 31 and (mes == 4 or mes == 6 or mes == 9 or mes == 11)):
        print("Essa data é verdadeira");
    elif(dia <= 31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12)):
        print("Essa data é verdadeira");
    elif(mes == 2):
        if(dia <= 29 and (ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0)):
            print("Essa data é verdadeira");
        elif(dia <= 28):
            print("Essa data é verdadeira");
        else:
            print("Essa data não é verdadeira");
    else:
        print("Essa data não é verdadeira");
else:
    print("Essa data não é verdadeira");

        
