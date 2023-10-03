#Novita in 3.9 per la gestione delle stringe: Metodi removeprefix() e removesuffix()
#Sono stati introdotti in aggiunta ai preesistenti lstrip(), rstrip(), strip(), che operano in maniera non sempre
#lineare, rimuovendo da una stringa una qualunque combinazione dei caratteri specificati.
#ad esempio lstrip('abc') rimuove un prefisso 'abc' da una una stringa, ma anche 'bca' o 'acb'.
stringa = "resettare e ritentare"
print(f"stringa = \"{stringa}\"")

stringa2 = 'abcde'
print(f"stringa2 = \"{stringa2}\"")
#removeprefix('re') rimuove esattamente il prefisso "re" dalla stringa
print(f"stringa2.lstrip('cba') = \"{stringa2.lstrip('cba')}\"")

print('#### Invece removeprefix() e removesuffix() rimuovono esattamente la stringa specificata')
#removeprefix('re') rimuove esattamente il prefisso "re" dalla stringa
print(f"stringa.removeprefix('re') = \"{stringa.removeprefix('re')}\"")
#removesuffix('re') rimuove esattamente il suffisso "re" dalla stringa
print(f"stringa.removesuffix('re') = \"{stringa.removesuffix('re')}\"")