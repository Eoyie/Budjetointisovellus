# Budjetointisovellus

## Lyhyesti sovelluksesta
Tässä sovelluksessa pystyt hallinnoimaan budjettiasi lisäämällä omia seurattavia menoja eri kategorioihin. Kyseiset kategoriat pystyt luoda vapaasti itse, riippuen siitä mitä menoja haluat sovelluksessa seurata. Voit lisäksi lisätä sekä normaaleja menoja, että tulevia menoja, jotka eivät vaikuta suoraan budjeteihin.

### Ominaisuuksia
- Kirjautuminen
  - Käyttäjä voi luoda itselleen uuden käyttäjän
  - Käyttäjä voi kirjautua sisään ja pois sovelluksesta
- Kotisivu
  - Käyttäjä voi kotisivullaan nähdä yhteenvedon kuluvan kuukauden menoista kategoreittain
  - Käyttäjä voi kotisivullaan nähdä yhteenvedon kuluvan kuukauden menojen summan ja vaikutuksen asetettuun budjettiin
- Budjetti
  - Käyttäjä voi asettaa budjetin eri kuukausille
  - Käyttäjä voi päivittää tai poistaa budjetin
- Kategoria
  - Käyttäjä voi luoda ja poistaa kategorioita
- Menot
  - Käyttäjä voi lisätä uusia menoja hinnan, päivämäärän, kategorian ja lisätietojen avulla
  - Käyttäjä voi nähdä listan kaikista menoista
  - Käyttäjä voi nähdä listan yksittäisten kuukausien menoista
  - Käyttäjä voi poistaa menon
- Tulevat menot
  - Käyttäjä voi lisätä uusia tulevia menoja hinnan, kategorian ja lisätietojen avulla
  - Käyttäjä voi nähdä listan kaikista tulevista menoista
  - Käyttäjä voi siirtää tulevan menon menneeksi ja antaa tälle päivämäärän
    -  Käyttäjä voi menoa siirtäessä päivittää kaikkia tietoja paitsi kategoriaa
  - Käyttäjä voi poistaa tulevan menon

## Miten sovelluksen pystyy käynnistää
**Sovellus ei ole testattavissa Fly.iossa!**
Tässä on siis ohjeet sovelluksen käynnistämiseen paikallisesti:

Kloonaa repositorio omalle koneellesi ja siirry sen juurikansioon. Luo kansioon oma .env-tiedosto ja määritä sen sisältö näin:
 
```
DATABASE_URL=<tietokannan-paikallinen-osoite>
SECRET_KEY=<salainen-avain>
```
 
- *tietokannan-paikallinen-osoite* eli postgresql:///user, jossa user on käytettävän tietokannan nimi (ja tämä näkyy myös PostgreSQL-tulkissa rivien alussa)
- *salainen-avain* eli esim. Pythonilla luotu salainen avain:
 
```
  $ python3
>>> import secrets
>>> secrets.token_hex(16)
```
 
Aktivoi virtuaaliympäristö ja asenna sovelluksen riippuvuudet komennoilla:
 
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r ./requirements.txt
```
 
Muista käynnistää oma PostgreSQL-tulkki! Tähän on ohje [asennusskriptin sivuilla](https://github.com/hy-tsoha/local-pg). Määritä tämän jälkeen tietokannan skeema komennolla:
 
```
$ psql < schema.sql
```
 
Tai manuaalisesti psql PostgreSQL-tulkissa!
 
Nyt voit käynnistää sovelluksen komennolla ja avata annetun linkin, josta pääsee sovellukseen.
 
```
$ flask run
```

