//13.1
from flask import Flask, jsonify

app = Flask(__name__)

def onko_alkuluku(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.route("/alkuluku/<int:luku>")
def tarkista_alkuluku(luku):
    tulos = {
        "Number": luku,
        "isPrime": onko_alkuluku(luku)
    }
    return jsonify(tulos)

if __name__ == "__main__":
    app.run(port=3000)


//13.2


from flask import Flask, jsonify

app = Flask(__name__)

# Yksinkertainen "tietokanta" sanakirjana
lentokentat = {
    "EFHK": {"Name": "Helsinki Vantaa Airport", "Municipality": "Helsinki"},
    "EFET": {"Name": "Enontekio Airport", "Municipality": "Enontekiö"},
    "EFTP": {"Name": "Tampere Pirkkala Airport", "Municipality": "Tampere"}
}

@app.route("/kentta/<string:icao>")
def hae_kentta(icao):
    icao = icao.upper()
    if icao in lentokentat:
        tiedot = lentokentat[icao]
        tulos = {
            "ICAO": icao,
            "Name": tiedot["Name"],
            "Municipality": tiedot["Municipality"]
        }
    else:
        tulos = {"Error": "Lentokenttää ei löytynyt."}
    return jsonify(tulos)


if __name__ == "__main__":
    app.run(port=3000)
