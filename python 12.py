//12.1

import requests

# Haetaan satunnainen vitsi
pyynto = "https://api.chucknorris.io/jokes/random"
vastaus = requests.get(pyynto).json()

# Tulostetaan vain vitsin teksti
print("Chuck Norris -vitsi:\n")
print(vastaus["value"])


//12.2

import requests

kaupunki = input("Anna paikkakunnan nimi: ")
api_avain = "API_AVAIN"

# Rakennetaan pyyntö
pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={api_avain}"
vastaus = requests.get(pyynto).json()

if vastaus.get("cod") != 200:
    print("Kaupunkia ei löytynyt.")
else:
    kuvaus = vastaus["weather"][0]["description"]
    lampotila_kelvin = vastaus["main"]["temp"]
    lampotila_celsius = lampotila_kelvin - 273.15

    print(f"\nSää paikassa {kaupunki}: {kuvaus}")
    print(f"Lämpötila: {lampotila_celsius:.1f} °C")
