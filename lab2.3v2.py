#Znajdź X i Y, które spełniają: X jest podzielne przez Y i oba X i Y są parzyste

import random
for n in range(1):
    x = random.randint(1,101)
    print ("Wylosowana wartość x:", x)

for k in range(1):
    y = random.randint(1,101)
    print ("Wylosowana wartość y:", y)

xIsEven = x % 2 == 0
yIsEven = y % 2 == 0

xIsEvenLog = 'X jest parzyste' if xIsEven else 'X jest nieparzyste'
yIsEvenLog = 'Y jest parzyste' if yIsEven else 'Y jest nieparzyste'

print(xIsEvenLog)
print(yIsEvenLog)

if (x%y)==0:
    print("Brak reszty z dzielenia-znalezione rozwiązanie")
else:
    print("Nie są podzielne")