print complex(real=3, imag=4)
print complex(**{'imag':2, 'real':5})
print complex(2, 7)
print complex(*(5, 6))

print coerce(3, 4.2)
print coerce(2, 3)
print coerce(2+3j, 3)

import operator

print operator.add(*coerce(2, 4.3))