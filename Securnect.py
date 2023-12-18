import hashlib
import getpass
import json
import os

current_directory = os.getcwd()
# File to store user credentials
CREDENTIALS_FILE = os.path.join(current_directory, 'etc', 'shadow',"user_credentials.json")

def load_credentials():
    """Load user credentials from the file."""
    try:
        with open(CREDENTIALS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_credentials(credentials):
    """Save user credentials to the file."""
    with open(CREDENTIALS_FILE, 'w') as file:
        json.dump(credentials, file)

def hash_password(password):
    """Hash the password using SHA-256."""
    sha256 = hashlib.sha256()
    sha256.update(password.encode('utf-8'))
    return sha256.hexdigest()

def authenticate(username, password, credentials):
    """Authenticate the user."""
    stored_password = credentials.get(username)
    if stored_password and hash_password(password) == stored_password:
        return True
    return False

def create_account(username, password, credentials):
    """Create a new user account."""
    if username not in credentials:
        credentials[username] = hash_password(password)
        save_credentials(credentials)
        print("Account created successfully for {}!".format(username))
    else:
        print("Username {} already exists. Choose another username.".format(username))

def delete_user(json_file, username):
    # Read data from JSON file
    with open(json_file, 'r') as file:
        credentials = json.load(file)

    # Check if the user exists
    if username in credentials:
        # Delete the user
        del credentials[username]
        print(f"User '{username}' deleted successfully.")
    else:
        print(f"User '{username}' not found.")

    # Save the updated data back to the JSON file
    with open(json_file, 'w') as f:
        json.dump(credentials, f, indent=2)

def add_chat(json_file, name, ip, mac):
    # Load existing data from the JSON file
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = {}

    # Add a new chat object
    data[name] = {'ip': ip, 'mac': mac}

    # Write the updated data back to the JSON file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)

def delete_chat(json_file, name):
    # Load existing data from the JSON file
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {json_file} not found.")
        return

    # Check if the chat name exists in the data
    if name in data:
        del data[name]
        print(f"Chat '{name}' deleted.")
    else:
        print(f"Chat '{name}' not found.")

    # Write the updated data back to the JSON file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)

def list_chats(json_file):
    # Load existing data from the JSON file
    try:
        with open(json_file, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {json_file} not found.")
        return

    # Print the list of chat names
    number = 1
    if data:
        print()
        print('|<----> chat list <---->|')
        print('|<--------------------->|')
        for device_name in data.keys():
            print('|')
            print('|<'+ str(number) +'>', device_name)
            number += 1
        print('|')
        print('|<--------------------->|')
    else:
        print("No chats found.")

def GOODBYE():
    print('_______________________________________________________________\n')
    print("   ####    #####    #####   #####    ######   ##  ##   #######")
    print('  ##  ##  ##   ##  ##   ##   ## ##    ##  ##  ##  ##    ##')
    print(' ##       ##   ##  ##   ##   ##  ##   ##  ##  ##  ##    ##')
    print(' ##       ##   ##  ##   ##   ##  ##   #####    ####     ####')
    print(' ##  ###  ##   ##  ##   ##   ##  ##   ##  ##    ##      ##')
    print('  ##  ##  ##   ##  ##   ##   ## ##    ##  ##    ##      ##')
    print('   #####   #####    #####   #####    ######    ####    #######')
    print('_______________________________________________________________')

def logo():    
    print()
    print("||<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>||")    
    print('||                                                                                                    ||')
    print('||        ███████╗ ███████╗  ██████╗ ██╗   ██╗ ██████╗  ███╗   ██╗ ███████╗  ██████╗ ████████╗        ||')
    print('||        ██╔════╝ ██╔════╝ ██╔════╝ ██║   ██║ ██╔══██╗ ████╗  ██║ ██╔════╝ ██╔════╝ ╚══██╔══╝        ||')
    print('||        ███████╗ █████╗   ██║      ██║   ██║ ██████╔╝ ██╔██╗ ██║ █████╗   ██║         ██║           ||')
    print('||        ╚════██║ ██╔══╝   ██║      ██║   ██║ ██╔══██╗ ██║╚██╗██║ ██╔══╝   ██║         ██║           ||')
    print('||        ███████║ ███████╗ ╚██████╗ ╚██████╔╝ ██║  ██║ ██║ ╚████║ ███████╗ ╚██████╗    ██║           ||')
    print('||        ╚══════╝ ╚══════╝  ╚═════╝  ╚═════╝  ╚═╝  ╚═╝ ╚═╝  ╚═══╝ ╚══════╝  ╚═════╝    ╚═╝           ||')
    print('||                                                                                                    ||')
    print("||<<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>><<>>||")
    print()       

user = ()
chat = ()

def core():

    while True:
        choice = input("<>|SECURNECT|<"+user+'>:')

        # Load existing credentials
        credentials = load_credentials()
        json_file_path = os.path.join(current_directory, 'usr', user, "Chat_list.json")

        if choice == 'help' :
            # Commands list
            print()
            print('+-----------------+----------------------------------------+')
            print('|<--------> command list <-------------------------------->|')
            print('+-----------------+----------------------------------------+')
            print('|<> user                                                   |')
            print("|<-------> -ls          show a list of all users           |")
            print("|<-------> -add         create a new user                  |")
            print("|<-------> -rm          delete a user from the user list   |")
            print('+-----------------+----------------------------------------+')
            print('|<> chat                                                   |')
            print('|<-------> -o           open a chat........(COMING SOON)   |')
            print('|<-------> -ls          show list of all chats             |')
            print('|<-------> -add         create a new chat                  |')
            print('|<-------> -rm          delete a chat from the chat list   |')
            print('+-----------------+----------------------------------------+')
            print('|<> out                                                    |')
            print("|<-------> -l           logout from SECURNECT              |")
            print("|<-------> -e           exit from SECURNECT                |")
            print('+-----------------+----------------------------------------+')
            print('|<> clear               clear all inputs and outputs       |')
            print('+-----------------+----------------------------------------+')
            print()
        elif choice == 'user -ls' :
            # show accounts
            number = 1
            print()
            print('|<----> users  list <---->|')
            print('|<----------------------->|')
            with open(CREDENTIALS_FILE, 'r') as openfile:
                json_object = json.load(openfile)
            for key in json_object.keys():
                print('|')
                print('|<'+ str(number) +'>',key)
                number += 1
            print('|')
            print('|<----------------------->|')
            print()

        elif choice == 'user -add' :
            # Create an account
            username = input('<>|SECURNECT|<>Enter a new username:')
            password = getpass.getpass('<>|SECURNECT|<-------->Enter '+ username +' password:')
            create_account(username, password, credentials)
            directory_path = os.path.join(current_directory, 'usr', username)
            os.makedirs(directory_path, exist_ok=True)

            
        elif choice == 'user -rm' : 
            # Delere an account 
            username_to_delete = str(input('<>|SECURNECT|<>Enter a username:'))

            if username_to_delete == 'admin':
                print('you can not delete "admin" user')
            elif username_to_delete == user:
                input('<>|SECURNECT|<>If you proceed, all of your data will be lost and any ongoing activities will be terminated.')
                selection = input('<>|SECURNECT|<>Do you want to delete '+username_to_delete+' ? (y/n) :')

                if selection == 'y':
                    os.rmdir(os.path.join(current_directory, 'usr', username_to_delete))
                    delete_user(CREDENTIALS_FILE, username_to_delete)
                    main()
                elif selection == 'n':
                    print('user '+username_to_delete+' not deleted')
                else: 
                    core()           
            else:
                input('<>|SECURNECT|<>If you proceed, any '+username_to_delete+' data will be lost.')
                selection = input('<>|SECURNECT|<>Do you want to delete '+username_to_delete+' ? (y/n) :')

                if selection == 'y':
                    os.rmdir(os.path.join(current_directory, 'usr', username_to_delete))
                    delete_user(CREDENTIALS_FILE, username_to_delete)
                elif selection == 'n':
                    print('user '+username_to_delete+' not deleted')
                else: 
                    core()

        elif choice == 'chat -add' :
            
            if user == 'admin' :
                print('You cannot use an admin account to access chat services. Please log in with personal credentials.')
            else :
                device_name = input("<>|SECURNECT|<>Enter chat name: ")
                device_ip = input("<>|SECURNECT|<>Enter contact IP: ")
                device_mac = input("<>|SECURNECT|<>Enter contact MAC: ")
                add_chat(json_file_path, device_name, device_ip, device_mac)
                print(f"Chat '{device_name}' added to {user} chat list.")
        
        elif choice == 'chat -rm' :
            
            if user == 'admin' :
                print('You cannot use an admin account to access chat services. Please log in with personal credentials.')
            else :
                chat_to_delete = input("<>|SECURNECT|<>Enter chat name to delete: ")
                selection = input('<>|SECURNECT|<>Do you want to delete '+chat_to_delete+' ? (Y/N) :')
                
                if selection == 'y':
                    delete_chat(json_file_path, chat_to_delete)
                    print('chat '+chat_to_delete+' deleted')
                elif selection == 'n':
                    print('chat '+chat_to_delete+' not deleted')
                else: 
                    core()
            
        elif choice == 'chat -ls' :
            
            if user == 'admin' :
                print('You cannot use an admin account to access chat services. Please log in with personal credentials.')
            else :
                list_chats(json_file_path)
                print('\n')

        elif choice == 'out -l' :
            # Logout
            GOODBYE()
            main()
        
        elif choice == 'out -e' :
            # Exit
            GOODBYE()
            break

        elif choice == 'clear' :
            os.system('cls' if os.name == 'nt' else 'clear')
            logo()
            core()

        elif choice == '' :
            core()

        else:
            print("Invalid choice, enter 'help' for more info.")
        
def main():
    """Main function for authentication and account creation."""
    print('\n')
    print('||<-------------------------------------------------------------------------------------------------->||')
    print('||<<>><<>><<>><<>><<>><<>><<>> Welcome to SECURNECT authentication system <<>><<>><<>><<>><<>><<>><<>>||')
    print('||<-------------------------------------------------------------------------------------------------->||')
    print('')
    login()

def login():
    
    # Load existing credentials
    credentials = load_credentials()

    log= False
    
    while not log :
            # Log in
            username = input("<>|SECURNECT|<>Enter your username: ")

            if username == '' :
                login()

            else :
                password = getpass.getpass("<>|SECURNECT|<-------->Enter your password: ")
            
                if authenticate(username, password, credentials):
                    print("Authentication successful. Welcome, {}!".format(username))
                    global user
                    user = username
                    log= True
                else:
                    print("Authentication failed. Please check your username and password.")  
    logo()
    core()

if __name__ == "__main__":
    main()

#   ╔══<>|SECURNECT|<>
#   ╚═>    