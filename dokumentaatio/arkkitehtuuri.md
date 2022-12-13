# Arkkitehtuurikuvaus
## Rakenne

```mermaid

classDiagram
SRC
UI
services
tests
sprites
assets

SRC --> UI
SRC --> services
SRC --> tests
SRC --> sprites
SRC --> assets

UI --> services
services --> sprites
services --> assets
assets --> UI
assets --> sprites

```

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


Game luokassa kutsuttujen eri luokkien toiminnallisuus Game luokassa sekvenssikaaviona:

```mermaid

sequenceDiagram
Game ->> Level: create maze
Level ->> Game: create maze
Game ->> Player: move player
Player ->> Game: move player
Game ->> Renderer: render
Renderer ->> Game: render


```
