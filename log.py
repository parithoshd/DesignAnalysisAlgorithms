import math as math

input = [999,1000,9999,10000,99999,100000,999999,1000000]

complexity_value = []

for x in input:
    complx_val = x * (math.log(x,2))
    
    complexity_value.append(complx_val)
    print(x, ", ", complx_val)


