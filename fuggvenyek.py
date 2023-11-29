import pandas as pd

# fájl beolvasása
def beolvas(pathToFile):
    csv_file = pd.read_csv(pathToFile)
    return csv_file

# Az egy olimpián gyűjtött éremek számának meghatározása
# Egy adott CSV DataFrame(csv_file) megadott sorából(index) adja vissza az arany, ezüst és bronz érmek számát
def ossz_erem(csv_file, index):
    gold, silver, bronze = csv_file["arany"], csv_file["ezüst"], csv_file["bronz"]

    sum = 0
    index -= 1

    for i in range(len(gold)):
        sum += 1
  
    if sum > index and index >= 0:
        gold_medals, silver_medals, bronze_medals = gold[index], silver[index], bronze[index]
    else:
        return "A megadott index nem található a listában"
    return [gold_medals, silver_medals, bronze_medals]

# Az egy olimpián elért 4., 5. és 6. helyezések
# Egy adott CSV DataFrame(csv_file) megadott sorából(index) adja vissza a 4., 5. és 6. helyezések számát
def fourthFifthSixth(csv_file, index):
    fourth, fifth, sixth = csv_file["IV."], csv_file["V."], csv_file["VI."]

    sum = 0
    index -= 1

    for i in range(len(fourth)):
        sum += 1

    if sum > index and index >= 0:
        fourth_place, fifth_place, sixth_place = fourth[index], fifth[index], sixth[index]
    else:
        return "A megadott index nem található a listában"
    return [fourth_place, fifth_place, sixth_place]

# Az egy olimpián szerzett pontszám meghatározása
# Az érmek, illetve 4-5-6. helyezések alapján meghatározza az összpontszámot
def ossz_pont(all_medals, ffs_places):
    all_points = 0;
    all_points += all_medals[0]*7
    all_points += all_medals[1]*5
    all_points += all_medals[2]*4
    all_points += ffs_places[0]*3
    all_points += ffs_places[1]*2
    all_points += ffs_places[2]

    return all_points

# adatok kiíratása fájlba
# Egy CSV DataFrame(data) tartalmát írja ki egy általunk megnevezett(csv_file) fájlba
def kiir(data, csv_file):
    data.to_csv(csv_file, index=False)
