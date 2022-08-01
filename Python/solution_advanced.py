import random

# This advanced solution is the same as the original but we have added a round counter.
# Each round begins by showing the round number
# This is quite simple, so I've put a comment on each line that has changed :)
balance = 100
symbols = ["{cherries}", "{bell}", "{lemon}", "{tangerine}", "{glowing star}", "{skull}"]
round_count = 1  # stores the current round number (starts at 1)

while balance > 0:
    is_quitting = input("Press enter to continue or type 'q' to quit!")
    if is_quitting == 'q':
        break

    print(f"\n============================[ Round {round_count} ]============================")  # Showing round count
    balance = balance - 20
    print("20 has been subtracted from your balance as payment for this round.")

    rolled = [random.choice(symbols) for _ in range(3)]
    print(f"You rolled: {' '.join(rolled)}!")

    for symbol in symbols:
        symbol_count = rolled.count(symbol)
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
    print("===================================================================\n")  # End of round
    round_count += 1  # Add to round

print(f"You finished the game with a balance of {balance}!")
