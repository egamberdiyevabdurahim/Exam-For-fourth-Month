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

    elif subject == "password":
        is_available = True
        lis = [x[subject] for x in data["users"]]
        lis2 = [x["username"] for x in data["users"]]

    if is_available:
        random_generation = random.randint(1, 10000)
        while random_generation in lis or random_generation in lis2:
            random_generation = random.randint(1, 10000)
        return random_generation


def dry1(file_name):
    data: dict = read_all_data(file_name)
    if data.get("users") is None:
        id_student: int = 0
    else:
        id_student: int = max([user["id_of"] for user in data["users"]])
    username: int = randomer(file_name, "username")
    password: int = randomer(file_name, "password")
    return username, password, id_student, data


smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_sender = 'egamberdiyevabdurahim@gmail.com'
smtp_password = 'yctu zenu eewo drdc'


def send_mail(to_user, subject, message):
    email = f"Subject: {subject}\n\n{message}"
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_sender, smtp_password)
        server.sendmail(smtp_sender, to_user, email)
        server.quit()
    except smtplib.SMTPException as e:
        print(f"Failed {e}")
