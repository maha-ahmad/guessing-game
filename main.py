def guess_word(secret_word: str, guess_limit: int) -> None:
    secret_word = secret_word.lower()
    remaining_guesses = guess_limit
    print(f"You have {guess_limit} guesses to guess the word.")

    while remaining_guesses > 0:
        guess = input('Enter your guess: ').lower()
        if guess == secret_word:
            print('Congratulations! You guessed the word!')
            return
        remaining_guesses -= 1
        print(f"Oops! '{guess}' is not the word. You have {remaining_guesses} guesses left.")

    print(f"Sorry, you ran out of guesses. The word was '{secret_word}'.")
    
guess_word(secret_word='pythonista', guess_limit=3)
