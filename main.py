# Brianna Yanqui
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
    en_coder = [num - 10 if num >= 10 else num for num in en_coder]
    en_coder_s = [str(num) for num in en_coder]
    en_coder_str = ''.join(en_coder_s)

    return en_coder_str

# Minh C Nguyen
def decoder(password):
    result = ''
    for i in password:
        temp = int(i) - 3
        if temp >= 0:
            result += str(temp)
        else:
            result += str(int(i) + 10 - 3) # if int minus 3 is negative we should plus 10
    print(f"The encoded password is {password}, and the original password is {result}.")


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
        # Minh C Nguyen
        elif op == 2:
            decoder(encoded)
        elif op == 3:
            password_continue = False
