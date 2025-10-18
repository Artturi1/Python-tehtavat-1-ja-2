//8.1

import mysql.connector

def hae_lentoasema(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Lentoaseman nimi: {rivi[0]}, sijaintikunta: {rivi[1]}")
    else:
        print("Lentoasemaa ei löytynyt.")

# Pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='salasana',
    autocommit=True
)

icao = input("Anna lentoaseman ICAO-koodi: ").upper()
hae_lentoasema(icao)


//8.2

import mysql.connector

def hae_lentokentat_maakoodilla(maakoodi):
    sql = f"""
        SELECT type, COUNT(*) 
        FROM airport 
        WHERE iso_country='{maakoodi}' 
        GROUP BY type;
    """
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount > 0:
        print(f"Lentokentät maassa {maakoodi}:")
        for rivi in tulos:
            print(f"{rivi[0]}: {rivi[1]} kpl")
    else:
        print("Maakoodia ei löytynyt tai lentokenttiä ei ole.")

# Pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='salasana',
    autocommit=True
)

maakoodi = input("Anna maakoodi (esim. FI): ").upper()
hae_lentokentat_maakoodilla(maakoodi)


//8.3

import mysql.connector
from geopy.distance import distance

def hae_koordinaatit(icao):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident='{icao}'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()
    return tulos  # palauttaa (lat, lon) tai None

# Pääohjelma
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='salasana',
    autocommit=True
)

icao1 = input("Anna ensimmäisen lentoaseman ICAO-koodi: ").upper()
icao2 = input("Anna toisen lentoaseman ICAO-koodi: ").upper()

koord1 = hae_koordinaatit(icao1)
koord2 = hae_koordinaatit(icao2)

if koord1 and koord2:
    etaisyys = distance(koord1, koord2).km
    print(f"Lentokenttien välinen etäisyys on {etaisyys:.2f} km.")
else:
    print("Toista ICAO-koodia ei löytynyt tietokannasta.")
