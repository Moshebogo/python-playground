from user_info import User, session, verify_user
from own_battleship import battleship
from matching_game import matching_game
from hangman import hangman


def choose_game():
     user_choice = (input("""                                   
                                        Please type a number to select a game from menu below:
                                          
                                                        
                                                        1)  Battleship
                                                        2)  Matching game
                                                        3)  Hangman
     
     """))
     if user_choice == '1':
          battleship()
     elif user_choice == '2':
          matching_game()
     elif user_choice == '3':
          hangman()

     

def account_initilization():
    counter = 0
    first_choice = input("""
                                                   Welcome to the FlatIron Arcade!

                     Please Select ( 1 ) to 'create an account', or if you already have an account, select ( 2 ) 'to log in':
                                              
                                                      ====>>>> \ / <<<<====
                                                                """)
    if first_choice == '1':
        create_user_username = input("Create a Username: ")
        create_user_password = input("Create a password: ")
        session.add(User(create_user_username, create_user_password))
        session.commit()
        print("You succesfully created an account!")
        choose_game()

    elif first_choice == '2':
            # while counter < 5:
                existing_user_username = input("Please enter your username: ")
                existing_user_password = input("Please enter your password: ")
                verify_user(existing_user_username, existing_user_password)
                choose_game()
                # counter += 1

if __name__ == '__main__':
    account_initilization()
