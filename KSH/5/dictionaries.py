tel = {'jack': 4098, 'sape': 4139}
print(tel)
print(tel['jack'])
tel['jack'] = 123
print(tel)
del tel['jack']
tel['irv'] = 4127
print(tel)
tel['z'] = 9999
print(list(tel.keys()))
print(sorted(tel.keys()))
print('z' in tel)
print('z' not in tel)
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))