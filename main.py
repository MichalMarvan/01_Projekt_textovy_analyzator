"""
main.py: první projekt do Engeto Online Python Akademie
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

if uzivatelske_jmeno in UZIVATELE and UZIVATELE[uzivatelske_jmeno] == heslo:
    print("Vítejte uživateli", uzivatelske_jmeno)
else:
    print("Uživatel není registrovaný.", "Program ukončen", sep="\n")
    exit()

print(f'{"Máme pro vás"} {len(TEXTS)} {"texty k analýze."}', "-" * 35, sep="\n")

# Zadání čísla textu uživatelem

cislo_textu = input(f'{"Zadejte číslo od 1 do"} {len(TEXTS)} {"k výběru textu: "}')

# Výpis vybraného textu na základě vybraného čísla

if cislo_textu.isdigit() and cislo_textu in [str(n+1) for n in range(len(TEXTS))]:
  print("-"*35, "Váš vybraný text je: ", TEXTS[int(cislo_textu) - 1], "-"*35, sep = '\n')
else:
  print("Nezadal jste správný znak. Jsou brány pouze čísla od 1 do", len(TEXTS) ,"- program bude ukončen.")
  exit()

# PRÁCE S TEXTEM:

# Příprava slov pro analýzu
# Rozdělení celého stringu na jednotlivá slova pomocí mezery

vsechna_slova = TEXTS[int(cislo_textu) - 1].split()

# Očištění jedsnotlivých slov o tečky a čárky, které mohou dělat později při analýze problémy
# dále přidání různých dalších ¨symbolů, které mohou být ve větách a na konci vět (? ! ; : _ - ")

slova = list(slovo.strip('.,?!;:_-"') for slovo in vsechna_slova)

# alternativně lze také zapsat jako normální for cyklus ne jen jako jednořádkový:
# for slova_bez_tecky in vsechna_slova:
#  slova.append(slova_bez_tecky.rstrip('.,'))

pocet_titulnich_slov = 0
pocet_velkych_slov = 0
pocet_malych_slov = 0
pocet_cisel = 0
cislelne_hodnoty = []
delky_slov = []
cetnost_slov = dict ()

for vsechna_slova in slova:  
# Vypsání počtu slov, která obsahují pouze slova s velkým počáteřčním písmenem
  if (vsechna_slova.isupper() == True or vsechna_slova.istitle() == True) and vsechna_slova.isalpha() == True:
    pocet_titulnich_slov += 1
# Vypsání počtu slov, která obsahují pouze VELKÁ písmena 
  if vsechna_slova.isupper() == True and vsechna_slova.isalpha() == True:
    pocet_velkych_slov += 1
# Vypsání počtu slov, která obsahují pouze malá písmena
  if vsechna_slova.islower() == True and vsechna_slova.isalpha() == True:
    pocet_malych_slov += 1
# Vypsání počtu číselných stringů v textu a následné vypsání jejich součtu
  if vsechna_slova.isdigit() == True:
    pocet_cisel += 1
    cislelne_hodnoty.append(int(vsechna_slova))
# zjištění délek jednotlivých slov
  delky_slov.append(len(vsechna_slova))

# souhrn výsledků
print("Ve vybraném textu se nachází", len(slova), "slov")
print("Ve vybraném textu se nachází", pocet_titulnich_slov, "titulních slov")
print("Ve vybraném textu se nachází", pocet_velkych_slov, "slovo/a s velkými písmeny")
print("Ve vybraném textu se nachází", pocet_malych_slov, "slovo/a s malými písmeny")
print("Ve vybraném textu se nachází", pocet_cisel, "čísla")
print("Součet všech čísel je:", sum(cislelne_hodnoty))

# vypočítání četnosti slov

for pocty in delky_slov:
    if pocty not in cetnost_slov:
        cetnost_slov[pocty] = 1
    else:
        cetnost_slov[pocty] += 1

# vytvoření grafu na základě délek a četností slov

print("-" * 35,
      f"{'DÉLKA':<6}|{'ČETNOST GRAF.':<20}|{'ČETNOST':>6}",
      "-" * 35,
      sep = "\n")

for index, (delka, pocet) in enumerate(sorted(cetnost_slov.items()), start = 1):
    print(
        f"{index:<6}|{'*' * int(pocet):<20}|{pocet}",
        sep="\n")