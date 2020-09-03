x = 1;

while x < 2:
    nomeUser = input("Insira o seu nome de Usuário: ");
    senhaUser = input("Insira uma sua senha: ");
                 
    if(senhaUser.lower() != nomeUser.lower()):
        x = 2;
        print("Sucesso ao fazer login!");
    else:
        print("\nErro. Digite novamente! Senha não pode ser igual ao nome usuario.\n");
        x = 1;
