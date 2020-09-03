x = 1;

while x < 2:
    nomeUser = input("Insira o seu nome de Usuário: ");
    idadeUser = int(input("Insira sua idade: "));
    salarioUser = float(input("Insira o valor do seu salário: "));
    sexoUser = input("Insira o seu sexo \nm - Masculino f - femenino o - ouros: ");
    estadoCivil = input("Insira o seu estado civil\ns - solteiro c - casado d - divorciado v - viuvo: ");             


    if(len(nomeUser) > 3 and
       (idadeUser >= 0 or idadeUser < 150) and
       salarioUser > 0 and
       (sexoUser == "m" or sexoUser == "f" or sexoUser == "o") and
       (estadoCivil == "c" or estadoCivil == "v" or estadoCivil == "s" or estadoCivil == "d")):

        x = 2;
        print("Sucesso ao fazer login!");
    else:
        print("Informações não são válidas\n");
        x = 1;
