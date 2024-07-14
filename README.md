Brute Force Password Cracker

Description
The Brute Force Password Cracker is a Python-based tool designed to perform dictionary and brute force attacks on password-protected files or systems. It supports various protocols like SSH and FTP, allowing you to test and evaluate the security of these services.

Features
Dictionary Attack: Attempts to crack passwords using a predefined list of passwords.
Brute Force Attack: Attempts to crack passwords by generating all possible combinations of a given character set up to a specified length.
Protocol Support: Supports SSH and FTP protocols.
Timing: Measures and displays the time taken to perform attacks.

Technologies
Python: The primary programming language used.

Libraries:
paramiko: For SSH connections.
ftplib: For FTP connections.
itertools: For generating combinations of characters.
time: For measuring the duration of attacks.

Installation
Clone the Repository:
git clone https://github.com/yourusername/brute-force-password-cracker.git
cd brute-force-password-cracker

Install Required Libraries:
pip install paramiko

Usage
Prepare the Password File:

Create a file named passwords.txt in the project directory.
Add a list of potential passwords, one per line.
Edit Configuration:

Open the brute_force.py file.
Set the target, username, and other parameters in the main function.

Run the Script:
python brute_force.py

Notes
Ensure that you have the correct permissions to perform these actions on the target system.
Use this tool responsibly and only on systems you have explicit permission to test.
License
This project is licensed under the MIT License. See the LICENSE file for details.
