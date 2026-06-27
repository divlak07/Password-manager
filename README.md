# Password-manager

## Overview
Password Manager is a simple Python command-line application that allows users to securely store and view account credentials. The program saves usernames and passwords in a text file and provides options to add new credentials or view existing ones.

## Features
- Add new account credentials.
- View all saved usernames and passwords.
- Store credentials in a local text file.
- Simple command-line interface.
- Uses a master password for basic access.

## Technologies Used
- Python
- File Handling
- Functions
- Text File Storage

## How It Works
1. Enter the master password to access the application.
2. Choose one of the following options:
   - **add** – Save a new username and password.
   - **view** – Display all stored credentials.
   - **q** – Exit the program.
3. Credentials are stored in the `password.txt` file.

## Project Structure

```
Password-Manager/
│
├── password_manager.py
├── password.txt
└── README.md
```

