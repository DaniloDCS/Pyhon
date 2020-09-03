popA = 80000;
popB = 200000;

print("População A inicial: ", popA);
print("População B inicial: ", popB);

a = 0;
b = 2;

anos = 0; 
while a < b:
    if(popA >= popB):
        a = 2;
        print("\nPara que a Poupulação A ultrapasse a População B levará",anos,"anos\n");        
        print("População A final: ", int(popA));
        print("População B final: ", int(popB));
    else:
        popA = popA + (popA * 3)/100;
        popB = popB + (popB * 1.5)/100;
        anos = anos + 1;  
        a = 0;
