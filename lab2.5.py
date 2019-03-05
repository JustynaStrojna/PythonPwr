#Add rounding for the above x/y operation. Round to 2 decimal points
#v1
print("Wesja 'wszystko w 1 linijce kodu':")
x=(float(input("Podaj X: ")) / float(input("Podaj Y:" ) ) )
print (round(x, 2))
print("-"*10)
#v2
print("Wesja z wyświetleniem wyniku dzielenia:")

from cs50 import get_int
a = get_int("Podaj a: ")
b = get_int("Podaj b: ")
print ("a/b=:", {a/b})
print (round((a/b), 2))