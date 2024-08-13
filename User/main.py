from classes import UserGender, UserStatus, User
from working_with_file import read_all_data, write_data
from others import randomer


class Main:
    def create_admin(self, full_name: str, email: str, phone: str, age: int, gender: UserGender):
        """
        Create an admin user
        """
        file_name: str = "users.json"
        data: dict = read_all_data(file_name)
        if data.get("users") is None:
            id_admin: int = 0
        else:
            id_admin: int = max([user["id_of"] for user in data["users"]])
        username: int = randomer(file_name, "username")
        password: int = randomer(file_name, "password")
        user: User = User(id_of=id_admin + 1, full_name=full_name, email=email, phone=phone, age=age,
                          gender=gender, status=UserStatus.ADMIN, username=username, password=password)
        print(f"{full_name} - Admin Created Successfully:\n"
              f"    ID {id_admin}:\n"
              f"        Full Name {full_name}\n"
              f"        Email: {email}\n"
              f"        Phone: +998{phone}\n"
              f"        Age: {age}\n"
              f"        Gender: {gender}\n"
              f"        Username: {username}\n"
              f"        Password: {password}")
