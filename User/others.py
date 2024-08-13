import random

from working_with_file import read_all_data


def randomer(filename: str, subject: str):
    data = read_all_data(filename)
    if subject == "username":
        lis = [x[subject] for x in data["users"]]
        lis2 = [x["password"] for x in data["users"]]
        random_username = random.randint(1, 10000)
        while random_username in lis or random_username in lis2:
            random_username = random.randint(1, 10000)
        return random_username

    elif subject == "password":
        lis = [x[subject] for x in data["users"]]
        lis2 = [x["username"] for x in data["users"]]
        random_password = random.randint(1, 10000)
        while random_password in lis or random_password in lis2:
            random_password = random.randint(1, 10000)
        return random_password
