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



def menu():
    os.system('clear')
    text = f'''\
    ******************************************************************************************
                                                                                            
                                    USER IP: {USER_IP}                                       
                                  TARGET IP: {TARGET_IP}                                     
                            DUMP DIRECTORY: {DUMP_DIRECTORY}                                 
                                                                                                                                                                    
      - PS: Execute a port Scan                                                              
      - F: Fuzzing test
      - BF: Brute Force password           
      - M: Go back to Menu
      - S: Settings                                                  
      - E: Exit the application                                                             
    ******************************************************************************************
    '''
    text_f = textwrap.indent(textwrap.dedent(text), ' ' * 3)
    print("\n")
    print(text_f)

    #Possible actions
    actions = {"S": settings, "PS": port_scan, "E": exit_menu, "F": fuzzing, "M": menu}

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