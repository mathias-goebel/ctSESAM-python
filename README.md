# ctSESAM-python
This is the command line Python version of the c't password manager.

## Improvements
  - password input without echo
  - password output to the clipboard instead of the terminal
  - more special characters (incl. quotation marks)
  - password now 20 characters long
    - in general this is to ensure we get lower case and upper case letters, numbers and special characters in the password to match oversized password requirements
  - a line of the private ssh key is used as salt, this is what makes this a linux only version
