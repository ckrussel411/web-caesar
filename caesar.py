def encrypt(text, rot):

    rot_int = int(rot)
    new_string = ""
    for i in text:
        new_string = new_string + rotate_character(i,rot_int)
    return(new_string)

def alphabet_position(letter):
    if letter.isalpha():
        letter = letter.upper()
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return(alphabet.index(letter))
    else:
        return letter

def rotate_character(char, rot):
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    if char.isalpha():
        if char.isupper():
            start_index = alphabet_position(char)
            high_rotation = rot % 26
            new_index = start_index + high_rotation
            if new_index > 25:
                new_index = new_index - 26
            new_char = upper_alphabet[new_index]
        if char.islower():
            start_index = lower_alphabet.index(char)
            high_rotation = rot % 26
            new_index = start_index + high_rotation
            if new_index > 25:
                new_index = new_index - 26
            new_char = lower_alphabet[new_index]
        return(new_char)
    else:
        return(char)
