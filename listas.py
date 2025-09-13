muebles = ['mesa', 'silla', 'armario', 'estante', 'banco', 'escritorio']
a = muebles[0:len(muebles)//2]
print(a)
print('banca' in muebles)

varios = [10, "hola", 3.6, True]

furniture = ['table', 'chair', 'rack', 'shelf']
table, chair, rack, shelf = furniture
table, chair, rack, shelf = ['table', 'chair', 'rack', 'shelf']

e = 10
f = 20

tmp = e
e = f
f = tmp
print(e, ' ', f)

e,f = f, e
print(e, ' ', f)