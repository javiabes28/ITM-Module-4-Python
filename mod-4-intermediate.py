'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

def shift_letter(letter, shift):
    '''Shift Letter. 
    4 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #if the letter is just a space, return a space
    if letter == " ":        
        return " "
    
    #shift the letter by the given amount, wrap around if needed
    shifted = ord(letter) + shift    
    if shifted > ord("Z"):
        shifted = shifted - ord("Z") + ord("A") - 1
    elif shifted < ord("A"):
        shifted = shifted + ord("Z") - ord("A") + 1
        
    #return the shifted letter
    return chr(shifted)
    
    
    
    
def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    6 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
   
    #create blank result string to return the correct message
    result = ""
    
    #shift each letter in the message by the given amount
    for letter in message:
        shifted = shift_letter(letter,shift)
        result += shifted
    
    #return the shifted message
    return (result)

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    4 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #If the letter is just a space, return a space
    if letter == "":
        return ""
    
    #Get the shift value by subtracting the ordinal value of "A" which is 0 from the ordinal value of the shift letter
    shift = ord(letter_shift) - ord("A")
        
    #Shift the letter by the calculated amount, wrap around if needed
    shifted = ord(letter) + shift 
    
    #if calculated amount is greater than the ordinal value of Z, it will wrap back to 0
    if shifted > ord("Z"):
            shifted = shifted - ord("Z") + ord("A") - 1    
    #if calculated amount is less that the ordinal value of A, it will wrap all the way to 25
    elif shifted < ord("A"):
            shifted = shifted + ord("Z") - ord("A") + 1
            
    #return the shifted letter
    return chr(shifted)
    


def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    6 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

# Create an empty result string 
    result = ""

    # Create an extended key by repeating the key as many times as needed to match the length of the message
    extended_key = (key * (len(message) // len(key) + 1))[:len(message)]

    # Shift each letter in the message by the number represented by the corresponding letter in the extended key
    for i in range(len(message)):
        letter = message[i]
        key_letter = extended_key[i]
        shifted = shift_by_letter(letter, key_letter)
        result += shifted

    # Return the shifted message
    return result