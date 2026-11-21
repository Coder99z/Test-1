secret = 27
max_attempts = 5
count = 0
guess = 0
print("=" * 42)
print("Welcome to the Guessing Game!")
print("=" * 42)
print("Guess a number between 1 and 50.")
print("You have 5 attempts to guess the correct number.")
print()

while count < max_attempts and guess != secret:
    guess = int(input("Enter your guess: "))
    count += 1

if guess == secret:
    print("Correct! You win!")
else:
    if guess > secret:
        diff = guess - secret
    else:
        diff = secret - guess

    if diff >= 20:
        print("You are way off 🧊.")
    elif diff >= 10:
        print("You are off by a bit. ❄️")
    elif diff >= 5:
        print("You are close! 🔥")
    else:
        print("You are very close! 🔥🔥")
    remaning_attempts = max_attempts - count
    if remaning_attempts > 0:
        print(f"You have {remaning_attempts} attempts left. Try again!")
        for i in range(remaning_attempts):
         print("❤️", end=" ")

if guess != secret:
    print("\nGame Over! The correct number was:", secret)
    print("Better luck next time!")
    print("The secret number was:", secret)
    print("=" * 42)

             