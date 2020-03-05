# zadanie 10
import sys
# a = int(input("Podaj liczbe = "))
# for i in range(a+1):
#     for j in range(i):
#         sys.stdout.write("A")  
#     sys.stdout.write("\n")

# zadanie 11
# b = int(input("Podaj liczbe = "))
# for i in range(b+1):
#     for j in range(0,b-i):
#         sys.stdout.write(" ")
#     for k in range(0,i+1):
#         sys.stdout.write("*")
#     sys.stdout.write("\n")


c = int(input("Podaj liczbe nieparzysta = "))
p = 1

for i in range(c+1):
    if i<=c/2:  
        for j in range(0,c-i):
            sys.stdout.write(" ")
        for k in range(0,p):
            sys.stdout.write("o")
        p+=2
        sys.stdout.write("\n") 
    else:
        for l in range(c-1,0):
            sys.stdout.write(" ")
        for m in range(p,0):
            sys.stdout.write("o")
        p-=2
        sys.stdout.write("\n")
