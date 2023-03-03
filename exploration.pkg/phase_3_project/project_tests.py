from user_info import User, session, verify_user   

def account_initilization():
    first_choice = input("""
    Welcome! Please Select 1 to 'create an account', or if you already have an account, select 2 'to log in':
                                              ====>>>> """)
    if first_choice == '1':
        create_user_username = input("Create a Username: ")
        create_user_password = input("Create a password: ")
        session.add(User(create_user_username, create_user_password))
        session.commit()
    elif first_choice == '2':
        existing_user_username = input("Please enter your username: ")
        existing_user_password = input("Please enter your password: ")
        verify_user(existing_user_username, existing_user_password)

if __name__ == '__main__':
    account_initilization()
