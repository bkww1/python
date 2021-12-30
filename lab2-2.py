def CaesarCipher(message, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    #make sure the message we work with is lowercased to match symbols in alphabet
    message = message.lower()

    result = ""
    #run on each letter in the message
    for letter in message:
        if letter in alphabet:
            #find the index of the letter in the alphabet
            index = alphabet.find(letter)
            #determine the shift
            index = (index + shift)%(len(alphabet))

            #deals with wrap around if index is greater than 26 or less than 0
            if index < 0:
                index = index + len(alphabet)

            #adds letter to result
            result = result + alphabet[index]

        #if the symbol isn't a letter (like punctuation), just print that
        else:
            result = result + letter
    #prints what the text would read if it were decrypted using each possible shift
    #go through the list and figure out which shift gives you a sensible message
    return result


print(CaesarCipher("aaaaaaaaaaaaaaaaaaatuvwxyz",-3))
