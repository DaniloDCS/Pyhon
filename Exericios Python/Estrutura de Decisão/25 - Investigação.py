print("Responder com s(sim) e n(não)!");
p1 = input("Telefonou para a vítima? ");
p2 = input("Esteve no local do crime? ");
p3 = input("Mora perto da vítima? ");
p4 = input("Devia para a vítima? ");
p5 = input("Já trabalhou com a vítima? ");

if(p1 == 's'):
    x = 1;
else:
    x = 0;
    
if(p2 == 's'):
    x = x + 1;
else:
    x = x + 0;
    
if(p3 == 's'):
    x = x + 1;
else:
    x = x + 0;
  
if(p4 == 's'):
    x = x + 1;
else:
    x = x + 0;
    
if(p5 == 's'):
    x = x + 1;
else:
    x = x + 0;

if(x == 2):
    print("Suspeito(a)");
elif(x >= 3 and x <= 4):
    print("Cúmplice");
elif(x == 5):
    print("Assasino");
else:
    print("Inocente");
 








    
  
