from Langrange import Polynomial

polynomial = Polynomial()
for i in range(10):
    #Adding data of y = x^2
    polynomial.add_data(i,i*2)
print(polynomial.execute())
