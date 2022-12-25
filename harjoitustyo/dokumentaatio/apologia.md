# Ohjelman rakenne

## Tietokanta
Ohjelman tietokanta on toteutettu SQLitellä, ja sisältää kolme taulua. Selitän vain epäilmeiset osat:
- taulussa users degree_id kertoo, mitä tutkintoa opiskelija suorittaa. Tämä on tärkeää myöhemmin.
- taulussa courses mandatory kertoo, onko kurssi pakollinen. Tätä tietoa tarvitaan myöskin myöhemmin
- taulu participants sisältää tiedot opiskelijoiden kurssisuorituksista. Arvosanat ovat normaali 0-5, ja -1 on vakioarvo, joka tarkoittaa suorittamatonta kurssia (ei oteta huomioon keskiarvoa laskettaessa)


## Moduulit
UserRepository tällä hetkellä käsittelee "backend" toiminnot users-taulun kanssa. Käyttäjän luominen, sisäänkirjautuminen yms. hoidetaan täällä

CourseRepository on laajempi, sillä se hoitaa taulujen courses ja participants operaatiot, eli kurssien luomiset ja lisäämiset opintosuunnitelmaan, arvosanan päivttäminen yms.

initialize_database hoitaa tietokantojen luonnin. Sen lisäksi, että tässä luodaan tietokantataulut, täällä myös luodaan pakolliset kurssit eri koulutusohjelmiin, sillä jos kaikki käyttäjät joutusivat lisäämään omat pakolliset kurssinsa, se olisi tyhmää. Täällä on siis määritelty tutkintojen (tällä hetkellä vain tkt) pakolliset kurssit, jotka lisätään tietokantaan heti taulujen luomisen jälkeen. Näillä kursseilla courses-taulun mandatory on true, millään muilla ei. Kun käyttäjä rekisteröityy, haetaan taulusta courses niiden kurssien id, joissa mandatory on true, ja degree_id on rekisteröityneen ja luodaan tauluun participants user_id, course_id pareja (ja arvosana tietysti).

database_connection hoitaa yhteyden tietokantaan. Ei ihan sillä tavalla kuin materiaalissa neuvotaan, mutta toimi virtuaalikoneella niin kelpaa minulle. Moduuli sisältää myös yhteyden muodostamisen testitietokantaan, jota kutsutaan testien setUp()issa

GUI tietysti hoitaa käyttöliittymän Tkinterillä, ja kutsuu repositories-luokkia services-luokan kautta välillisesti


## Testit
Testeissä testataan haluttuja ominaisuuksia, eli kahta samannimistä saman koulutusohjelman kurssia ei lisätä tietokantaan, kahta samanlaista participants riviä ei lisätä yms.