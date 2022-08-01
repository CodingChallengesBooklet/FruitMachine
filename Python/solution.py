import random

# We pre-define our user's balance and the symbols we are going to use
balance = 100

# I originally tried to get symbols to work, but I ran into issues with checking what symbol the
# random picker chose, so instead they are just "{symbols name}"
# feel free to try adding symbols into the program, you can use "\N{symbol name}" or the emoji package from pip
symbols = ["{cherries}", "{bell}", "{lemon}", "{tangerine}", "{glowing star}", "{skull}"]

while balance > 0:

    # Here we check if the player wants to continue playing.
    # They can enter anything but "q" to quit the game.
    is_quitting = input("Press enter to continue or type 'q' to quit!")
    if is_quitting == 'q':
        break

    # We're subtracting 20 from the balance because that's how much a round costs
    balance = balance - 20
    print("20 has been subtracted from your balance as payment for this round.")

    # We pick three random symbols, and send them to the end user.
    rolled = [random.choice(symbols) for _ in range(3)]  # This is called "list comprehension" btw.
    print(f"You rolled: {' '.join(rolled)}!")

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
