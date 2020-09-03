h = float(input("Digite a sua altura: "));

pesoIdealH = round((72.7 * h) - 58, 2);
pesoIdealM = round((61.1 * h) - 44.7, 2);

print("Peso ideal Homem: %s" % pesoIdealH);
print("Peso ideal Mulher: %s" % pesoIdealM);
