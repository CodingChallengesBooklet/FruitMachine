# Fruit Machine
Write a program to simulate a Fruit Machine that displays three symbols at random from Cherry, Bell, Lemon, Orange, Star, Skull.

![GitHub followers](https://img.shields.io/github/followers/hrszpuk?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/hrszpuk?style=social)
<br>
![GitHub language count](https://img.shields.io/github/languages/count/CodingChallengesBooklet/FruitMachine?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/CodingChallengesBooklet/FruitMachine?style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/CodingChallengesBooklet/FruitMachine?style=for-the-badge)
![GitHub last commit](https://img.shields.io/github/last-commit/CodingChallengesBooklet/FruitMachine?style=for-the-badge)
![GitHub branch checks state](https://img.shields.io/github/checks-status/CodingChallengesBooklet/FruitMachine/main?style=for-the-badge)

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
Let's write this out in pseudocode. 

Below we are setting up the basic "game loop", quitting, and we define balance (but do not use it yet).
Our loop is infinite and only stops when the `balance` is less than or equal to 0.
We output "roll again or type 'q' to quit" and check if the player inputted a 'q'.
If the player does enter a 'q' the game will end, otherwise it will continue looping.
Note, our balance is always going to be in pence. This makes it easier to subtract or add to the balance later on.
```python
balance = 100
symbols = ["cherry", "bell", "lemon", "orange", "star", "skull"]
LOOP UNTIL balance <= 0
    OUTPUT "Press enter to roll again or type 'q' to quit!"
    is_quitting = INPUT
    IF is_quitting IS "q"
        STOP LOOP
    
    
    
END OF LOOP
OUTPUT "You left with a balance of " balance  
```
In the code above we're missing a lot of the logic needed, so let's write that out as well.
First we need to subtract 20 from the balance at the start of the round.
```python
balance = balance - 20
OUTPUT "20p as been taken from your balance"
```
Then we need to choose three random symbols. 
This is pretty easy, `symbols` is already defined with all the symbols we need.
We randomly add a single item from `symbols` into `rolled`. 
We also output what symbols the player got.
```python
rolled = []
ADD RANDOM symbol TO rolled
ADD RANDOM symbol TO rolled
ADD RANDOM symbol TO rolled

FOR EACH symbol IN rolled
    OUTPUT "You got " symbol
END
```
Now we have our random symbols, we now need to count the symbols! 
This is the simplest technique, we simply go through all the symbols in `rolled` and add 1 to the relevant count for the symbol we find.
```python
skull_count = 0
bell_count = 0
cherry_count = 0
lemon_count = 0
orange_count = 0
star_count = 0
FOR EACH symbol IN rolled
    IF symbol IS skull
        skull_count += 1
    ELSE IF symbol IS bell
        bell_count += 1
    ELSE IF symbol IS cherry
        cherry_count += 1
    ELSE IF symbol IS lemon
        lemon_count += 1
    ELSE IF symbol IS star
        star_count += 1    
    ENDIF
END
```
Now we've got the count, we have to check the count to see if the player won or lost anything!
Remember, two or more skulls and the player loses money, two or more of the same symbol and the player wins money.
When the player gets three bells they win a significant amount of money.
```python
IF skull_count IS 2
    OUTPUT "You got two skulls! You lose £1!"
    balance = balance - 100
ELSE IF skull_COUNT IS 3
    OUTPUT "You got three skulls! You lose everything!"
    balance = 0
ELSE IF cherry_count IS 2 OR lemon_count IS 2 OR orange_count IS 2 OR star_count IS 2 OR bell_count IS 2
    OUTPUT "You got two of the same symbols! You won 50p!"
    balance = balance + 50
ELSE IF cherry_count IS 3 OR lemon_count IS 3 OR orange_count IS 3 OR star_count IS 3
    OUTPUT "You got three of the same symbols! You won £1!"
    balance = balance + 100
ELSE IF bell_count IS 3
    OUTPUT "You got three bells! Super lucky! You won £5!"
    balance = balance + 500
ELSE
    OUTPUT "You didn't win anything! Unlucky!"
```
For the explanation I've split everything up to it's easier to understand. Let's finally put it together so we can see what it looks like as a complete program.
```python
balance = 100
symbols = ["cherry", "bell", "lemon", "orange", "star", "skull"]
LOOP UNTIL balance <= 0
    OUTPUT "Press enter to roll again or type 'q' to quit!"
    is_quitting = INPUT
    IF is_quitting IS "q"
        STOP LOOP
        
    balance = balance - 20
    OUTPUT "20p as been taken from your balance"
    
    rolled = []
    ADD RANDOM symbol TO rolled
    ADD RANDOM symbol TO rolled
    ADD RANDOM symbol TO rolled

    FOR EACH symbol IN rolled
        OUTPUT "You got " symbol
    END
    
    skull_count = 0
    bell_count = 0
    cherry_count = 0
    lemon_count = 0
    orange_count = 0
    star_count = 0
    FOR EACH symbol IN rolled
        IF symbol IS skull
            skull_count += 1
        ELSE IF symbol IS bell
            bell_count += 1
        ELSE IF symbol IS cherry
            cherry_count += 1
        ELSE IF symbol IS lemon
            lemon_count += 1
        ELSE IF symbol IS star
            star_count += 1    
        ENDIF
    END
    
    IF skull_count IS 2
        OUTPUT "You got two skulls! You lose £1!"
        balance = balance - 100
    ELSE IF skull_COUNT IS 3
        OUTPUT "You got three skulls! You lose everything!"
        balance = 0
    ELSE IF cherry_count IS 2 OR lemon_count IS 2 OR orange_count IS 2 OR star_count IS 2 OR bell_count IS 2
        OUTPUT "You got two of the same symbols! You won 50p!"
        balance = balance + 50
    ELSE IF cherry_count IS 3 OR lemon_count IS 3 OR orange_count IS 3 OR star_count IS 3
        OUTPUT "You got three of the same symbols! You won £1!"
        balance = balance + 100
    ELSE IF bell_count IS 3
        OUTPUT "You got three bells! Super lucky! You won £5!"
        balance = balance + 500
    ELSE
        OUTPUT "You didn't win anything! Unlucky!"
    
END OF LOOP
OUTPUT "You left with a balance of " balance  
```

