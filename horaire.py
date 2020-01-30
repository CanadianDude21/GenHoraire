from openpyxl import load_workbook, Workbook
import classes

noms = ["Kelan Grimes", "Hayden Rooney", "Lisa Villarreal", "Tate Pate", "Ella-Mae Burt", "Tommie Lawson",
        "Kwabena Bassett", "Dewi Dodson", "Shae Bright", "Tobi Richard"]
employes = {}
for i in range(1,11):
    wb = load_workbook('data/horaire{}.xlsx'.format(i))
    employes[noms[i]] = classes.employe(noms[i],wb)

nom_lieux = ["Sentier","René-Lévesque","Paul-Beaulieu","NDL","Marquis","JDV","Saint-Gérard"]
length = len(nom_lieux)
lieux = {}
for i in range(length):
    lieux[nom_lieux[i]] = classes.lieux(nom_lieux[i])