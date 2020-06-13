from sympy import *

class Polynomial:
    x, y = symbols('x y')
    array_size  = 0

    x_values = []
    f_values = []

    langrange_eqn = 0
    def add_data(self,val_1=0, val_2=0):
        self.x_values.append(val_1)
        self.f_values.append(val_2)
    def clear_array(self):
        self.x_values.clear()
        self.f_values.clear()
    def execute(self):
        array_size = len(self.x_values)
        self.langrange_eqn = 0
        for L in range(0, array_size):
            expr = 1
            den = 1
            for i in range(array_size - 1, -1, -1):
                if i == L:
                    expr = expand(expr * 1)
                else:
                    expr = expand(expr * (self.x - self.x_values[i]))
                if i == L:
                    den = den * 1
                else:
                    den = (self.x_values[L] -  self.x_values[i]) * den
            self.langrange_eqn = self.langrange_eqn + self.f_values[L] * (1 / den) * expr
            #Polynomial.clear_array(1)
        return  self.langrange_eqn
    def subs_val(self,b):
        val = self.langrange_eqn.subs(self.x, b)
        return val
    def predict(self,val):
        first_order_finite_difference = []
        for j in range (0, val):
            array_size = len(self.f_values)
            for i in range(0, array_size - 1):
                first_order_finite_difference.append(self.f_values[i + 1] - self.f_values[i])

            avg = sum(first_order_finite_difference) / array_size
            self.f_values.append(avg+self.f_values[array_size-1])
            print(self.f_values)
        return int(self.f_values[len(self.f_values)-1])

