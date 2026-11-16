import random
import math
print("random fun calculator")
lucky_number = random.randint(1, 10)
print("your lucky number is:", lucky_number)
fun_choices = ["play a game", "solve a puzzle", "read a story", "draw something"]
random_activity = random.choice(fun_choices)
print("random activity for today:", random_activity)
print("\nguess the secret number from 1 to 5")
secret_number = random.randint(1, 5)
while True:
    guess = int(input("enter your guess: "))
    if guess == secret_number:
        print("correct you guessed the number.")
        break
    else:
        print("wrong guess try again")
decimal_number = float(input("\nenter a decimal number: "))
print("ceiling value:", math.ceil(decimal_number))
print("floor value:", math.floor(decimal_number))
x = 10
y = -5
print("copy sign result:", math.copysign(x, y))
negative_number = int(input("enter a negative number: "))
print("absolute value:", math.fabs(negative_number))
num1 = int(input("enter the first number for gcd"))
num2 = int(input("enter the second number for gcd "))
print("gcd is", math.gcd(num1, num2))
print("\nfun calculator summary")
print("lucky number:", lucky_number)
print("random activity:", random_activity)
print("secret number:", secret_number)