a = 0;
b = 0;
c = 1;
for x in range(0, 10):
    a = b + c;
    b = c;
    c = a;

    print(a);
