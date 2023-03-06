def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')


def encoder(password):
    # The password encoder should take in an 8-digit password in string format containing only integers.
    # After passing the password into the encoder, the encoder stores the encoded password to a new
    # variable, with each digit being shifted up by 3 numbers.
    password = [int(num) for num in password]
    K = 3
    en_coder = [num + K for num in password]
    en_coder_s = [str(num) for num in en_coder]
    en_coder_str = ''.join(en_coder_s)

    return en_coder_str


def decoder(password):
    # The password decoder takes in the encoded password and returns the original password.
    password = [int(num) for num in password]
    k = 3
    de_coder = [num - k for num in password]
    de_coder_s = [str(num) for num in de_coder]
    de_coder_str = ''.join(de_coder_s)

    return de_coder_str


password_continue = True
if __name__ == '__main__':

    while password_continue:
        # displaying and allowing for input until user exits out
        menu()
        op = int(input('Please enter an option:'))

        if op == 1:
            pass_word = input('Please enter your password to encode:')
            encoded = encoder(pass_word)
            print("Your password has been encoded and stored!")
        # elif op == 2:

        elif op == 3:
            password_continue = False
