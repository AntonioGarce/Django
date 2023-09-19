import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def generate_secure_code():
    secure_code = ''
    for k in range(5):
        nr_letters = random.randint(3, 5)
        password_letters = [random.choice(letters) for i in range(nr_letters)]
        password_list = password_letters
        random.shuffle(password_list)
        number_app = "".join(password_list)
        if k == 4:
            secure_code += number_app
        else:
            secure_code += number_app + '-'
    return secure_code
