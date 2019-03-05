#Znajdź X i Y, które spełniają: X jest podzielne przez Y i oba X i Y są parzyste// wersja z podawaniem wlasnych liczb
from cs50 import get_int
x = get_int("Podaj x: ")

y = get_int("Podaj y: ")
xIsEven = x % 2 == 0
yIsEven = y % 2 == 0

xIsEvenLog = 'X jest parzyste' if xIsEven else 'X jest nieparzyste'
yIsEvenLog = 'Y jest parzyste' if yIsEven else 'X jest nieparzyste'

print(xIsEvenLog)
print(yIsEvenLog)

if (x%y)==0:
    print("Brak reszty z dzielenia")
else:
    print("Nie są podzielne")