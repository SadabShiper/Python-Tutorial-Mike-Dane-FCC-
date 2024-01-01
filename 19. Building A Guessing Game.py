secret = "sadab"
guess = ""
guess_count = 0

while guess_count < 3:
    guess = input("Enter guess: ")
    guess_count += 1

if guess_count == 3:
    print("You lose!")
else:
    print("You win!")
