secret = 27
max_attempts = 5
count = 0
guess = 0
print("=" * 42)
print("try to guess the number")
print("=" * 42)
print("try to guess a number 1 - 50")
print("You have 5 attempts to guess it.")
print("you get a hint if your guess is wrong")
print()
while count < max_attempts and guess != secret:
    guess = int(input("your guess: "))
    count = count + 1
    if guess == secret:
        print()
        print("you got it correct", count, "attempt(s)!")
        print("you are good at this game")
    else:
        if guess > secret:
            diff = guess - secret
        else:
            diff = secret - guess

        if diff >= 20:
            print("you are super far away")
        elif diff >= 10:
            print("still far away")
        elif diff >= 5:
            print("your close")
        else:
            print("super close")
        remaining = max_attempts - count
        if remaining > 0:
            print("guesses left", end="")
            for i in range(remaining):
                print("", end="")
            print()
            print()
if guess != secret:
    print("" * 42)
    print("you lost")
    print("the number was", secret)
    print("" * 42)