
a = [4,8,15,16,23,42]
b = ['4','8','15','16','23','42']

print(a)
print(b)

c = [float(x) for x in b]
print( c )
print('-'*30)

print(a.index(16))

n = {'plane':1, 'double':2, 'triple':3}['triple']
print(n)