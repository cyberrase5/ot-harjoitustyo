# Sisu 2.0
Sisu 2.0 on Sisu-kopio, eli eräänlainen opintojen seurausjärjestelmä. Luo tunnus, kirjaudu sisään, valitse itsellesi mieluisia kursseja, päivitä niiden arvosanoja, katso kuin keskiarvo nousee (tai laskee). Tai poista kursseja opintosuunnitelmastasi


# Dokumentaatio
[vaatimusmaarittely.md](dokumentaatio/vaatimusmaarittely.md)

[tuntikirjanpito.md](dokumentaatio/tuntikirjanpito.md)

[changelog.md](dokumentaatio/changelog.md)

[arkkitehtuurikuvaus.md](dokumentaatio/apologia.md)


# Käteviä komentoja
- poetry install (lataa riippuvuudet)
- poetry run invoke initialize (luo tietokannan)
- poetry run invoke start (käynnistää)
- poetry run invoke test (ajaa testit)


# Nykyiset toiminnot
- Luo käyttäjä, kirjaudu sisään
- Tarkastele saamiasi arvosanoja
- Lisää kursseja omaan opintosuunnitelmaan
- Päivitä kurssiesi arvosanoja
- Poista kursseja omasta opintosuunnitelmasta


# TODO
- Tarkista, ettei kurssia ole olemassa
- Tarkista arvosanan päivityksen kentät
- Tarkista syötteet, ei tyhjiä yms.