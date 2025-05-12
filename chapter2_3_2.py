# 2.3. 辞書型
# 2.3.2. 辞書型のメソッド
d = {'x': 10, 'y': 20}

# keysメソッド
print(d.keys())

# valuesメソッド
print(d.values())

# updateメソッド
d = {'x': 10, 'y': 20}
d2 = {'x': 1000, 'j': 500}
d.update(d2)

print(d)

# getメソッド
print(d['x'])
print(d.get('x'))

# NoneType
print(d.get('z'))

# popメソッド
print(d.pop('x'))
print(d)

# del文
del d['y']
print(d)

del d

# clearメソッド
d = {'x': 10, 'y': 20}
d.clear()

print(d)