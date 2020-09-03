a = 0;
b = 0;
c = 1;

while a < 500:
    a = b + c;
    b = c;
    c = a;
    print(a);
