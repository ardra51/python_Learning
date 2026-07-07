'''
#shallow copy

import copy
k = [[23,"kochi"],["one team",19]]
n = k
n[0][1]="python"
n = copy.copy(k)
print(k)
print(n)
'''

#deep copy
'''
import copy
k = [[23,"kochi"],["one team",19]]
n = k
n = copy.deepcopy(k)
print(n)

'''