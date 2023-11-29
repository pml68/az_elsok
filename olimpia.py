import tetelek
import fuggvenyek

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

if __name__ == "__main__":
    main()
  