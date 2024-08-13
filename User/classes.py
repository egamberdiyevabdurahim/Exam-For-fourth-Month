from enum import Enum
from datetime import datetime


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
        return (f"ID: {self.id_of}, User: {self.full_name}, Email: {self.email}, Phone: {self.phone},"
                f"Age: {self.age}, Gender: {self.gender}, Status: {self.status}, Username: {self.username}")


class Group:
    def __init__(self, name: str, teacher_id: int, max_student: int,
                 start_time: datetime, end_time: datetime, status: bool):
        self.name: str = name
        self.teacher_id: int = teacher_id
        self.max_student: int = max_student
        self.start_time: datetime = start_time
        self.end_time: datetime = end_time
        self.status: bool = status

    def __str__(self):
        return (f"Name: {self.name}, Teacher ID: {self.teacher_id}, Max Student: {self.max_student},"
                f"Start Time: {self.start_time}, End Time: {self.end_time}, Status: {self.status}")
