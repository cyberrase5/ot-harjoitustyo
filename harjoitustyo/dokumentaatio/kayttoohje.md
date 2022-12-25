# Käyttöohje
(asennusohje löytyy READMEstä)

## Ohjelman käynnistys
- poetry run invoke start
- Eteesi avautuu kirjautumissivu, mutta luodaan ensin käyttäjä
- Paina nappia Tai luo tunnus

## Tunnuksen luominen
- Rekisteröitymissivulla luodaan tunnuksia
- Syötä haluttu yli yksi merkkiä pitkät käyttäjänimi ja salasana sekä valitse koulutusohjelma
- Virheellinen syöte johtaa virheilmoitukseen, onnistunut luominen uudelleenohjaa kirjautumissivulle
- Jos et sittenkään halua luoda tunnusta, paina nappia Tai kirjaudu sisään

## Kirjaudu sisään
- Syötä tunnus ja salasana, väärien syöttämisestä tulee virheilmoitus

## Etusivulla
- Täällä näet opintosuunnitelmaasi lisäämäsi kurssit ja tietoa opintojesi etenemisestä
- Paina nappia Hallitse kursseja päästäksesi lisäämään, poistamaan kursseja, sekä päivittämään arvosanoja
- Voit myös kirjautua ulos painamalla Kirjaudu ulos nappia

## Kurssien hallinta
Tällä sivulla lisätään ja poistetaan kursseja omasta opintosuunnitelmasta, ja päivitetään niiden arvosanoja

### Päivitä arvosanaa
- Arvosanat ovat väliltä 0-5
- Syötä kurssin (joka löytyy opintosuunnitelmastasi) id ja kelpo arvosana
- Kurssien idt löytyvät etusivulta nimen vierestä ja virheellisestä arvosanasta tulee virheilmoitus
- Onnistuneesta päivittämisestä ei tule viestiä, paitsi virheviesti katoaa

### Lisää kurssi opintosuunnitelmaan
- Syötä kurssin nimi ja epänegatiivinen opintopisteiden määrä
- Väärästä määrästä tulee virhe, onnistumisesta ei mitään

### Poista kurssi opintosuunnitelmasta
- Syötä poistettavan kurssin id
- Ei viestejä siitä, miten operaatiot menivät