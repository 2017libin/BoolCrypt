from boolcrypt.utilities import *
from sage.all import *
import sage.all
entries = [\
[1, 0, 0, 0, 1, 1, 1, 1], [1, 1, 0, 0, 0, 1, 1, 1], [1, 1, 1, 0, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0, 0, 1],\
[1, 1, 1, 1, 1, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 1, 1, 1, 1, 1]]

bin_matrix = matrix(GF(2), 8, 8, entries)
ct = get_rijndael_field().fetch_int(vector2int([1, 1, 0 ,0, 0, 1, 1, 0]))
poly = matrix2poly(bin_matrix, get_rijndael_field())

poly = matrix2poly(sage.all.identity_matrix(GF(2), 4), GF(2**4))
print(poly)