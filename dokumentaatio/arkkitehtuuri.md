# Arkkitehtuurikuvaus
## Rakenne

![Screenshot from 2022-11-29 19-32-30](https://user-images.githubusercontent.com/102189885/204601032-0a90e9b9-5c99-4518-aec4-a681539d6065.png)

## Käyttöliittymä

Käyttöliittymä sisältää kolme erillistä näkymää:

* Pelin aloitus
* Pelikenttä
* Pelin lopetus

```mermaid
classDiagram
  StartGame--|>Game
  Game--|>GameOver
  
  class StartGame{
    state = start
    
   }
  class Game{
    state = playing
  }
  
  class GameOver{
    state = game over
  }
```

