import enchant

letters = "abcdefghijklmnopqrstuvwxyz"
letters = letters + letters

enc_list = "--+-"

d = enchant.Dict("en_US")


def encrypt():

    # Юзер инпут !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    while True:
        enc = input('Enter "+" to encrypt, "-" to decrypt or "--" to decode: ').strip()
        enc_f = enc_list.find(enc)
        enc_l = len(enc)
        if enc_f == -1:
            print("It is not + or -")
        elif enc_l == 0:
            print("Entered nothing")
        else:
            break

    if enc == "+":
        message_user = "Enter your message to encrypt: "
    elif enc == "-":
        message_user = "Enter your message to decrypt: "
    elif enc == "--":
        message_user = "Enter your message, try to decrypt : "

    message = input(message_user).strip()

    if enc == "--":
        pass
    else:
        while True:
            message_key = input("Enter a message key in range 1-25: ").strip()
            if not message_key.isnumeric():
                print("Enter a number not letter/s")
            elif not 1 <= int(message_key) <= 25:
                print("Enter a number in a range 1-25: ")
            else:
                break

    # Расшифровать !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if enc == "--":
        print("Try find yor message here: ")
        aa = []
        aaaa = []

        for letter1 in message:
            position1 = letters.find(letter1.lower())
            a = []
            for i in range(1, 25):
                if position1 != -1:
                    position1 += 1
                    if position1 != -1:
                        a.append(position1)
                if position1 == -1:
                    a.append(-1)
            aa.append(a)

        for i in range(0, 23):
            aaa = []
            decrypted_decrypted = ""
            for aa1 in aa:
                aaa.append(aa1[i])
            aaaa.append(aaa)
            for inc, ai in enumerate(aaa, start=0):
                if ai != -1:
                    decrypted_decrypted = decrypted_decrypted + letters[ai]
                if ai == -1:
                    decrypted_decrypted = decrypted_decrypted + message[inc]
                if message[inc].isupper() is True:
                    decrypted_decrypted = decrypted_decrypted.replace(
                        decrypted_decrypted[-1], letters[ai].upper()
                    )

            chk_decode_a = []
            for decode in decrypted_decrypted.split():
                chk_decode = d.check(decode)
                if chk_decode is True:
                    chk_decode_a.append(1000)
                if chk_decode is False:
                    chk_decode_a.append(-1)

            if max(chk_decode_a) > 0:
                print(decrypted_decrypted)

        else:
            pass

    # Кодинг, Декодинг !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if enc == "--":
        pass
    else:
        encrypted = ""

        for letter in message:
            position = letters.find(letter.lower())

            if position != -1:
                position = position + int(f"{enc}{message_key}")
            if position != -1:
                encrypted = encrypted + letters[int(position)]
            if letter.isupper() is True:
                encrypted = encrypted.replace(
                    encrypted[-1], letters[int(position)].upper()
                )
            if letter.isupper is True:
                encrypted = encrypted.replace()
            if position == -1:
                encrypted = encrypted + letter

        if enc == "+":
            print("Encrypted: " + encrypted)
        else:
            print("Decrypted: " + encrypted)


if __name__ == "__main__":
    encrypt()