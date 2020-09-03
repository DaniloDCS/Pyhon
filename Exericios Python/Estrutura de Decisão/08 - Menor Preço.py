p1 = float(input("Valor do 1o produto: "));
p2 = float(input("Digite do 2o produto: "));
p3 = float(input("Digite do 3o produto: "));

if(p1 < p2 and p1 < p2):
    print("Você deve comprar o 1o Produto: R$", p1);
elif(p2 < p1 and p2 < p3):
    print("Você deve comprar o 2o Produto: R$", p2);
else:
    print("Você deve comprar o 3o Produto: R$", p3);
