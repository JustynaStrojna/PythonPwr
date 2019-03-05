print ("zadanie 2") #silnia=factorial

print("Podaj dowolną liczbe:")
x = int(input())
factorial=1
if x<0:
    print ("Silnia nie wystepuje dla ujmenych liczb")
elif x==0:
    print ("Silnia dla 0 wynosi 1")
else:
    for i in range (1, x+1):
        factorial=factorial*i
print ('Silnia liczby',x, 'wynosi', factorial)