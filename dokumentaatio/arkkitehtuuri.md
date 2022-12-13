# Arkkitehtuurikuvaus
## Rakenne

![Screenshot from 2022-11-29 19-32-30](https://user-images.githubusercontent.com/102189885/204601032-0a90e9b9-5c99-4518-aec4-a681539d6065.png)

## Käyttöliittymä

Käyttöliittymä sisältää kolme erillistä näkymää:

* Pelin aloitus
* Pelikenttä
* Pelin lopetus

```mermaid

sequenceDiagram
participant StartGame
participant Game
participant GameOver

StartGame->>Game: start_game()
Game->>GameOver: end_game()
GameOver->>Game: restart()
GameOver->>StartGame: exit()


```

Toiminnallisista kokonaisuuksista vastaa luokka Game. Luokka tarjoaa käyttäliittymän toiminnoille metodeja. Näitä ovat esimerkiksi:

* start_game()
* playing()
* game_running()
* exit_level()
