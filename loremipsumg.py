import random

lortext = ["Kouzlo", "Voda", "Otevřít", "Vystoupit", "Zabít kouzlem", "Výbuch", "Mučení", "Sestoupit", "Postavit", "Vykázat zbraní", "Kopie", "Skákání", "Ovládnutí mysli", "Světlo", "Zatemnit", "Zničit", "Ztišit", "Šimrání", "Zelený světelný paprsek", "Zvednout", "Zapomenout", "Jez slimáky", "TopG", "Fakt", "Je", "Mamina", "Krabice", "Kočka", "Hovadina", "Loremipsum", "příklad", "programování", "Python", "kód", "úprava", "český", "věta"]

pocet_vet = int(input("\nkolik vět chcete generovat?: "))      #otazka programu na poctu generovaych vet

text = []
i = 0
while i < pocet_vet:
    pocet_slov = random.randint(4, 11)     #nahodne vylosovani, kolik jedna veta bude mit slov v rozmezi 4 az 11 slov
    pocet_slov_ve_vete = random.sample(lortext, pocet_slov)
    
    if random.choice([True, False]):
        sprosta_slova = random.choice(["Sakra", "Hovno", "Prdel", "Kunda", "Kurva", "Losert Dopiče", "Píča", ])    #nahodna explicitni slova dle meho gusta :)
        pocet_slov_ve_vete.insert(random.randint(0, pocet_slov), sprosta_slova)

    veta = " ".join(pocet_slov_ve_vete).capitalize() + ".\n"   #oddeli kazdou vetu teckou a funkce capitalize na zacatku da velke pismeno a zbytek malym
    text.append(veta)
    i += 1

finito = " ".join(text)
print(finito)  #vypis vet


nazev_soboru = "loremipsumleitgeb.txt"

soubor = open(nazev_soboru, "w", encoding = "utf-8")
soubor.write(finito)
soubor.close()

print(f"Generovaný lorem ipsum je v souboru s názvem: {nazev_soboru}")

  #toto mel byt pokus na ulozeni souboru vygenerovanyho do .txt souboru, nejak se tomu nekdy chce nekdy ne