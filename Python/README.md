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
I've broken down the solution shown in `solution.py` below. 

We will break down the solution into 4 parts:
1. pre-defining needed variables
2. Checking if user want to continue, and charging user for round
3. Picking our random symbols
4. Checking the symbols and outputting the correct message or removing/adding balance

Here's the first part. We are creating two variables, one called `balance` that holds the user's balance (default value of 100),
and `symbols` which stores the symbols in the problem question.
```python
import random

# We pre-define our user's balance and the symbols we are going to use
balance = 100

# I originally tried to get symbols to work, but I ran into issues with checking what symbol the
# random picker chose, so instead they are just "{symbols name}"
# feel free to try adding symbols into the program, you can use "\N{symbol name}" or the emoji package from pip
symbols = ["{cherries}", "{bell}", "{lemon}", "{tangerine}", "{glowing star}", "{skull}"]
```

Next we create the "game loop": an infinite loop that only ends when the balance is 0 or less.
This ensures the user cannot keep playing after losing all their money!
We also check if the user wants to quit, of which they can be typing "q",
and subtracting 20 from the user's balance (as that's what a round costs to play).
```python
while balance > 0:
    
    # Here we check if the player wants to continue playing.
    # They can enter anything but "q" to quit the game.
    is_quitting = input("Press enter to continue or type 'q' to quit!")
    if is_quitting == 'q':
        break

    # We're subtracting 20 from the balance because that's how much a round costs
    balance = balance - 20
    print("20 has been subtracted from your balance as payment for this round.")
```

Now we will pick the three random symbols and display them to the user.
For this we use the `random` module we imported in the first section.
We also display the symbols to the user, so they can see what they got.
```python
    # We pick three random symbols, and send them to the end user.
    rolled = [random.choice(symbols) for _ in range(3)]  # This is called "list comprehension" btw. 
    print(f"You rolled: {' '.join(rolled)}!")
```

Finally, for each symbol we will check what it is and the number of them to determine the correct
output and add/remove the correct value from the balance.
After modifying the balance we show the balance to the user.
```python
    for symbol in symbols:
        symbol_count = rolled.count(symbol)  # In case there is more than one symbol.
        
        # Here we just check the symbol, and the count, and then send the right message or subtract the correct amount.
        if symbol == "{skull}":
            if symbol_count == 2:
                print(f"Unlucky! You got two skulls! 50 has been taken from your balance!")
                balance = balance - 50
            elif symbol_count == 3:
                print(f"Very unlucky! You got three skulls! You lose everything!!!")
                balance = 0
        elif symbol == "{bell}":
            if symbol_count == 3:
                print(f"Lucky lucky lucky! You got two bells! 500 has benn added to your balance!")
                balance = balance + 500
        elif symbol_count == 2:
            print(f"Lucky you! Two of the same symbol? That's an extra 50 in your balance!")
            balance = balance + 50
        elif symbol_count == 3:
            print(f"Wow that's really lucky! 100 has been added to your balance!")
            balance = balance + 100

    print(f"You finished the round with a balance of {balance}!")

print(f"You finished the game with a balance of {balance}!")
```

## Extension
This task doesn't have an extension solution. 
You can create your own solution by adding something new to the game!
Try adding a round counter, or a leaderboard.
I decided to do a round counter, which you can see in `solution_advanced.py`.