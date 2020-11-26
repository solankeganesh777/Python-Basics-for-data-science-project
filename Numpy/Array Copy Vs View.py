#Array Copy vs View

# copy owns the data and any changes made to the copy will not affect original array,
# and any changes made to the original array will not affect the copy

import numpy as np

b=np.array([55,6,3,5,8])
print(b)
a=b.copy()
print(a)

b[0]=100
print(b)
print(a)
print("\n")

#view does not own the data and any changes made to the view will affect the original array,
# and any changes made to the original array will affect the view

b=np.array([55,6,3,5,8])
print(b)
a=b.view()
print(a)

b[0]=100
print(b)
print(a)
print("\n")

# base attribute:Returns None if the array owns the data.
# Otherwise, the base  attribute refers to the original object

p=np.array([5,4,3,2])
q=p.copy()
r=p.view()

print(q.base)
print(r.base)
