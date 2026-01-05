import random

# Hangman stages (index = lives left)
stages = [
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    ''',
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========
    '''
]

word_list = ["camel", "apple", "cat", "dog"]
chosen_word = random.choice(word_list)

display = ["_"] * len(chosen_word)
lives = 6
guessed_letters = []

while True:
    print("\nWord:", " ".join(display))
    guess = input("Guess a letter: ").lower()

    # input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Enter only ONE alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in chosen_word:
        lives -= 1
        print("Wrong guess!")
        print(stages[lives])

        if lives == 0:
            print("Game Over!")
            print(f"The word was: {chosen_word}")
            break
    else:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess

        if "_" not in display:
            print("You Win!")
            print("Word:", " ".join(display))
            break
