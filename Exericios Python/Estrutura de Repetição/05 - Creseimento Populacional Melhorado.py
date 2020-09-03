x = 0;
y = 2;
while x < y:
    popA = int(input("\nQuantidade de pessoas da População 1: "));
    popB = int(input("Quantidade de pessoas da População 2: "));

    print("População A inicial: ", popA);
    print("População B inicial: ", popB);

    a = 0;
    b = 2;
    anos = 0;
    
    while a < b:    
        if(popA >= popB):
            print("\nPara que a Poupulação A ultrapasse a População B levará",anos,"anos\n");        
            print("População A final: ", int(popA));
            print("População B final: ", int(popB));
            a = 2;
        else:
            popA = popA + (popA * 3)/100;
            popB = popB + (popB * 1.5)/100;
            anos = anos + 1;  
            a = 0;

    repeat = input("\Deseja realizar outra operação: s para SIM e n para NÃO: ");

    if(repeat == "s"):
        x = 0;
    else:
        x = 2;

 

