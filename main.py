#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

logo = """ ____   _  _   ___    ___    ___     _____  _  _   ___     _  _   _  _   _   _  ___   ___   ____  
).-._( ) () ( ) __(  (  _(  (  _(   )__ __() () ( ) __(   ) \/ ( ) () ( ) \_/ (\  _) ) __( /  _ \ 
|( ,-. | \/ | | _)   _) \   _) \      | |  | -- | | _)    |  \ | | \/ | |  _  ||  (  | _)  )  ' / 
)_`__( )____( )___( )____) )____)     )_(  )_()_( )___(   )_()_( )____( )_( )_(/__o) )___( |_()_\ """

print(logo)
import random
print("\nWelcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

computer_number = random.choice(number)
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

def attemps():
  if difficulty == "easy":
    lifes = 10
    print(f"You have {lifes} attempts remaining to guess the number.")
  elif difficulty == "hard":
    lifes = 5
    print(f"You have {lifes} attempts remaining to guess the number.")
  else:
    print("You type a different option")
attemps()

guess_number = False
lifes_e = 10
lifes_h = 5
while not guess_number:
  guess = int(input("Make a guess: "))
  if guess != computer_number:
    if guess > computer_number and difficulty == "easy":
      lifes_e -= 1
      print("Too High")
      print("Guess again.")
      print(f"You have {lifes_e} attempts remaining to guess the number.")
      if lifes_e == 0:
        print("You've run out of guesses, you lose.")
        guess_number = True
    elif guess < computer_number and difficulty == "easy":
      lifes_e -= 1
      print("Too Low")
      print("Guess again.")
      print(f"You have {lifes_e} attempts remaining to guess the number.")
      if lifes_e == 0:
        print("You've run out of guesses, you lose.")
        guess_number = True
    elif guess > computer_number and difficulty == "hard":
      lifes_h -= 1
      print("Too High")
      print("Guess again.")
      print(f"You have {lifes_h} attempts remaining to guess the number.")
      if lifes_h == 0:
        print("You've run out of guesses, you lose.")
        guess_number = True
    elif guess < computer_number and difficulty == "hard":
      lifes_h -= 1
      print("Too Low")
      print("Guess again.")
      print(f"You have {lifes_h} attempts remaining to guess the number.")
      if lifes_h == 0:
        print("You've run out of guesses, you lose.")
        guess_number = True
  elif guess == computer_number:
    print(f"You got it! The answer was {computer_number}.")
    guess_number = True




























    
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# logo = """ ____   _  _   ___    ___    ___     _____  _  _   ___     _  _   _  _   _   _  ___   ___   ____  
# ).-._( ) () ( ) __(  (  _(  (  _(   )__ __() () ( ) __(   ) \/ ( ) () ( ) \_/ (\  _) ) __( /  _ \ 
# |( ,-. | \/ | | _)   _) \   _) \      | |  | -- | | _)    |  \ | | \/ | |  _  ||  (  | _)  )  ' / 
# )_`__( )____( )___( )____) )____)     )_(  )_()_( )___(   )_()_( )____( )_( )_(/__o) )___( |_()_\ """

# print(logo)
# import random
# print("\nWelcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100.")

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

# computer_number = random.choice(number)
# difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")



# def attemps():
#   if difficulty == "easy":
#     lifes == lifes - 1
#     print(f"You have {lifes} attempts remaining to guess the number.")
#   elif difficulty == "hard":
#     lifes == lifes - 1
#     print(f"You have {lifes} attempts remaining to guess the number.")
#   else:
#     print("You type a different option")
# attemps()

# if difficulty == "hard":
#    lifes == int(5)
# else:
#    lifes == int(10)


# lifes = 0
# guess_number = False

# if lifes != 0:
#   while guess_number == False:
#     guess = int(input("Make a guess: "))
#     if guess != computer_number :
#       attemps()
#       if guess > computer_number:
#         print("Too High")
#         print("Guess again.")
#       elif guess < computer_number:
#         print("Too Low")
#         print("Guess again.")
#     elif guess == computer_number:
#       print(f"You got it! The answer was {computer_number}.")
#       guess_number = True
# else:
#   print ("Sorry, maximum attempts reached")