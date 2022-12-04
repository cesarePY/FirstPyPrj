# "w": Write  => sovrascrive, se non esist viene creato, se esiste viene rimosso e ricreato
# "a": Append => accoda, se non esiste viene creato, se esiste viene aperto e puntatore a fine file
# "x": Exclusive => se non esiste viene creato, se esiste viene generata un'eccezione, per impedire sovrascrittura file esistenti
# "wb", "ab", "xb": come sopra, ma binario
# "r+", "rb+": Read/Write
# "w+", "wb+": Read/Write
# "a+", "ab+": Append/Write