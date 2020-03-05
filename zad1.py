import sys
a = int(input("Podaj liczbe = "))
for i in range(a+1):
    for j in range(i):
        sys.stdout.write("A")  
    sys.stdout.write("\n")
