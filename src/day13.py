import math
from sympy.ntheory.modular import crt

tt, ids = open(0).read().splitlines()
ids = [x for x in ids.split(",")]
int_ids = [int(x) for x in ids if x != "x"]

# part 1
print(math.prod(min([(x - int(tt) % x, x) for x in int_ids])))

# part 2
print(crt(int_ids, [-i % int(x) for i, x in enumerate(ids) if x != "x"])[0])
