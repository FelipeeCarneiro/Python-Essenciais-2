# camarada que me ajudou https://github.com/IvanDemin3467/Python-Essentials-LAB-2.5.1.6-Improving-the-Caesar-cipher/blob/main/improved-caesar-cipher.py#L4

def user_input():   # This function prompts the user validate the input
    global text    # test to encode
    global shift    # secret key for encoding

    #check user imput 'text' for alphanumeric characters and spaces
    while True:
        text = input ("Enter one line of text to encrypt (Roman alphabet only): ")
        text_without_spaces = text.replace(" ", "")    #spaces are allowed
        if not text_without_spaces.isalnum():
            print("Invalid input. Only alphanumeric characters and spaces are allowed.")
        else:
            break

        # check user input 'shift' for alphanumeric characters and spaces
        while True:
            shift = input("Enter the shift value (an integer from the range 1..25): ")
            if not shift.isdigit():
                print("Invalid input. Only digits are allowed.")
            else:
                shift = int(shift)
                if shift < 1 or shift > 25:
                    print("Invalid input. Only integers from the range 1..25 are allowed.")
                else:
                    break
        return


def improved_caesar_cipher(text, shift):
    # this function accpets text to encode (type(text) must be string)
    # and secret key for encoding (type(shift) must be integer)
    # encoding is: replacing given latters with other predefined letter
    # the same of original Ceasar cypher is: A->B, B->C, C->D ...
    # so the shift was always 1
    # impruvement is: shift may be any int in range (1..25)
    cipher = ''                                 # prepare string for output
    for char in text:                           # iterate over characters in text
        if char.isalpha():                      # is the current character a letter?
            code = ord(char) + shift            # -> encode is by applying shit
            if char.islower():                  # maybe we got beyond alphabet
                overflow = code - ord('z')      # calculate overflow for lower case letters
            else:
                overflow = code - ord('Z')      #               same for upper case latters
            if overflow > 0:                    # did we get beyond alphabet?
                code -= ord('z') - ord('a') + 1 # -> continue from the beginning of alphabet
        else:                                   # is the current character a digit or a space?
            code = ord(char)                    # -> keep it untouched
        cipher += chr(code)                     # current job is done -> add char to output
    return cipher                               # all is done -> return encoded string

def tests():
    # typical code that tries test cases
    print("Self-test ...")
    print_texts = ["abcxyzABCxyz 123", "The die is cast"]
    test_shift = [2, 25]
    test_results = ["cdezabCDEzab 123", "Sgd chd hr bzrs"]
    for i in range(len(test_texts)):
        txt = test_texts[i]
        shf = test_shifts[i]
        result = impruved_caesar_cipher(txt, shf)
        print(txt, shf, "->", result, end=" ")
        if result == test_results[i]:
            print("OK")
        else:
            print("Failed")


# Main
if __name__ == "__main__":
    user_input()
    print(improved_caesar_cipher(text, shift))

## testes() #uncoment ot perfom self-te