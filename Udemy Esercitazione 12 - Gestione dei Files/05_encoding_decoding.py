#conversione, codifica o decodifica, esplicita da stringhe a bytes e viceversa

x = 'sequenza' #x è un literal di tipo string
print(f'Tipo di x è: {type(x)}')
y = x.encode('utf-8')
print(f'Tipo di y (encode di x) è: {type(y)}')


print('###############')

x = b'sequenza' #x è un literal di tipo bytes
print(f'Tipo di x è: {type(x)}')
y = x.decode('utf-8')
print(f'Tipo di y (encode di x) è: {type(y)}')
