from numpy import *

from numpy.random import *

from matplotlib.pyplot import *

print ("Podaj ile punktów ma mieć wykres:")
xy = int(input())

show()

x = linspace(0, 20, xy)

y = (4*x)**2 +3*x+1
plot(x, y)

show()

