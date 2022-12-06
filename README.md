# Ohjelmistotekniikka

Harjoitustyö Helsingin yliopiston Ohjelmistotekniikka-kurssille.

## MazeRunner

Sokkelopelissä MazeRunner pelaajan on tarkoitus selvittää reitti turvaan. Reittiä etsiessään hän kohtaa vihollisia ja palkkiota joilla on seuraukset pelin kulkuun. Pelin tarkoitus on läpäistä kenttiä ja saavuttaa mahdollisimman suuri HIGH SCORE.

Sovellus on toteutettu Python -versiolla 3.8

## Dokumentaatiot

* [vaatimusmäärittely](https://github.com/tuovinenemma/ot-harjoitustyo2022/blob/master/dokumentaatio/vaatimusmaarittely.md)

* [työaikakirjanpito](https://github.com/tuovinenemma/ot-harjoitustyo2022/blob/master/dokumentaatio/tuntikirjanpito.md)

* [changelog](https://github.com/tuovinenemma/ot-harjoitustyo2022/blob/master/dokumentaatio/changelog.md)

* [arkkitehtuuri](https://github.com/tuovinenemma/ot-harjoitustyo2022/blob/master/dokumentaatio/arkkitehtuuri.md)

## Release

[Viikon 5 release](https://github.com/tuovinenemma/ot-harjoitustyo2022/releases/tag/viikko5)


## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Ohjelman pystyy suorittamaan komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage-report
```

### Pylint

Tiedoston [.pylintrc](https://github.com/tuovinenemma/ot-harjoitustyo2022/blob/master/project/.pylintrc) määrittelemät tarkistukset voi suorittaa komennolla:

```bash
poetry run invoke lint
```
