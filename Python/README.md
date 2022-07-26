# Fruit Machine
Write a program to simulate a Fruit Machine that displays three symbols at random from Cherry, Bell, Lemon, Orange, Star, Skull.

## Problem
Write a program to simulate a Fruit Machine that displays three symbols at random from Cherry, Bell, Lemon, Orange, Star, Skull.
The player starts with £1 credit, with each go costing 20p. If the Fruit Machine “rolls” two of the same symbol, the user wins 50p. The player wins £1 for three of the same
and £5 for 3 Bells. The player loses £1 if two skulls are rolled and all of his/her money if three skulls are rolled. The player can choose to quit with the winnings after each
roll or keep playing until there is no money left

### Summary
Here is a summary of what the program must do, this may be easier to read than a chunk of text.
- Player starts with £1
- Each spin/round costs 20p
- The fruit machine displays three symbols at random from :cherries: :bell: :lemon: :orange: :star: :skull:
- If fruit machine "rolls" two of the same symbol the user wins 50p
- If fruit machine "rolls" three of the same symbol the user wins £1
- If fruit machine "rolls" three bells :bell: the user wins £5
- If fruit machine "rolls" two skulls :skull: the user loses £1
- If fruit machine "rolls" three skulls :skull: the user loses everything
- The user can quit with the winnings after each round or keep playing until no money left.

## Solution
This is a very simple game of chance. The solution is to assign a value to each symbol and then randomly choose three values. We then check the symbols chosen and reward the player depending on what was "rolled".

We will use a "game loop". This is an infinite loop that repeats the same questions/rolls over and over until either the player runs out of money or decides to quit.
