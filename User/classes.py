from enum import Enum

from colorama import Fore, init

init(autoreset=True)

prints = Fore.YELLOW


class UserStatus(Enum):
    SUPER = "super"
    ADMIN = "admin"
    TEACHER = "teacher"
    STUDENT = "student"
    PARENT = "parent"


class UserGender(Enum):
    MALE = "male"
    FEMALE = "female"


class User:
    def __init__(self, id_of: int, full_name: str, email: str, phone: str, age: int, gender: UserGender,
                 status: UserStatus, username: any, password: any):
        self.id_of: int = id_of
        self.full_name: str = full_name
        self.email: str = email
        self.phone: str = phone
        self.age: int = age
        self.gender: UserGender = gender
        self.status: UserStatus = status
        self.username: any = username
        self.password: any = password

    def __str__(self):
        return (prints+f"ID {self.id_of}:\n"
                f"    User: {self.full_name}\n"
                f"    Email: {self.email}\n"
                f"    Phone: {self.phone}\n"
                f"    Age: {self.age}\n"
                f"    Gender: {self.gender}\n"
                f"    Status: {self.status}\n"
                f"    Username: {self.username}")


class Student(User):
    def __init__(self, id_of: int, full_name: str, email: str, phone: str, age: int, gender: UserGender,
                 status: UserStatus, username: any, password: any, money: float = 0):
        super().__init__(id_of, full_name, email, phone, age, gender, status, username, password)
        self.money: float = money

    def __str__(self):
        return super().__str__() +prints+ f"\n    Money: {self.money}"


class Group:
    def __init__(self, id_of, name: str, teacher_id: list, max_student: int,
                 start_time: str, end_time: str, status: bool, student_id: list = list):
        self.id_of: int = id_of
        self.name: str = name
        self.teacher_ids: list = teacher_id
        self.student_ids: list = student_id
        self.max_student: int = max_student
        self.start_time: str = start_time
        self.end_time: str = end_time
        self.status: bool = status

    def __str__(self):
        return (prints+f"ID {self.id_of}:\n"
                f"  Name: {self.name}\n"
                f"  Teacher ID: {self.teacher_ids}\n"
                f"  Student IDs: {self.student_ids}\n"
                f"  Max Student: {self.max_student}\n"
                f"  Start Time: {self.start_time}\n"
                f"  End Time: {self.end_time}\n"
                f"  Status: {self.status}")


class CustomOpen:
    def __init__(self, filename: str, mode: str):
        self.filename: str = filename
        self.mode: str = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
