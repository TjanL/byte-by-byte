# Tipi spremenljivki
stevilo = 123
stevilo_z_vejico = 123.456
beseda = "beseda"
formatirano_besedilo = f"formatirana {beseda}"
prazna_vrednost = None

# Operacije
sestevanje = stevilo + stevilo_z_vejico
print(sestevanje)

mnozenje = stevilo * stevilo
print(mnozenje)

sestavljanje = beseda + beseda
print(sestavljanje)

print(formatirano_besedilo)
print(prazna_vrednost)

# Zanke
while stevilo > 0:
    print(stevilo)
    stevilo = stevilo - 1

stranica = 10
for vrstica in range(stranica):
    for j in range(stranica):
        if j == 0:
            print("*", end="")
        elif vrstica == stranica - 1:
            print("*", end="")
        elif vrstica == j:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Seznam
a = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
]

for vrstica in a:
    for stevilo in vrstica:
        print(stevilo)

## Stevilo stolpcev
print(len(a))
## Stevilo elementov v prvem stolpcu
print(len(a[0]))

## Iskanje v seznamu
if 10 in a:
    print("10 je v seznamu")

# Seznam
d = {"a": 1, "b": ["dasda", "asdad"], "c": 3}

print(d["a"])
print(d["b"][1])
print(d.get("aasdasd"))
del d["b"]

# Set
b = set([2131, 312, 1231231, 123123, 12, 12, 1, 3])
a = set([1, 2, 3])
print(b.issuperset(a))

# Knjiznice
import math

r = 2
povrsina_kroga = math.pi * math.pow(r, 2)
print(povrsina_kroga)

a = 1
b = 2
c = 3
povrsina_trikotnika = math.sqrt(math.pow(a, 2) + math.pow(b, 2) + math.pow(c, 2))
print(povrsina_trikotnika)
