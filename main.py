"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Michal Marvan
email: marvan.michal@gmail.com
discord: Michal_M
"""

# zadání textů k analýze

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

# Vytvoření seznamu uživatelů a jejich hesel, kteří mohou analýzu spustit

UZIVATELE = {
    "bob" : "123",
    "ann":"pass123",
    "mike":"password123",
    "liz": "pass123",
    }

# Zadání uživatelských informací (jméno, heslo)

uzivatelske_jmeno = input('Zadejte své uživatelské jméno:')
heslo = input("Zadejte své heslo:")
print("-"*35)

# Kód, který ověří, zda se přihlásil správný uživatel
## První if pro uživatelské jméno, druhé if a else pro heslo

if uzivatelske_jmeno in UZIVATELE.keys():
  if UZIVATELE.get(uzivatelske_jmeno) == heslo:
    print("Vítejte uživateli", uzivatelske_jmeno)
  else:
    print("Uživatel není registrovaný.", "Program ukončen", sep = "\n")
    exit()
else:
  print("Uživatel není registrovaný.", "Program ukončen", sep = "\n")
  exit()

print("Máme pro vás 3 texty k analýze." , "-" * 35, sep = '\n')

# Zadání čísla textu uživatelem

cislo_textu = int(input("Zadejte číslo od 1 do 3 k výběru textu: "))

# Výpis vybraného textu na základě vybraného čísla

if cislo_textu in (1, 2, 3):
  print("-"*35, "Váš vybraný text je: ", TEXTS[cislo_textu - 1], "-"*35, sep = '\n')
else:
  print("Vybral jste špatné číslo!")
  exit()

# PRÁCE S TEXTEM:

# Příprava slov pro analýzu
# Rozdělení celého stringu na jednotlivá slova pomocí mezery

vsechna_slova = TEXTS[cislo_textu - 1].split()

# Očištění jedsnotlivých slov o tečky a čárky, které mohou dělat později při analýze problémy

slova = []
slova = [slovo.rstrip('.,') for slovo in vsechna_slova]

# alternativně lze také zapsat jako normální for cyklus ne jen jako jednořádkový:
# for slova_bez_tecky in vsechna_slova:
#  slova.append(slova_bez_tecky.rstrip('.,'))

# Vypsání počtu slov v textu

print("Ve vybraném textu se nachází", len(slova), "slov")

# Vypsání počtu slov začínající velkým písmenem

pocet_titulnich_slov = 0
for titulni_slova in slova:
  if titulni_slova.istitle() == True:
    pocet_titulnich_slov = pocet_titulnich_slov + 1

print("Ve vybraném textu se nachází", pocet_titulnich_slov, "titulních slov")

# Vypsání počtu slov, která obsahují pouze VELKÁ písmena

pocet_velkych_slov = 0
for velka_slova in slova:
  if velka_slova.isupper() == True and velka_slova.isalpha() == True:
    pocet_velkych_slov = pocet_velkych_slov + 1

print("Ve vybraném textu se nachází", pocet_velkych_slov, "slovo/a s velkými písmeny")

# Vypsání počtu slov, která obsahují pouze malá písmena

pocet_malych_slov = 0
for mala_slova in slova:
  if mala_slova.islower() == True and mala_slova.isalpha() == True:
    pocet_malych_slov = pocet_malych_slov + 1

print("Ve vybraném textu se nachází", pocet_malych_slov, "slovo/a s malými písmeny")

# Vypsání počtu číselných stringů v textu a následné vypsání jejich součtu

pocet_cisel = 0
cislelne_hodnoty = []

for cisla in slova:
  if cisla.isdigit() == True:
    pocet_cisel = pocet_cisel + 1
    cislelne_hodnoty.append(int(cisla))

print("Ve vybraném textu se nachází", pocet_cisel, "čísla")
print("Součet všech čísel je:", sum(cislelne_hodnoty))

# Vypsání sloupcového grafu s četností různých délek slov
## zjištění délek jednotlivých slov

delky_slov = []

for delky in slova:
  delky_slov.append(len(delky))

# vypočítání cetnosti slov

cetnost_slov = dict ()

for pocty in delky_slov:
    if pocty not in cetnost_slov:
        cetnost_slov[pocty] = 1
    else:
        cetnost_slov[pocty] = cetnost_slov[pocty] + 1

# vytvoření grafu na základě délek a četností slov

print("-" * 35,
      f"{'DÉLKA':<6}|{'ČETNOST GRAF.':<20}|{'ČETNOST':>6}",
      "-" * 35,
      sep = "\n")

for index, (delka, pocet) in enumerate(sorted(cetnost_slov.items()), start = 1):
    print(
        f"{index:<6}|{'*' * int(pocet):<20}|{pocet}",
        sep="\n")