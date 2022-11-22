# Ohjelmistotekniikka

## MazeRunner

Sokkelopelissä MazeRunner pelaajan on tarkoitus selvittää reitti turvaan. Reittiä etsiessään hän kohtaa vihollisia ja palkkiota joilla on seuraukset pelin kulkuun. Pelin tarkoitus on läpäistä kenttiä ja saavuttaa mahdollisimman suuri HIGH SCORE.

## Dokumentaatiot

[vaatimusmäärittely](https://github.com/tuovinenemma/ot-harjoitustyo2022/blob/master/dokumentaatio/vaatimusmaarittely.md)

[työaikakirjanpito](https://github.com/tuovinenemma/ot-harjoitustyo2022/blob/master/dokumentaatio/tuntikirjanpito.md)

[changelog](https://github.com/tuovinenemma/ot-harjoitustyo2022/blob/master/dokumentaatio/changelog.md)


## Asennus

1. Asenna riippuvuudet komennolla:

```bash
poetry install
```

2. Suorita vaadittavat alustustoimenpiteet komennolla:

```bash
poetry run invoke build
```

3. Käynnistä sovellus komennolla:

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
