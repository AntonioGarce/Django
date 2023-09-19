import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def generate_order_num():
    password_letters = [random.choice(numbers) for i in range(5)]
    password_list = password_letters
    random.shuffle(password_list)
    number_app = "".join(password_list)
    return number_app
