# Sisu 2.0
Sisu 2.0 on Sisu-kopio, eli eräänlainen opintojen seurausjärjestelmä. Luo tunnus, kirjaudu sisään, valitse itsellesi mieluisia kursseja, päivitä niiden arvosanoja, katso kuin keskiarvo nousee (tai laskee). Tai poista kursseja opintosuunnitelmastasi


# Dokumentaatio
[Käyttöohje](dokumentaatio/kayttoohje.md)

[Vaatimusmaarittely](dokumentaatio/vaatimusmaarittely.md)

[Arkkitehtuurikuvaus](dokumentaatio/arkkitehtuuri.md)

[Testidokumentti](dokumentaatio/testidokumentti.md)

[Changelog](dokumentaatio/changelog.md)

[Tuntikirjanpito](dokumentaatio/tuntikirjanpito.md)


# Käteviä komentoja
- poetry install (lataa riippuvuudet)
- poetry run invoke initialize (luo tietokannan)
- poetry run invoke start (käynnistää)
- poetry run invoke test (ajaa testit)
- poetry run invoke coverage-report (luo testikattavuusraportin)


# Nykyiset toiminnot
- Luo käyttäjä, kirjaudu sisään
- Tarkastele saamiasi arvosanoja ja opintojen etenemistä
- Lisää kursseja omaan opintosuunnitelmaan
- Päivitä kurssiesi arvosanoja
- Poista kursseja omasta opintosuunnitelmasta

## Pohdintaa laajuudesta
- Koulutusohjelmia voi lisätä (kohtalaisen) helposti, pitää vain muistaa lisätä pakolliset kurssit initialize_database.py