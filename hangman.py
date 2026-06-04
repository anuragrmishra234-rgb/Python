import random
stages= ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']
words=['tree','cat','bottle','anurag','riya']

word=random.choice(words)
print(word)
word_length=len(word)
display_blanks=""

for position in range(word_length):
    display_blanks=display_blanks+"_"
print(display_blanks)
game_over=False
correct_words=[]
lifes=6

while not game_over:
    guess=input("Pls guess a word: ").lower()

    display=""

    for letter in word:
        if letter==guess:
            display=display+letter
            correct_words.append(letter)
        elif letter in correct_words:
            display+=letter
        else:
            display=display+"_"

    print(display)
    if guess not in word:
        lifes-=1
        print(lifes)
        if lifes==0:
            "YOU HAVE LOST!"
            game_over=True

    if "_" not in display:
        print("Game over you win !!")
        game_over=True

    print (stages[lifes])

