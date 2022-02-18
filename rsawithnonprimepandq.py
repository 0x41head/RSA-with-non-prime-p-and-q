
from factordb.factordb import FactorDB

n=57436275279999211772332390260389123467061581271245121044959385707165571981686310741298519009630482399016808156120999964
e= 65537
ct=25287942932936198887822866306739577372124406139134641253461396979278534624726135258660588590323101498005293149770225633

f = FactorDB(n)
f.connect()
primes = f.get_factor_from_api()

print(primes)
phi = 1

for _ in primes:
	p = int(_[0])
	exp = _[1]

	phi *= (p ** (exp - 1)) * (p-1)

pt = pow(ct, pow(65537, -1, phi), n)

from Crypto.Util.number import long_to_bytes

flag = long_to_bytes(pt)
print(flag)
