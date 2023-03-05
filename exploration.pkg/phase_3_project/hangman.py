



def hangman():
    print("You chose to play Hangman! Great choice!")
    user_word = input("Please Choose a word for the game: ")

    word_to_guess = [letter for letter in user_word]
    user_won = False
    hidden_word = []
    all_user_guesses = []
    hidden_word.extend('_' * len(user_word))
    while user_won == False:
        user_guess = input("Great! Please guess a letter: ")
        
        if user_guess in word_to_guess:
            all_user_guesses.append(user_guess)
            print(all_user_guesses)
            print("                        ===== That is correct! =====")
            index_of_guess = word_to_guess.index(user_guess)
            hidden_word[index_of_guess] = user_guess
            print(f"               State of guesses:  {hidden_word}")
            if len(all_user_guesses) == len(word_to_guess):
                print("                 Good Job! You're A Good Guesser!")
                user_won = True

        else:
            print("That is not correct!")

hangman()    



incorect_result_1 = """
                                       |
                                       |
                                       |
                                       |
                                       |
                                       |
                                       |
                                       | 
"""

incorect_result_2 = """
                             ___________         
                                     \ |
                                      \|
                                       |
                                       |
                                       |
                                       |
                                       | 
"""

incorect_result_3 = """
                             ___________         
                             |       \ |
                             O        \|
                           _/|\_       |
                             |         |
                            _|_        |
                                       |
                                       | 
"""