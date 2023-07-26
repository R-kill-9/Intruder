import textwrap
import os

USER_IP = "0.0.0.0"
TARGET_IP = "0.0.0.0"
DUMP_DIRECTORY = os.getcwd()
exit_flag = False

def box():
    text = '''\
 _    _ _ _        _____   _       _                  _           
| |  (_) | |      |  _  | (_)     | |                | |          
| | ___| | |______| |_| |  _ _ __ | |_ _ __ _   _  __| | ___ _ __ 
| |/ / | | |______\____ | | | '_ \| __| '__| | | |/ _` |/ _ \ '__|
|   <| | | |      .___/ / | | | | | |_| |  | |_| | (_| |  __/ |   
|_|\_\_|_|_|      \____/  |_|_| |_|\__|_|   \__,_|\__,_|\___|_|  
'''
    text_f = textwrap.indent(textwrap.dedent(text), ' ' * 3)
    print(text_f)


def set_D():
    global DUMP_DIRECTORY
    print("* Enter the Dump Directory: ")
    path = input()
    while not os.path.exists(path):
        print("* Inexistent path, enter a valid one: ")
        path = input()
    DUMP_DIRECTORY = path


def set_UIP():
    global USER_IP
    print("* Enter the IP address of your machine: ")
    USER_IP = input()


def set_TIP():
    global TARGET_IP
    print("* Enter the IP address of the target machine: ")
    TARGET_IP = input()
    while TARGET_IP == USER_IP:
        print("* You can't repeat the IP address, enter the IP address of the target machine: ")
        TARGET_IP = input()

def set_IP():
    set_UIP()
    set_TIP()


def error():
    print("!!!!! INPUT ERROR !!!!!")


def port_scan():
    print("* If you want to scann all the ports type 1, if you want to scan an specific port type 2: ")
    mode = input()
    if mode == '1':
        command = f"nmap -sCV -p- --min-rate 5000 -vv --open -Pn {TARGET_IP} > {DUMP_DIRECTORY}/nmap.txt"
        os.system(command)
    elif mode == '2':
        print("Select the port:")
        port = input()
        command = f"nmap -sCV -vv --min-rate 5000 -Pn -p {port} {TARGET_IP} >{DUMP_DIRECTORY}/nmap.txt"
        os.system(command)
    elif mode == 'M':
        menu()
    else: 
        print("!!!!! INPUT ERROR !!!!!")


def exit_menu():
    global exit_flag
    exit_flag = True

def settings():
    os.system('clear')
    text = f'''\
    ******************************************************************************************
                                                                                             
                                    USER IP: {USER_IP}                                       
                                  TARGET IP: {TARGET_IP}                                     
                            DUMP DIRECTORY: {DUMP_DIRECTORY}                                 
                                                                                             
      - U: Change User IP                                                                     
      - T: Change Target IP                                                                  
      - D: Change dump directory                                                             
      - M: Go back to Menu                                                                   
    ******************************************************************************************
    '''
    text_f = textwrap.indent(textwrap.dedent(text), ' ' * 3)
    print("\n")
    print(text_f)

    #Possible actions
    actions = {"M": menu, "U": set_UIP, "T": set_TIP, "D": set_D}

    while True:
        if exit_flag:
            break
        inp = input()
        action = actions.get(inp, error)
        action()


def fuzzing():
    print("* If you want to do a subdirectory enumeration type 1, if you want to do a subdomain enumeration type 2:")
    mode = input()
    if mode == '1':
        os.system("wget https://raw.githubusercontent.com/theMiddleBlue/DNSenum/master/wordlist/subdomains-top1mil-20000.txt")
        command = f"gobuster dir -u {TARGET_IP} -w subdomains-top1mil-20000.txt > {DUMP_DIRECTORY}/subdir_enum.txt"
        os.system(command)
        command2 = "rm subdomains-top1mil-20000.txt"
        os.system(command2)
    elif mode == '2':
        os.system("wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/DNS/subdomains-top1million-5000.txt")
        command = f" gobuster vhst -w {TARGET_IP} -wsubdomains-top1million-5000.txt > {DUMP_DIRECTORY}/subdom_enum.txt"
        os.system(command)
        command2 = "rm subdomains-top1million-5000.txt"
        os.system(command2)
    elif mode == 'M':
        menu()
    else: 
        error()


def brute_force():
    print("* Introduce a username:")
    username = input()
    os.system("wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt")
    command = f"hydra -L {username} -P 10-million-password-list-top-1000000.txt {TARGET_IP} ssh"
    os.system(command)
    os.system("rm 10-million-password-list-top-1000000.txt")


def john(hashes_file):
    try:
        with open(hashes_file, 'r') as file:
            pass
    except FileNotFoundError:
        print(f"The file '{hashes_file}' was not found.")
        return

    try:
        result = subprocess.run(["john", hashes_file], capture_output=True, text=True, check=True)
        # verify password existence
        if "password hashes cracked" in result.stdout:
            print("Passwords found:")
            print(result.stdout)
        else:
            print("No passwords found.")

    except subprocess.CalledProcessError as e:
        print("Error executing John the Ripper:")
        print(e.stderr)


def crack_password():
    print("* If you want to crack just a password type 1, if you want to crack a file with passwords type 2: ")
    mode = input()
    if mode == 'M':
        menu()
    elif mode == '1':
        print("* Introduce the hash: ")
        hash_password = input()
        
        with open('crack.txt', 'w') as crack:
            crack.write(f"kill:{hash_password}\n")
            john(crack.txt)

    elif mode == '2':
        print("* Insert the full file's PATH: ")
        file = input()
        john(file)
    
    else:
        error()


def netcat():
    print("* Enter a port between 1024 and 2000: ")
    port = int(input())
    while not 1024 <= port <= 2000:
        print("* Not valid port, enter a port between 1024 and 2000: ")
        port = int(input())
    command = f"nc -lvnp {port}"
    os.system(command)


def burpsuite():
    os.system("burpsuite")


def menu():
    os.system('clear')
    text = f'''\
    ******************************************************************************************
                                                                                            
                                    USER IP: {USER_IP}                                       
                                  TARGET IP: {TARGET_IP}                                     
                            DUMP DIRECTORY: {DUMP_DIRECTORY}                                 
                                                                                                                                                                    
      - PS: Execute a port Scan                                                              
      - F: Fuzzing test
      - BF: Brute Force service password
      - CP: Crack hash password           
      - N: Activate a listener
      - B: Execute Burpsuite
      - M: Go back to Menu
      - S: Settings                                                  
      - E: Exit the application                                                             
    ******************************************************************************************
    '''
    text_f = textwrap.indent(textwrap.dedent(text), ' ' * 3)
    print("\n")
    print(text_f)

    #Possible actions
    actions = {"S": settings, "PS": port_scan, "E": exit_menu, "F": fuzzing, "M": menu, "BF": brute_force, "CP": crack_password, "N": netcat, "B": burpsuite}

    while True:
        if exit_flag:
            break
        inp = input()
        action = actions.get(inp, error)
        action()


def main():
    box()
    set_IP()
    menu()



if __name__ == "__main__":
    main()