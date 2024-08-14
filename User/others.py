import random
import smtplib

from .working_with_file import read_all_data


def randomer(filename: str, subject: str):
    data = read_all_data(filename)
    is_available = False
    if subject == "verification":
        lis = [x["code"] for x in data["codes"]]
        random_code = random.randint(1, 1000)
        while random_code in lis:
            random_code = random.randint(1, 1000)
        return random_code

    elif subject == "username":
        is_available = True
        lis = [x[subject] for x in data["users"]]
        lis2 = [x["password"] for x in data["users"]]

    if is_available:
        random_generation = random.randint(1, 10000)
        while random_generation in lis or random_generation in lis2:
            random_generation = random.randint(1, 10000)
        return random_generation
