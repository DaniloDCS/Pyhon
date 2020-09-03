import math

m = float(input("Digite a area em m2: "));

litrosNecessarios = int(round(m / 3 + 0.5)); 
latas18Qtd = math.ceil(litrosNecessarios / 18);
latas36Qtd = math.ceil(litrosNecessarios / 3.6);
pagarLatas18 = latas18Qtd * 80;
pagarLatas36 = latas36Qtd * 35;
sobra18 = (latas18Qtd * 18) - litrosNecessarios;
sobra36 = (latas36Qtd * 3.6) - litrosNecessarios;

print("Voce precisará de litros ", litrosNecessarios);
print("Voce precisará de ", latas18Qtd, " latas de tinta de 18L, pagrá R$", pagarLatas18, " sobrará ", sobra18, " litros.");
print("Voce precisará de ", latas36Qtd, " latas de tinta de 3.6L, pagrá R$", pagarLatas36, " sobrará ", sobra36, " litros.");
