import math as math

input = [999,1000,9999,10000,99999,100000,999999,1000000]
theory_values = [9954.376526924627,  9965.784284662088,  132862.3934602112,  132877.1237954945,  1660945.9951153793,  1660964.0474436812,  19931547.195061285,19931568.569324173]
expiremental_values = [3436000,2967000,33549000,33973000,471685000,476321000,9670140000,9127986000]

theory_normalized = []
expiremental_normalized = []

for x in theory_values:
    min_val = min(theory_values)
    max_val = max(theory_values)
    x_changed = (x - min_val) / (max_val - min_val)
    theory_normalized.append(x_changed)

for x in expiremental_values:
    min_val = min(expiremental_values)
    max_val = max(expiremental_values)
    x_changed = (x - min_val) / (max_val - min_val)
    expiremental_normalized.append(x_changed)


for x in theory_normalized:
    print(x)

print("--------")

for x in expiremental_normalized:
    print(x)
