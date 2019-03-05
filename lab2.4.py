#Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'

def czy_podzielne():


    if int(input("Podaj X: ")) % int(input("Podaj Y: ")) == 0:
        print("X jest podzielne")
    else:
        print("X nie jest podzielne")


czy_podzielne() #wywołanie

#sposób v2


print("a:")
a = int(input())
print("b:")
b = int(input())

Podzielne = a % b == 0
xIsEvenLog = 'A jest podzielne' if Podzielne else 'A jest niepodzielne'
print(xIsEvenLog)