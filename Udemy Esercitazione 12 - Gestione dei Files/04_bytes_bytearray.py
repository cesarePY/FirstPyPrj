s = b'sequenza' #il prefisso "b" caratterizza s come tipo bytes
print(f'Tipo di s è: {type(s)}')
print(s)

print('###############')
s = bytearray('sequenza','utf-8') #bytearray è un tipo mutabile, mentre bytes è immutabile
s.extend(b' di bytes') #è quindi possibile modificarlo, come in questo caso, appendendo un bytes
print(s)
