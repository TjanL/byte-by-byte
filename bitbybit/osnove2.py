def izpisi_vrsto(text):
    print(text + " ", end="")


def narisi_kvadrat(visina, sirina, znak="#"):
    for v in range(visina):
        for s in range(sirina):
            izpisi_vrsto(znak)
        print()
    print()


file = open("output.txt", "a")
file.write("Hello world!")
file.close()

file = open("output.txt", "r")
print(file.read())
file.close()

with open("output.txt", "r") as file:
    file.write("Hello world!")
    print(file.read())
