import random
print("Welcome to our Number Guessing Game.")
def number():
    lower=1
    upper=10
    guess=random.randint(lower,upper)
    attempts=0
    while True:
        n=int(input("Your Guess: "))
        attempts+=1
        if n>guess:
            print("It is lower")
        elif n<guess:
            print("It is higher")
        else:
            print("You are correct")
            print(f'You took {attempts} attempts')
            break
number()


