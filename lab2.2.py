#oblicz pole Perimeter i  obwód Field dwóch okręgów, przy zadanych promieniach X i Y
from cs50 import get_int
from numpy import *
X = get_int("Podaj promień koła X: ")
print(' '*10)
print(f"Pole koła X wynosi: {pi*X**2}")
print(f"Obwód koła X wynosi:{2*pi*X}")
print('-'*10)
Y = get_int("Podaj promień koła Y: ")
print(' '*10)
print(f"Pole koła Y wynosi: {pi*Y**2}")
print(f"Obwód koła Y wynosi:{2*pi*Y}")