import tetelek
import fuggvenyek
import pyfiglet

def main():
    olimpiak = fuggvenyek.beolvas("olimpia.csv")
    arany_oszlop = olimpiak["arany"]
    ossz_erem_minden_olimpia = []
    ossz_pont_minden_olimpia = []
    for i in range(len(arany_oszlop)):
        ermek = fuggvenyek.ossz_erem(olimpiak, i+1)
        ffs = fuggvenyek.fourthFifthSixth(olimpiak, i+1)
        pontok = fuggvenyek.ossz_pont(ermek, ffs)
        ossz_erem_minden_olimpia.append(ermek)
        ossz_pont_minden_olimpia.append(pontok)
    ossz_arany = 0
    ossz_ezust = 0
    ossz_bronz = 0
    arany,ezust,bronz = [], [], []
    for o in ossz_erem_minden_olimpia:
        arany.append(o[0])
        ezust.append(o[1])
        bronz.append(o[2])
    ossz_arany = tetelek.osszegzes(arany)
    ossz_ezust = tetelek.osszegzes(ezust)
    ossz_bronz = tetelek.osszegzes(bronz)
    print(f'Eddig elért összes aranyérem: {ossz_arany}')
    print(f'Eddig elért összes ezüstérem: {ossz_ezust}')
    print(f'Eddig elért összes bronzérem: {ossz_bronz}')
    atlag_pontszam = tetelek.osszegzes(ossz_pont_minden_olimpia) / len(ossz_pont_minden_olimpia)
    print(f'Eddigi átlag pontszám: {round(atlag_pontszam, 2):.2f}')
    olimpiak["pontszám"] = ossz_pont_minden_olimpia
    pontszam_csv = olimpiak[["év", "város","pontszám"]]
    fuggvenyek.kiir(pontszam_csv, "pontszam.csv")
    rendezett_csv = olimpiak.sort_values(by="pontszám", ascending=False)
    fuggvenyek.kiir(rendezett_csv, "rendezett.csv")
    varos = input("Adjon meg egy várost: ")
    evszam = olimpiak.loc[olimpiak["város"] == varos, "év"]
    if len(evszam) != 0:
        print('\n')
        for i in evszam:
            f = pyfiglet.figlet_format(str(i), font="alphabet")
            print(f)
    else:
        print("A megadott városban még nem rendeztek olimpiát!")
if __name__ == "__main__":
    main()
