# Random Password Generator

## Description

The Random Password Generator is a Python project designed to create secure, random passwords based on user-defined criteria. This tool is ideal for generating strong passwords to enhance security for your accounts and applications.

## Features

- **User-Defined Length**: Enter your desired password length to generate a password of that specific length.
- **Character Variety**: The generated password can include:
  - Uppercase letters
  - Lowercase letters
  - Digits
  - Special characters
- **Randomness**: Utilizes Python’s `secrets` module to ensure high-quality randomness for strong security.

## How It Works

1. **Prompt for Length**: The program starts by asking the user to input the desired length of the password.
2. **Password Generation**: Based on the specified length, the script generates a random password. The length of the password is determined entirely by user input.
3. **Output**: Displays the generated password to the user.

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/random-password-generator.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd random-password-generator
   ```

3. **Run the Script**:
   ```bash
   python random-password-generator.py
   ```

4. **Input Password Length**: Follow the prompt to enter the length of the password you wish to generate.

## Example

```bash
$ python password_generator.py
Enter the length of your password: 12
Generated Password: aB3$dEfG7h!J
```

## Requirements

- Python 3.12
