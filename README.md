# Intruder
This is a Python project to execute some tools used in ethical hacking and intrusion testing. Currently, I have added the functionalities that I could think of, but feel free to use what I have done to add more features or enhance existing ones.

![screenshot](https://github.com/R-kill-9/Intruder/blob/main/intruder.png)

## Execution
```bash
python3 intruder.py
```

## Usage
First of all, the program asks you to enter your IP and the target IP, these values can be changed later if desired. Similarly, you can also change the Dump Directory, all of this with the option S (settings).
After inserting these IPs you access to the main Menu. Here you can execute:
-   PS: Port Scan using NMAP.
-   F: Fuzzing test with GOBUSTER, you have the option to fuzz subdirectories or subdomains.
-   BF: Execute a brute force attack to a service using HYDRA.
-   CP: Cracking hashed passwords with JOHN THR RIPPER
-   N: Activate a listener with NETCAT on a port between 1024 and 2000
-   B: Execute BURPSUITE
-   M: Going back to Menu
-   E: Exit
-   S: Settings  (Change User Ip, Change Target Ip, Change Dump Directory)
  
