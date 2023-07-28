# Battleships-game

Battleships-game is a game that let  players and the computer to interact each other on a very

smart way between Computer and Human. The game target player who wants  play with the computer
 
in very smart and excited way.



![ro](https://github.com/RodriguesIsrael/A-Battleships-game/assets/122437243/1633e933-9346-4d56-97db-26091400a2c7)


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


![Screenshot (203)](https://github.com/RodriguesIsrael/A-Battleships-game/assets/122437243/ef114283-5c03-4f40-b611-60b63c0143d8)

  * Play against the computer 
  
  * Input validation and error-checking
    * You cannot enter numbers outside the size of the grid
    * You must enter numbers
    * You can not enter the same guess Twice

### Future Features

  * Allow player to select the board size and number of ships
  * Allow player to position ship themselves

## Data Model

I decided to create a simple battlesheep-game. In the begin  the game creates a board where we can see the sheep , then the game creates two instances of the Board one for the player(human) and another for the computer with  their respective tatic entraces.

Everytime the player makes a move on his board, the computer board appears as a second board and makes also his strategic movement.

## Testing
I have manually this project by doing the following:
 
  * Passed the code throught a PEPE8linter and confirmed that there are not big issue.
  * Give invalid inputs: string when numbers are expected out of bounds inputs, same input twice
  * Tested in my local terminal and the Code Institute Heroku Terminal

### Bugs

#### Solved Bugs
  * When I wrote the project, I was getting function declaration  error because I had forgotten 
  that a declaration of a function always has to have (:) in end of it.
  * I was having serious problems with code alignment, since python requires a lot of attention to code alignment, so I also had a lot of errors in this aspect while working on the project.
### Remaining Bugs
  * No bugs remaining

### Validator Testing
  * PEP8
    *  After a thorough correction, no more errors were found from PEP8CI.HEROKUAPP.COM

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.
  * Steps for deployment:
      *  Fork or clone this repository
      *  Create a new Heroku app
      *  Set the buildback to pythong and NodeJs that order
      *  Link the Heroku app to the repository
      *  Click on *Deploy*

## Credits
  * Code Institute for the deployment terminal
  * Google and other internet source for details of the Battleship game
![#1589F0]RODRIGUES `#1589F0`
