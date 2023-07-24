# Battleships-game

Battleships-game is a game that let  players and the computer to interact each other on a very

smart way between Computer and Human. The game target player who wants  play with the computer
 
in very smart and excited way.


## How to play

Battleship-game is bessed on the classic pen-and-paper game. To know more about it you need to

hava a look on Goolgle.com or Wikipedia.

In this game, the player (human) enters 8 number from 1 - 8 and the overwiew of the first board

is generated.

The player can see where the ships are indicated by an ( _ ).

The player then takes it in turn to make a guess followed by the , according to the players guess to try to sink each other's battleships.

The capital ( X ) represents places in miss while lowercase ( o ) represents places in hit.

The winner is the player who sinks all their opponent's  battleship fist, when this append we
 
have the capital ( O ) to reprent the end of the game.


## Features


### Existing Features
  * Random board generation
    * Ships are randomly placed on both player and computer boards
    * The player cannot see where the computer's ship are 
     
  * Play against the computer 
  
  * Input validation and error-checking
    * You cannot enter numbers outside the size of the grid
    * You must enter numbers
    * You can not enter the same guess Twice

### Future Features

  * Allow player to select the board size and number of ships
  * Allow player to position ship themselves

## Data Model

I decided to create a simple battlesheep-game. The game creates two instances of the Board one for the player(human) and another is for the computer.

Every time the player makes a move on his board, the computer board appears as a second board and makes also his strategic movement.
  