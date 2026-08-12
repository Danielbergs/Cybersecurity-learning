# Password Generator

This is my first cybersecurity project.

## Goal

The goal of this project was to learn Python while exploring
password security and secure password generation.

## Features

- User-defined password length
- Minimum password length of 8 characters
- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Cryptographically secure random generation using `secrets`
- Randomized character order

## What I Learned

- How Python variables work
- How `for` loops and `range()` work
- How to work with lists using `append()`
- How `input()` and type conversion work
- How to validate user input with `ValueError`
- How Python modules work
- Why `secrets` is more appropriate than `random` for password generation
- How `join()` converts a list into a string

## Security

I initially used Python's `random` module but learned that
`secrets` is more appropriate for security-sensitive random
values such as passwords.

## Future Improvements

- Handle invalid user input without crashing
- Add more password options
- Add automated tests
