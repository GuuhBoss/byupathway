secret_word = input("Enter the secret word: ").lower()

print("Welcome to the word guessing game!")
print()

guess_count = 0
current_word = ["_"] * len(secret_word)
show_hint = True

while True:
    if show_hint:
        print("Your hint is:", " ".join(current_word))

    # Reset hint
    show_hint = True

    guess = input("What is your guess? ").lower()
    guess_count += 1

    # Check if the guess is correct
    if guess == secret_word:
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")
        break

    # Check if the guess is the same length as the secret word
    if len(guess) != len(secret_word):
        # If the guess is not the same length, don't show hint
        show_hint = False
        print("Your guess must be the same length as the secret word. Please try again.")
        print()
        continue

    for i in range(len(secret_word)):
        # Set default to underscore if the letter is not guessed
        current_word[i] = "_"

        # If the letter is in the secret word, but not in the correct position, show it in lowercase
        if guess[i] in secret_word:
            current_word[i] = guess[i].lower()

        # If the letter is in the secret word, and in the correct position, show it in uppercase
        if guess[i] == secret_word[i]:
            current_word[i] = guess[i].capitalize()
    print()