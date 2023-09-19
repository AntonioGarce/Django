import random

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def generate_number_order():
    password_letters = [random.choice(numbers) for i in range(6)]
    password_list = password_letters
    random.shuffle(password_list)
    order_num = "".join(password_list)
    return order_num