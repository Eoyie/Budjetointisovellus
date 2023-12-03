# Budjetointisovellus

### Välipalautus 2

## Sovelluksen nykyinen tilanne
Sovelluksessa pitäisi toimia:
- Käyttäjän luominen ja kirjautuminen
- Kategorioiden lisäys ja poisto (jos poistat kategorian, myös kaikki sen menot poistuvat)
- Budjettien lisäys ja poisto (jos lisäät samalle kuulle budjetteja, niin updeittaa eli muokkaa. Lisätiedot eivät näy missään vielä!)
- Menojen lisäys ja poisto
- Listaukset budjeteista, kategorioista ja menoista
- Yhteenveto kuun budjetista ja menoista.
 
 Mitä pitää vielä viimeistellä:
 - Lisätään vielä tietokanta future_expenses (eli tulee 5 tietokantaa!!).
 - Ulkonäkö yleisesti paremmaksi (Varsinkin menojen listaus!!)
 - Budjettejen lisätiedot nähtäviin (tai pois).
 - Lisää sääntöjä esim. salasanan luomiseen, nyt vain pituus rajoja! 
 - Yleistä koodin siivousta ym.

## Miten pystyy käynnistää
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
##
### Välipalautus 1

En ole vielä täysin varma tarkasta laajuudesta, mutta pääideana olisi tehdä sovellus omien tehtyjen ja mahdollisesti tulevien ostoksien budjetoinnista. Tämä tulisi olla yleisesti mukavampi ja interaktiivisempi, kuin ns. perinteinen excel-taulukko, jota usein käytetään budjetointiin. Siis vielä enemmän idea on erotella ns. turhia, pakollisia ja hupi ostoksia vain yksinkertaisen "mihin meni rahaa" sijaan.

## Tässä yleisiä idoita sovelluksen toimivuudesta:

Sovelluksessa näkyy käyttäjän ostoksia ja tulevia ostosuunnitelmia, joista löytyy tarkempia tietoja menojen tärkeydestä ja tarkoituksesta. Jokainen käyttäjä on peruskäyttäjä tai ylläpitäjä.
- Käyttäjä voi kirjautua sisään ja ulos, sekä luoda uuden käyttäjän ##DONE##
- Käyttäjä voi päättää mitä budjetoinnin alueita hän käyttää ja mitä ei (Esim. jos ei ole autoa, tähän liittyvää osuutta ei ole aina turhaan näkyvillä). Voi siis esim. käyttää ainoastaan ruokaostoksien tai ns. "ylimääräisten" ostoksien seuraamiseen.  ##DONE?##
- Käyttäjä voi laittaa tietoja ostoksistaan yksityiskohtaisia tietoja ja lisätä myös myöhemmin kommentteja näihin liittyen. Voi tehdä näistä myös toistuvia (esim. vuokraa ei tarvitse aina lisätä uudestaan) ##VAIN NOTES MUUT LUULTAVASTI EI TEHDÄ##
- Käyttäjä voi myös tehdä kirjauksia asioista, mitä saatetaan ostaa tulevaisuudessa. Olkoon esim. lahjoja, "ylimääräistä" hauskaa tai tarpeellisia asioita. Ja nähdä miten nämä vaikuttaisivat tulevan ajan budjetointiin tai voi myös olla vain "idea" ilman mitään vaikutusta. ##TODO##
- Käyttäjä voi nähdä näistä kaikista asioista jonkinlaisen yhteenvedon.  ##DONE?##
- Käyttäjä voi helposti etsiä ja muokata tehtyjä kirjauksia.  ##CHANGED##

Ylläpitäjän rooli on vielä hieman auki, sillä en ole varma kuinka paljon käyttäjän tiedoista on salattua. Käyttäjälle kokemus on sinäänsä hyvin yksityinen, joten seuranta ei ole kovin tarpeellista. Ehkä, jos kaksi käyttäjää voivat jotenkin olla vuorovaikutuksessa esim. yhdistää budjetteja niin tällöin, kyllä. Budjetoinnissa ei sinäänsä voi tehdä paljoa "väärin", johon ylläpitäjän pitäisi puuttua. Asia on vielä pohdinnan alla siis..
