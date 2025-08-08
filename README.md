# SecurePass Vault

A local password strength analyzer that checks user-submitted passwords against a list of known weak passwords and returns security advice.

##  Purpose

This tool helps users become more aware of weak password choices and encourages better security practices.

##  How It Works

- You enter a password into the console
- The script checks:
  - If it's in the list of weak/breached passwords
  - If it’s too short
  - If it lacks character variety
- You get advice on how to improve it

##  Example


##  Files

- `main.py` – Launches the program
- `analyzer.py` – Analyzes the password
- `weak_passwords.py` – Local password database
