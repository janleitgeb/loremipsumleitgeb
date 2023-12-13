import random

lortext = ["Kouzlo", "Voda", "Otevřít", "Vystoupit", "Zabít kouzlem", "Výbuch", "Mučení", "Sestoupit", "Postavit", "Vykázat zbraní", "Kopie", "Skákání", "Ovládnutí mysli", "Světlo", "Zatemnit", "Zničit", "Ztišit", "Šimrání", "Zelený světelný paprsek", "Zvednout", "Zapomenout", "Jez slimáky", "TopG", "Fakt", "Je", "Mamina", "Krabice", "Kočka", "Hovadina", "Loremipsum", "příklad", "programování", "Python", "kód", "úprava", "český", "věta"]

while True:
    pocet_vet = int(input("\nKolik vět chcete generovat?: "))

    text = []
    i = 0
    while i < pocet_vet:
        pocet_slov = random.randint(4, 11)
        pocet_slov_ve_vete = random.sample(lortext, pocet_slov)
        
        if random.choice([True, False]):
            sprosta_slova = random.choice(["Sakra", "Hovno", "Prdel", "Kunda", "Kurva", "Losert Dopiče", "Píča"])
            pocet_slov_ve_vete.insert(random.randint(0, pocet_slov), sprosta_slova)

        veta = " ".join(pocet_slov_ve_vete).capitalize() + ".\n"
        text.append(veta)
        i += 1

    finito = " ".join(text)
    print(finito)

    ulozit_do_souboru = input("Chcete uložit vygenerovaný text do souboru? (ano/ne): ").lower()
    
    if ulozit_do_souboru == 'ano':
        nazev_souboru = input("Zadejte název souboru: ")
        soubor = open(nazev_souboru, "w", encoding="utf-8")
        soubor.write(finito)
        soubor.close()
        print(f"Generovaný lorem ipsum byl uložen do souboru s názvem: {nazev_souboru}")
    
    znova = input("Chcete vygenerovat znovu? (ano/ne): ").lower()
    if znova != 'ano':
        break
