Battleships-game is a game that let  players and the computer to interact each other on a very

smart way between Computer and Human. The game target player who wants  play with the computer
 
in very smart and excited way 

https://battlesheep-game-aad062da49d0.herokuapp.com/


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
      

![Screenshot (409)](https://github.com/RodriguesIsrael/A-Battleships-game/assets/122437243/a4a0742b-3bc9-4ea0-b928-618d2239b975)


  * Play against the computer
 

![Screenshot (401)](https://github.com/RodriguesIsrael/A-Battleships-game/assets/122437243/aaeb5ebd-ac3d-4c04-b7fb-1439b6b280d8)


![Screenshot (413)](https://github.com/RodriguesIsrael/A-Battleships-game/assets/122437243/7d0de70f-ed64-428a-8b9c-e892c9fa6b60)


    
  
  * Input validation and error-checking
    * You cannot enter numbers outside the size of the grid
    * You must enter numbers
    * You can not enter the same guess Twice
   
![Screenshot (407)](https://github.com/RodriguesIsrael/A-Battleships-game/assets/122437243/f0bdfe1d-5517-4a06-8464-6e92030b2829)



![Screenshot (406)](https://github.com/RodriguesIsrael/A-Battleships-game/assets/122437243/c05c9ccf-84c0-40b5-8269-b485c72dd85f)



### Future Features

  * Allow player to select the board size and number of ships
  * Allow player to position ship themselves

## Data Model

I decided to create a simple battleship-game. In the begin  the game creates a board where we can see the ship , then the game creates two instances of the Board one for the player(human) and another for the computer with  their respective tatic entraces.

Everytime the player makes a move on his board, the computer board appears as a second board and makes also his strategic movement.

## Testing
I have manually this project by doing the following:
 
  * Passed the code throught a PEPE8linter and confirmed that there are no issue.
  * Give invalid inputs: string when numbers are expected out of bounds inputs, same input twice
  * To many white space where found on my code, but they were all deleted
  * Very long line of code, were all shorted without affecting the performance of the code.
  * Tested in my local terminal and  Heroku open app

### Bugs

#### Solved Bugs
  * When I wrote the project, I was getting function declaration  error because I had forgotten 
  that a declaration of a function always has to have (:) in end of it.
  * I was having serious problems with code alignment, since python requires a lot of attention to code alignment, so I also had a lot of errors in this aspect while working on the project.
### Remaining Bugs
  * No bugs remaining

### Validator Testing
  * PEP8
    *  After a thorough correction with PEP8CI.HEROKUAPP.COM, no more errors were found

## Technology
  * Gidpod
  * Heroku
  * Visual Studio 
  * PEP8
  * Pypi.org(colorama)
  

## Deployment

This project was deployed using Code Institute's mock terminal for Heroku.
  * Steps for deployment:
      *  Go to Heroku and click "New" to create a new app.
      *  Choose an app name and region region, click "Create app".
      *  Go to "Settings" and navigate to Config Vars. Add the following config variables:
          *PORT : 8000
      *  Navigate to Buildpacks and add buildpacks for Python and NodeJS (in that order).
      *  Navigate to "Deploy". Set the deployment method to Github and enter repository name and connect.
      *  Scroll down to Manual Deploy, select "main" branch and click "Deploy Branch".
      *  The app will now be deployed to heroku
        
TODO - Live Link
## Credits
  * Code Institute for the deployment terminal
  * Internet source(python-forum.io,rollbar.com,copyassignment.com)
  * Stack overflow
  * Google


