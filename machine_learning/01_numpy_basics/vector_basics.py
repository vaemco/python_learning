import numpy as np

mengen = np.array( [2.5, 1.0, 0.5] )
preise = np.array( [2.0, 1.5, 6.0] )
discount = 0.9
raw_total = mengen * preise
discounted_total = raw_total * discount
final_total = np.sum(discounted_total)  
print(f"Der rabatt ware: {discounted_total} und die finale summe ist: {final_total}")