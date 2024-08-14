import threading

from colorama import Fore, init
from datetime import datetime

from User.classes import UserGender, UserStatus, User, Group, Student
from User.working_with_file import read_all_data, write_data
from User.others import dry1, send_mail
from User.validators import validate_email, validate_phone, validate_gender

init(autoreset=True)

error = Fore.RED
enter = Fore.CYAN
re_enter = Fore.MAGENTA
success = Fore.LIGHTGREEN_EX
prints = Fore.YELLOW
command = Fore.LIGHTCYAN_EX


class Main:
    file_name: str = "users.json"
    group_file_name: str = "groups.json"

    # SUPER ADMIN
    def create_admin(self, full_name: str, email: str, phone: str, age: int, gender: str) -> User:
        """
        Create an admin user
        """
        while not validate_email(email):
            print(error+"Invalid email\nPlease enter a valid email or enter stop for exit&logout")
            email: str = input(re_enter+"Re-Enter Email: ")
            if email.lower() == "stop":
                exit()

        while not validate_phone(phone):
            print(error+"Invalid phone number\nPlease enter a valid phone number or enter stop for exit&logout")
            phone: str = input(re_enter+"Re-Enter Phone: ")
            if phone.lower() == "stop":
                exit()

        while gender not in ["m", "f"]:
            print(error + "Invalid gender!\nPlease enter a gender or enter stop for Exit&Logout")
            gender = input(re_enter + "Re-Enter Gender: ")
            if phone.lower() == "stop":
                exit()

        if gender == 'm':
            gender = UserGender.MALE.value
        elif gender == 'f':
            gender = UserGender.FEMALE.value

        dry_1 = dry1(self.file_name)
        print("dry:", dry_1)
        username: int = dry_1[0]
        password: int = dry_1[1]
        id_admin: int = dry_1[2]
        data: dict = dry_1[3]
        user: User = User(id_of=id_admin + 1, full_name=full_name, email=email, phone=phone, age=age,
                          gender=gender, status=UserStatus.ADMIN.value, username=username, password=password)
        print(success+f"{full_name} - Admin Created Successfully:\n")
        print(prints+f"    ID {id_admin}:\n"
              f"        Full Name {full_name}\n"
              f"        Email: {email}\n"
              f"        Phone: +998{phone}\n"
              f"        Age: {age}\n"
              f"        Gender: {gender}\n"
              f"        Username: {username}\n"
              f"        Password: {password}")
        data["users"].append({
            "id_of": user.id_of,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "age": user.age,
            "gender": user.gender,
            "status": user.status,
            "username": user.username,
            "password": user.password
        })
        write_data(self.file_name, data)
        return user

    def create_user(self, full_name: str, email: str, phone: str,
                    age: int, gender: str, status: UserStatus) -> User:
        """
        Create a user
        """
        while not validate_email(email):
            print(error+"Invalid email\nPlease enter a valid email or enter stop for exit&logout")
            email: str = input(re_enter+"Re-Enter Email: ")
            if email.lower() == "stop":
                exit()

        while not validate_phone(phone):
            print(error+"Invalid phone number\nPlease enter a valid phone number or enter stop for exit&logout")
            phone: str = input(re_enter+"Re-Enter Phone: ")
            if phone.lower() == "stop":
                exit()

        while gender not in ["m", "f"]:
            print(error + "Invalid gender!\nPlease enter a gender or enter stop for Exit&Logout")
            gender = input(re_enter + "Re-Enter Gender: ")
            if phone.lower() == "stop":
                exit()

        if gender == 'm':
            gender = UserGender.MALE.value
        elif gender == 'f':
            gender = UserGender.FEMALE.value

        dry_1: dict = dry1(self.file_name)
        username: int = dry_1[0]
        password: int = dry_1[1]
        id_user: int = dry_1[2]
        data: dict = dry_1[3]
        if status == UserStatus.TEACHER.value:
            user: User = User(id_of=id_user + 1, full_name=full_name, email=email, phone=phone, age=age,
                              gender=gender, status=status, username=username, password=password)
            print(success+f"{full_name} - {str(status).capitalize()} Created Successfully:\n")
            print(prints+f"    ID {id_user}:\n"
                  f"        Full Name {full_name}\n"
                  f"        Email: {email}\n"
                  f"        Phone: +998{phone}\n"
                  f"        Age: {age}\n"
                  f"        Gender: {gender}\n"
                  f"        Status: {status}\n"
                  f"        Username: {username}\n"
                  f"        Password: {password}")
            data["users"].append({
                "id_of": user.id_of,
                "full_name": user.full_name,
                "email": user.email,
                "phone": user.phone,
                "age": user.age,
                "gender": user.gender,
                "status": user.status,
                "username": user.username,
                "password": user.password,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            write_data(self.file_name, data)
            return user
        elif status == UserStatus.STUDENT.value:
            user: Student = Student(id_of=id_user + 1, full_name=full_name, email=email, phone=phone, age=age,
                                    gender=gender, status=status, username=username, password=password)
            print(success+f"{full_name} - {str(status).capitalize()} Created Successfully:\n")
            print(prints+f"    ID {user.id_of}:\n"
                  f"        Full Name {full_name}\n"
                  f"        Email: {email}\n"
                  f"        Phone: +998{phone}\n"
                  f"        Age: {age}\n"
                  f"        Money: {user.money}\n"
                  f"        Gender: {gender}\n"
                  f"        Status: {status}\n"
                  f"        Username: {username}\n"
                  f"        Password: {password}")
            data["users"].append({
                "id_of": user.id_of,
                "full_name": user.full_name,
                "email": user.email,
                "phone": user.phone,
                "age": user.age,
                "money": user.money,
                "gender": user.gender,
                "status": user.status,
                "username": user.username,
                "password": user.password,
                "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            write_data(self.file_name, data)
            return user

    def edit_user_by_id(self, status: UserStatus):
        """
        Edit a user by ID
        """
        self.get_all_users_by_type(status=status)
        print(command+"Birortasini Edit Qilish Uchun ID-sini Kiriting!")
        choice: str = input(enter+"Enter: ")
        while not choice.isdigit():
            print(error+"Invalid input\nPlease enter a valid or enter stop for exit and logout")
            choice = input(re_enter+"Re-Enter: ")
            if choice == "stop":
                return
        data: dict = read_all_data(self.file_name)
        new_dat: dict = {"users": []}
        for dat in data["users"]:
            state: bool = True
            if dat["status"] == status:
                if dat["id_of"] == int(choice):
                    print(command+"1. Edit Full Name\n"
                          "2. Edit Email\n"
                          "3. Edit Phone\n"
                          "4. Edit Age\n"
                          "5. Edit Gender\n"
                          "6. Edit Status\n"
                          "7. Delete User\n"
                          "8. Exit")
                    second_choice: str = input(enter+"Enter: ")
                    mess: bool = True
                    while not second_choice.isdigit() or int(second_choice) < 1 or int(second_choice) > 7:
                        print(error+"Invalid input\nPlease enter a valid number between 1 and 7"
                              " or enter stop for exit&logout")
                        second_choice = input(re_enter+"Re-Enter: ")
                        if second_choice == "stop":
                            state: bool = False
                            break
                    if mess:
                        second_choice: int = int(second_choice)
                        if second_choice == 1:
                            new_name: str = input(enter+"New Full Name: ")
                            dat["full_name"] = new_name
                            print(f"Full Name changed to {new_name}")

                        elif second_choice == 2:
                            new_email: str = input("New Email: ")
                            mess: bool = True
                            while not validate_email(new_email):
                                print(error+"Invalid email\nPlease enter a valid email or enter stop for exit&logout")
                                new_email: str = input(re_enter+"Re-Enter Email: ")
                                if new_email.lower() == "stop":
                                    mess: bool = False
                                    break
                            if mess:
                                dat["email"] = new_email
                                print(success+f"Email changed to {new_email}")

                        elif second_choice == 3:
                            new_phone: str = input(enter+"New Phone: ")
                            mess: bool = True
                            while not validate_phone(new_phone):
                                print(error+
                                    "Invalid phone number\nPlease enter a valid phone number"
                                    " or enter stop for exit&logout")
                                new_phone: str = input(re_enter+"Re-Enter Phone: ")
                                if new_phone.lower() == "stop":
                                    mess: bool = False
                                    break
                            if mess:
                                dat["phone"] = new_phone
                                print(success+f"Phone changed to +998{new_phone}")

                        elif second_choice == 4:
                            new_age: int = int(input(enter+"New Age: "))
                            dat["age"] = new_age
                            print(success+f"Age changed to {new_age}")

                        elif second_choice == 5:
                            new_gender: str = input(enter+"New Gender (m/f): ")
                            mess: bool = True
                            while validate_gender(new_gender):
                                print(error+"Invalid gender\nPlease enter a valid gender (m/f) or enter stop for exit&logout")
                                new_gender: str = input(re_enter+"Re-Enter: ")
                                if new_gender.lower() == "stop":
                                    mess: bool = False
                                    break
                            if mess:
                                if new_gender == "m":
                                    dat["gender"] = UserGender.MALE.value
                                    new_gender: str = UserGender.MALE.value
                                elif new_gender == "f":
                                    dat["gender"] = UserGender.FEMALE.value
                                    new_gender: str = UserGender.FEMALE.value
                                print(success+f"Gender changed to {new_gender}")

                        elif second_choice == 6:
                            new_status: str = input(enter+"New Status(admin/student/teacher): ")
                            mess: bool = True
                            while new_status.lower() not in ('admin', 'student', 'teacher'):
                                print(error+"Invalid status\nPlease enter a valid status (admin/student/teacher)"
                                      " or enter stop for exit&logout")
                                new_status: str = input(re_enter+"Re-Enter: ")
                                if new_status.lower() == "stop":
                                    mess: bool = False
                                    break
                            if mess:
                                if new_status == "admin":
                                    dat["status"] = UserStatus.ADMIN.value
                                    new_status: str = UserStatus.ADMIN.value
                                elif new_status == "student":
                                    dat["status"] = UserStatus.STUDENT.value
                                    new_status: str = UserStatus.STUDENT.value
                                elif new_status == "teacher":
                                    dat["status"] = UserStatus.TEACHER.value
                                    new_status: str = UserStatus.TEACHER.value
                                print(success+f"Status changed to {new_status}")

                        elif second_choice == 7:
                            print(success+f"User with ID {int(choice)} deleted successfully!")
                            state = False

                        elif second_choice == 8:
                            pass
            if state:
                new_dat["users"].append(dat)
        write_data(self.file_name, new_dat)
        return

    def get_all_users_by_type(self, status: UserStatus):
        """
        Get all users by type
        """
        data: dict = read_all_data(self.file_name)
        message: bool = False
        for user in data["users"]:
            if user["status"] == status:
                if status == UserStatus.TEACHER.value:
                    message = True
                    user_info: User = User(id_of=user['id_of'], full_name=user["full_name"], email=user["email"],
                                           phone=user["phone"], age=user["age"], gender=user["gender"],
                                           status=user["status"], username=user["username"], password=user["password"])
                    print(user_info)
                    print("--------------------")

                elif status == UserStatus.STUDENT.value:
                    message = True
                    user_info: Student = Student(id_of=user['id_of'], full_name=user["full_name"],
                                                 email=user["email"], phone=user["phone"], age=user["age"],
                                                 gender=user["gender"], status=user["status"],
                                                 username=user["username"], password=user["password"],
                                                 money=user["money"])
                    print(user_info)
                    print("--------------------")

                elif status == UserStatus.ADMIN.value:
                    message = True
                    user_info: Student = Student(id_of=user['id_of'], full_name=user["full_name"],
                                                 email=user["email"], phone=user["phone"], age=user["age"],
                                                 gender=user["gender"], status=user["status"],
                                                 username=user["username"], password=user["password"])
                    print(user_info)
                    print("--------------------")
        if not message:
            print(error+"No users found with the given status!")
        return message

    def send_mail(self, male: UserGender = None, female: UserGender = None):
        """
        Send mail to male, female and all users
        """
        data: dict = read_all_data(self.file_name)
        subject: str = input(enter+"Enter Subject: ")
        body: str = input(enter+"Enter Text: ")
        print(success+"Mails sent successfully!")
        for user in data["users"]:
            if male:
                if user["gender"] == male:
                    threading.Thread(target=send_mail, args=(user["email"], subject, body)).start()

            elif female:
                if user["gender"] == female:
                    threading.Thread(target=send_mail, args=(user["email"], subject, body)).start()

            else:
                threading.Thread(target=send_mail, args=(user["email"], subject, body)).start()

        return

    # ADMIN
    def create_group(self, name: str, teacher: str, max_student: int,
                     start_time: str, end_time: str) -> Group:
        """
        Create a new group
        """
        data: dict = read_all_data(self.group_file_name)
        if data.get("groups") is None:
            id_group: int = 0
        else:
            id_group: int = max([user["id_of"] for user in data["groups"]])
        group: Group = Group(id_of=id_group + 1, name=name, teacher_id=list(teacher), max_student=max_student,
                             start_time=start_time, end_time=end_time, status=False)
        print(success+f"{name} - Group Created Successfully:\n")
        print(prints+f"    ID {id_group}:\n"
              f"        Name: {name}\n"
              f"        Teacher ID: {teacher}\n"
              f"        Max Student: {max_student}\n"
              f"        Start Time: {start_time}\n"
              f"        End Time: {end_time}\n")
        if data == {}:
            data["groups"] = []
        data["groups"].append({
            "id_of": group.id_of,
            "name": group.name,
            "teacher_ids": group.teacher_ids,
            "student_ids": [],
            "max_student": group.max_student,
            "start_time": group.start_time,
            "end_time": group.end_time,
            "status": group.status,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        write_data(self.group_file_name, data)
        return group

    def edit_group_by_id(self):
        """
        Edit a group by ID
        """
        data: dict = read_all_data(self.group_file_name)
        for group in data["groups"]:
            group_info: Group = Group(id_of=group['id_of'], name=group["name"], teacher_id=group["teacher_ids"],
                                      student_id=group["student_ids"], max_student=group["max_student"],
                                      start_time=group["start_time"],
                                      end_time=group["end_time"],
                                      status=group["status"])
            print(group_info)
            print("--------------------")
        choice: str = input(enter+"Enter group ID to edit: ")
        mess: bool = True
        while not choice.isdigit() or int(choice) < 1:
            print(error+"Invalid input\nPlease enter a valid group ID or enter stop for exit")
            choice: str = input(re_enter+"Re-Enter: ")
            if choice == "stop":
                mess: bool = False
                break
        if mess:
            choice: int = int(choice)
            new_dat: dict = {"groups": []}
            for group in data["groups"]:
                state: bool = True
                if group["id_of"] == choice:
                    print(command+"1. Edit Name\n"
                          "2. Edit Max Student\n"
                          "3. Delete Group\n"
                          "4. Exit")
                    second_choice: str = input(enter+"Enter: ")
                    while not second_choice.isdigit() or int(second_choice) < 1 or int(second_choice) > 6:
                        print(error+"Invalid gender\nPlease enter a valid gender (m/f) or enter stop for exit&logout")
                        second_choice: str = input(re_enter+"Re-Enter: ")
                        if second_choice.lower() == "stop":
                            pass

                    if second_choice == "1":
                        new_name: str = input(enter+"New Name: ")
                        group["name"] = new_name
                        print(success+f"Name changed to {new_name}")

                    elif second_choice == "2":
                        new_max_student: str = input(enter+"New Max Student: ")
                        group["max_student"] = int(new_max_student)
                        print(success+f"Max Student changed to {new_max_student}")

                    elif second_choice == "3":
                        print(success+f"Group with ID {int(choice)} deleted successfully!")
                        state = False

                    elif second_choice == "4":
                        pass
                if state:
                    new_dat["groups"].append(group)
            write_data(self.group_file_name, new_dat)
            return

    def get_all_groups(self):
        """
        Get all groups
        """
        data: dict = read_all_data(self.group_file_name)
        for group in data["groups"]:
            group_info: Group = Group(id_of=group['id_of'], name=group["name"], teacher_id=group["teacher_ids"],
                                      student_id=group["student_ids"], max_student=group["max_student"],
                                      start_time=group["start_time"],
                                      end_time=group["end_time"],
                                      status=group["status"])
            print(group_info)
            print("--------------------")

    def add_student_to_group(self, group_id: int, student_id: int):
        """
        Add a student to a group
        """
        data: dict = read_all_data(self.group_file_name)
        if data.get("groups") is None:
            print(error+"No groups found!")
            return
        new_data: dict = {"groups": []}
        message: bool = False
        for group in data["groups"]:
            if int(group["id_of"]) == group_id:
                message: bool = True
                if len(group["student_ids"]) < group["max_student"]:
                    if student_id in group["student_ids"]:
                        print(error+"Student already exists in the group!")
                        continue
                    dat = read_all_data(self.file_name)
                    lis = [x["id_of"] for x in dat["users"]]
                    if student_id in lis:
                        group["student_ids"].append(student_id)
                        print(success+f"Student with ID {student_id} added to group with ID {group_id} successfully!")
                    else:
                        print(error+"Student not found!")
                else:
                    print(error+"Group is full!")
            new_data["groups"].append(group)
        write_data(self.group_file_name, new_data)
        if not message:
            print(error+f"Group with ID {group_id} not found!")
            return

    def remove_student_from_group(self, group_id: int, student_id: int):
        """
        Remove a student from a group
        """
        data: dict = read_all_data(self.group_file_name)
        if data.get("groups") is None:
            print(error+"No groups found!")
            return
        new_data: dict = {"groups": []}
        message: bool = False
        message2: bool = False
        for group in data["groups"]:
            if int(group["id_of"]) == group_id:
                message: bool = True
                if student_id in group["student_ids"]:
                    message2: bool = True
                    group["student_ids"].remove(student_id)
                    print(success+f"Student with ID {student_id} removed from group with ID {group_id} successfully!")
            new_data["groups"].append(group)
        write_data(self.group_file_name, new_data)
        if not message:
            print(error+f"Group with ID {group_id} not found!")
            return
        if not message2:
            print(error+"Student not found in the group!")
            return

    def add_teacher_to_group(self, teacher_id, group_id: int):
        """
        Add a teacher to a group
        """
        data: dict = read_all_data(self.group_file_name)
        if data.get("groups") is None:
            print(error+"No groups found!")
            return
        new_data: dict = {"groups": []}
        message: bool = False
        for group in data["groups"]:
            if int(group["id_of"]) == group_id:
                message: bool = True
                if teacher_id not in group["teacher_ids"]:
                    group["teacher_ids"].append(teacher_id)
                    print(success+f"Teacher with ID {teacher_id} added to group with ID {group_id} successfully!")
                else:
                    print(error+"Teacher already exists in the group!")
            new_data["groups"].append(group)
        write_data(self.group_file_name, new_data)
        if not message:
            print(error+f"Group with name is not found in the group!")
            return

    def remove_teacher_from_group(self, teacher_id, group_id: int):
        """
        Remove a teacher from a group
        """
        data: dict = read_all_data(self.group_file_name)
        if data.get("groups") is None:
            print(error+"No groups found!")
            return
        new_data: dict = {"groups": []}
        message: bool = False
        for group in data["groups"]:
            if int(group["id_of"]) == group_id:
                message: bool = True
                if teacher_id in group["teacher_ids"]:
                    group["teacher_ids"].remove(teacher_id)
                    print(success+f"Teacher with ID {teacher_id} removed from group with ID {group_id} successfully!")
                else:
                    print(error+"Teacher not found in the group!")
            new_data["groups"].append(group)
        write_data(self.group_file_name, new_data)
        if not message:
            print(error+f"Group with name is not found in group!")

    def get_student_by_id_or_by_name(self, student_id: int = None, name: str = None, type_of: bool = None):
        """
        Get a student by ID or by name
        """
        data: dict = read_all_data(self.file_name)
        if data.get("users") is None:
            print(error+"No users found!")
            return
        mess: bool = False
        if student_id:
            for user in data["users"]:
                if user["id_of"] == student_id:
                    user_info: User = User(id_of=user['id_of'], full_name=user["full_name"], email=user["email"],
                                           phone=user["phone"], age=user["age"], gender=user["gender"],
                                           status=user["status"], username=user["username"], password=user["password"])
                    if type_of is None:
                        print(user_info)
                    return user
            print(error+"User Not Found")
        elif name:
            for user in data["users"]:
                if user["full_name"].lower() == name.lower() or name.lower() in user["full_name"].lower():
                    mess: bool = True
                    user_info: User = User(id_of=user['id_of'], full_name=user["full_name"], email=user["email"],
                                           phone=user["phone"], age=user["age"], gender=user["gender"],
                                           status=user["status"], username=user["username"], password=user["password"])
                    print(user_info)
            if not mess:
                print(error+"User Not Found")

    def transfer_money_for_student(self, student_id: int, money: float):
        """
        Transfer money to a student's account
        """
        data: dict = read_all_data(self.file_name)
        if data.get("users") is None:
            print(error+"No users found!")
            return
        new_data: dict = {"users": []}
        message: bool = False
        for user in data["users"]:
            if user["id_of"] == student_id:
                message: bool = True
                user["money"] += money
                print(success+f"Successfully transferred {money} to {user['full_name']}'s account!")
            new_data["users"].append(user)
        write_data(self.file_name, new_data)
        if not message:
            print(error+f"User with ID {student_id} not found!")
            return

    # TEACHER

    def get_student_by_group_id(self, group_id: int):
        """
        Get all students by a group
        """
        data: dict = read_all_data(self.group_file_name)
        if data.get("groups") is None:
            print(error+"No groups found!")
            return
        counter: int = 0
        for group in data["groups"]:
            if int(group["id_of"]) == group_id:
                counter += 1
                for user in group["student_ids"]:
                    user = self.get_student_by_id_or_by_name(student_id=user, type_of=True)
                    user_info: Student = Student(id_of=user['id_of'], full_name=user["full_name"],
                                                 email=user["email"], phone=user["phone"], age=user["age"],
                                                 gender=user["gender"], status=user["status"],
                                                 username=user["username"], password=user["password"],
                                                 money=user["money"])
                    print(user_info)
                    print("--------------------")
        print(f"\nTotal Students = {counter}\n")

    def get_groups_by_teacher(self, teacher_id: str, type_of: bool = None):
        """
        Get all groups by a teacher
        """
        data: dict = read_all_data(self.group_file_name)
        if data.get("groups") is None:
            print(error+"No groups found!")
            return None
        counter: int = 0
        for group in data["groups"]:
            if teacher_id in group["teacher_ids"]:
                counter += 1
                gr: Group = Group(id_of=group["id_of"], name=group["name"], teacher_id=group["teacher_ids"],
                                  max_student=group["max_student"], start_time=group["start_time"],
                                  end_time=group["end_time"], status=group["status"])
                print(gr)
                print("--------------------")
        if type_of is None:
            print(f"\nTotal Groups = {counter}\n")
            if counter > 0:
                print(command+"Enter Group ID for get students in group or enter stop for exit")
                choice: str = input(enter+"Enter: ")
                if choice == "stop":
                    return
                while not choice.isdigit():
                    print(error+"Invalid input. Please enter a number or enter stop for exit")
                    choice = input(re_enter+"Re-Enter: ")
                    if choice == "stop":
                        return
                self.get_student_by_group_id(int(choice))
        return None

    def start_lesson(self, group_id: int):
        """
        Start a lesson
        """
        data: dict = read_all_data(self.group_file_name)
        if data.get("groups") is None:
            print(error+"No groups found!")
            return
        new_data: dict = {"groups": []}
        mess: bool = False
        for group in data["groups"]:
            if group["id_of"] == group_id:
                mess: bool = True
                if group["status"]:
                    print(error+"Group's Lesson Already Started!")
                else:
                    print(success+"Lesson started successfully!")
                    group["status"] = True
            new_data["groups"].append(group)
        write_data(self.group_file_name, new_data)
        if not mess:
            print(error+f"Group with ID {group_id} not found!")

    def end_lesson(self, group_id: int):
        """
        End a lesson
        """
        data: dict = read_all_data(self.group_file_name)
        if data.get("groups") is None:
            print(error+"No groups found!")
            return
        new_data: dict = {"groups": []}
        mess: bool = False
        for group in data["groups"]:
            if group["id_of"] == group_id:
                mess: bool = True
                if not group["status"]:
                    print(error+"Group's Lesson Already Ended!")
                else:
                    print(success+"Lesson ended successfully!")
                    group["status"] = False
            new_data["groups"].append(group)
        write_data(self.group_file_name, new_data)
        if not mess:
            print(error+f"Group with ID {group_id} not found!")

    def status_of_lesson(self, group_id: int):
        """
        Status of a lesson
        """
        data: dict = read_all_data(self.group_file_name)
        if data.get("groups") is None:
            print(error+"No groups found!")
            return
        message: bool = False
        for group in data["groups"]:
            if group["id_of"] == group_id:
                message: bool = True
                print(prints+f"Lesson Status: {group['status']}")
        if not message:
            print(error+f"Group with ID {group_id} not found!")

    def start_or_end_lesson(self, group_id: int):
        """
        Start or end a lesson
        """
        data: dict = read_all_data(self.group_file_name)
        if data.get("groups") is None:
            print(error+"No groups found!")
            return
        message: bool = False
        for group in data["groups"]:
            if group["id_of"] == group_id:
                message: bool = True
                print(success+"Group is found!")
                print(command+"1. Start Lesson\n"
                      "2. End Lesson\n"
                      "3. Status of Lesson\n"
                      "4. Exit")
                choice: str = input(enter+"Enter: ")
                if choice == "1":
                    self.start_lesson(group_id)

                elif choice == "2":
                    self.end_lesson(group_id)

                elif choice == "3":
                    self.status_of_lesson(group_id)

                elif choice == "4":
                    return
        if not message:
            print(error+f"Group with ID {group_id} not found!")

    # STUDENT
    def get_all_groups_by_student(self, student_id: int):
        """
        Get all groups by a student
        """
        data: dict = read_all_data(self.group_file_name)
        if data.get("groups") is None:
            print(error+"No groups found!")
            return
        counter: int = 0
        for group in data["groups"]:
            if student_id in group["student_ids"]:
                counter += 1
                gr: Group = Group(id_of=group["id_of"], name=group["name"], teacher_id=group["teacher_ids"],
                                  max_student=group["max_student"], start_time=group["start_time"],
                                  end_time=group["end_time"], status=group["status"], student_id=group["student_ids"])
                print(gr)
                print("--------------------")
        print(f"\nTotal Groups = {counter}\n")
        return None

    def get_balance(self, student_id: int):
        """
        Get student's balance
        """
        data: dict = read_all_data(self.file_name)
        if data.get("users") is None:
            print(error+"No users found!")
            return None
        for user in data["users"]:
            if user["id_of"] == student_id:
                print(f"Balance: {user['money']}")
                return None
        print(error+"User Not Found")
        return None

    def edit_student(self, student_id: str):
        """
        Edit student data
        """
        data: dict = read_all_data(self.file_name)
        choice: int = int(student_id)
        new_dat: dict = {"users": []}
        for user in data["users"]:
            state: bool = True
            if user["id_of"] == choice:
                print(command+"1. Edit Full Name\n"
                      "2. Edit Email\n"
                      "3. Edit Phone\n"
                      "4. Edit Age\n"
                      "5. Edit Gender\n"
                      "6. Delete User\n"
                      "7. Exit")
                second_choice: str = input("Enter: ")
                while not second_choice.isdigit() or int(second_choice) < 1 or int(second_choice) > 6:
                    print(error+"Invalid gender\nPlease enter a valid gender (m/f) or enter stop for exit&logout")
                    second_choice: str = input(re_enter+"Re-Enter: ")
                    if second_choice.lower() == "stop":
                        pass

                if second_choice == "1":
                    new_name: str = input(enter+"New Full Name: ")
                    user["full_name"] = new_name
                    print(success+f"Full Name changed to {new_name}")

                elif second_choice == "2":
                    new_emil: str = input(enter+"New Email: ")
                    user["email"] = new_emil
                    print(success+f"Email changed to {new_emil}")

                elif second_choice == "3":
                    new_phone: str = input(enter+"New Phone: ")
                    user["phone"] = new_phone
                    print(success+f"Phone changed to {new_phone}")

                elif second_choice == "4":
                    new_age: str = input(enter+"New Age: ")
                    while not new_age.isdigit():
                        print(error+"Invalid age\nPlease enter a valid age or enter stop for Exit&Logout")
                        new_age: str = input(re_enter+"Re-Enter: ")
                        if second_choice.lower() == "stop":
                            pass

                elif second_choice == "5":
                    new_gender: str = input(enter+"New Gender (m/f): ")
                    while new_gender.lower() not in ["m", "f"]:
                        print(error+"Invalid gender\nPlease enter a valid gender (m/f) or enter stop for exit&logout")
                        new_gender: str = input(re_enter+"Re-Enter: ")
                        if second_choice.lower() == "stop":
                            pass

                    if new_gender == "m":
                        user["gender"] = UserGender.MALE.value
                        new_gender = UserGender.MALE.value
                    elif new_gender == "f":
                        user["gender"] = UserGender.FEMALE.value
                        new_gender = UserGender.FEMALE.value
                    print(success+f"Gender changed to {new_gender}")

                elif second_choice == "6":
                    print(success+"User deleted successfully!")
                    state: bool = False

                elif second_choice == "7":
                    pass
            if state:
                new_dat["users"].append(user)
        write_data(self.file_name, new_dat)
        return None

    def get_info(self, student_id: str):
        """
        Get student's information
        """
        data: dict = read_all_data(self.file_name)
        if data.get("users") is None:
            print(error+"No users found!")
            return
        for user in data["users"]:
            if user["id"] == student_id:
                print(prints+f"Full Name: {user['full_name']}\n"
                      f"Email: {user['email']}\n"
                      f"Phone: {user['phone']}\n"
                      f"Age: {user['age']}\n"
                      f"Gender: {user['gender']}\n"
                      f"Status: {user['status']}\n"
                      f"Username: {user['username']}\n"
                      f"Password: {user['password']}\n"
                      f"Money: {user['money']}")
        print(error+"User Not Found")
        return

    # USER
    def login(self, username: str, password: str) -> User or None:
        """
        Login to the system
        """
        data: dict = read_all_data(self.file_name)
        for user in data["users"]:
            if str(user["username"]) == username:
                if password == str(user["password"]):
                    print(success+f"{user['full_name']} - Logged In Successfully!")
                    user_info: User = User(id_of=user['id_of'], full_name=user["full_name"],
                                           email=user["email"], phone=user["phone"], age=user["age"],
                                           gender=user["gender"], status=user["status"],
                                           username=user["username"], password=user["password"])
                    return user_info
                else:
                    print(error+"Wrong password!")
                    return
        print(error+"User Not Found")
        return


main = Main()


def send_mail_command():
    while True:
        print("Main/AfterLoginSuperAdmin/SendMail/")
        print(command + "1. Send Email to Male\n"
                        "2. Send Email to Female\n"
                        "3. Send Email to All\n"
                        "4. Exit")
        choice: str = input(enter + "Enter: ")
        if choice == "1":
            main.send_mail(UserGender.MALE.value)

        elif choice == "2":
            main.send_mail(UserGender.FEMALE.value)

        elif choice == "3":
            main.send_mail()

        else:
            print(success + "Exiting...")
            break


def after_login_super(user: User):
    print(f"{success}Welcome, {user.full_name}!")
    while True:
        print("Main/AfterLoginSuperAdmin/")
        print(command + "1. Create New Admin\n"
                        "2. Get All Admins\n"
                        "3. Edit or Delete Admin\n"
                        "4. Create New Teacher\n"
                        "5. Get All Teachers\n"
                        "6. Edit or Delete Teacher\n"
                        "7. Send Email\n"
                        "8. LogOut")
        choice: str = input(enter + "Enter: ")
        if choice == "1":
            full_name: str = input(enter + "Enter Admin Full Name: ")
            email: str = input(enter + "Enter Admin Email: ")
            phone: str = input(enter + "Enter Admin Phone: ")
            age: str = input(enter + "Enter Admin Age: ")
            gender = input(enter + "Enter Admin Gender (m/f): ")

            main.create_admin(full_name=full_name, email=email, phone=phone,
                              age=int(age), gender=gender)
        elif choice == "2":
            main.get_all_users_by_type(UserStatus.ADMIN.value)

        elif choice == "3":
            main.edit_user_by_id(UserStatus.ADMIN.value)

        elif choice == "4":
            name: str = input(enter + "Enter New Teacher Full Name: ")
            email: str = input(enter + "Enter New Teacher Email: ")
            phone: str = input(enter + "Enter New Teacher Phone: ")
            age: str = input(enter + "Enter New Teacher Age: ")
            gender = input(enter + "Enter New Teacher Gender (m/f): ")

            main.create_user(full_name=name, email=email, phone=phone,
                             age=int(age), gender=gender, status=UserStatus.TEACHER.value)

        elif choice == "5":
            main.get_all_users_by_type(UserStatus.TEACHER.value)

        elif choice == "6":
            main.edit_user_by_id(UserStatus.TEACHER.value)

        elif choice == "7":
            send_mail_command()

        elif choice == "8":
            print(success + "Exiting...")
            break


def after_login_adm(user: User):
    print(f"{success}Welcome, {user.full_name}!")
    while True:
        print("Main/AfterLoginAdmin/")
        print(command + "1. Create New Group\n"
                        "2. Get All Groups\n"
                        "3. Edit or Delete Group\n"
                        "4. Create New Student\n"
                        "5. Get All Students\n"
                        "6. Edit or Delete Student\n"
                        "7. Find Student By Name or ID\n"
                        "8. Get Payment for Student\n"
                        "9. Add Teacher to Group\n"
                        "10. Remove Teacher from Group\n"
                        "11. Add Student to Group\n"
                        "12. Remove Student from Group\n"
                        "13. LogOut")
        choice: str = input(enter + "Enter: ")
        if choice == "1":
            main.get_all_users_by_type(UserStatus.TEACHER.value)
            choice: str = input(enter + "Enter Teacher ID: ")
            name: str = input(enter + "Enter Group Name: ")
            max_student: str = input(enter + "Max Student Number: ")
            start_time: str = input(enter + "Start Date(01.01.2000): ")
            end_time: str = input(enter + "End Time(08.08.2000): ")
            main.create_group(teacher=choice, name=name, max_student=int(max_student),
                              start_time=start_time,
                              end_time=end_time)

        elif choice == "2":
            main.get_all_groups()

        elif choice == "3":
            main.edit_group_by_id()

        elif choice == "4":
            full_name: str = input(enter+"Enter Full Name: ")
            email: str = input(enter+"Enter Email: ")
            phone: str = input(enter+"Enter Phone: ")
            age: str = input(enter+"Enter Age: ")
            gender: str = input(enter+"Enter Gender (m/f): ")
            main.create_user(full_name=full_name, email=email, phone=phone, age=int(age), gender=gender,
                             status=UserStatus.STUDENT.value)

        elif choice == "5":
            main.get_all_users_by_type(UserStatus.STUDENT.value)

        elif choice == "6":
            main.edit_user_by_id(status=UserStatus.STUDENT.value)

        elif choice == "7":
            name_or_id: str = input(enter+"Enter Name or ID: ")
            if name_or_id.isdigit():
                main.get_student_by_id_or_by_name(student_id=int(name_or_id))
            else:
                main.get_student_by_id_or_by_name(name=name_or_id)

        elif choice == "8":
            main.get_all_users_by_type(UserStatus.STUDENT.value)
            student: str = input("Enter Student ID: ")
            while not student.isdigit():
                print(error + "Invalid ID.\n"
                              "stop for Exit")
                student = input(re_enter+"Re-Enter ID: ")
                if student == "stop":
                    exit()
            amount: str = input("Enter Amount: ")
            while not amount.isdigit() and float(amount) < 1.:
                print(error + "Invalid Amount.\n"
                              "stop for Exit")
                amount = input(re_enter+"Re-Enter Amount: ")
                if amount == "stop":
                    exit()
            main.transfer_money_for_student(int(student), float(amount))

        elif choice == "9":
            main.get_all_users_by_type(UserStatus.TEACHER.value)
            choice: str = input(enter + "Enter Teacher ID: ")
            main.get_all_groups()
            choice2: str = input(enter + "Enter Group ID: ")
            main.add_teacher_to_group(teacher_id=choice, group_id=int(choice2))

        elif choice == "10":
            main.get_all_users_by_type(UserStatus.TEACHER.value)
            choice: str = input(enter + "Enter Teacher ID: ")
            main.get_all_groups()
            choice2: str = input(enter + "Enter Group ID: ")
            main.remove_teacher_from_group(teacher_id=choice, group_id=int(choice2))

        elif choice == "11":
            main.get_all_users_by_type(UserStatus.STUDENT.value)
            choice: str = input(enter + "Enter Student ID: ")
            main.get_all_groups()
            choice2: str = input(enter + "Enter Group ID: ")
            main.add_student_to_group(student_id=int(choice), group_id=int(choice2))

        elif choice == "12":
            main.get_all_users_by_type(UserStatus.STUDENT.value)
            choice: str = input(enter + "Enter Student ID: ")
            main.get_all_groups()
            choice2: str = input(enter + "Enter Group ID: ")
            main.remove_student_from_group(student_id=int(choice), group_id=int(choice2))

        elif choice == "13":
            print(success + "Exiting...")
            break


def after_login_teacher(user: User):
    print(f"{success}Welcome, {user.full_name}!")
    while True:
        print("Main/AfterLoginTeacher/")
        print(command + "1. Get My Groups\n"
                        "2. Get Students By Group\n"
                        "3. Start or End Lesson\n"
                        "4. LogOut")
        choice: str = input(enter + "Enter: ")
        if choice == "1":
            main.get_groups_by_teacher(str(user.id_of))

        elif choice == "2":
            main.get_groups_by_teacher(str(user.id_of), type_of=True)
            choice: str = input("Enter ID: ")
            main.get_student_by_group_id(int(choice))

        elif choice == "3":
            main.get_groups_by_teacher(str(user.id_of), type_of=True)
            choice: str = input("Enter ID: ")
            main.start_or_end_lesson(int(choice))

        elif choice == "4":
            print(success + "Exiting...")
            break


def after_login(user: User):
    print(f"{success}Welcome, {user.full_name}!")
    while True:
        print("Main/AfterLogin/")
        print(command + "1. Get My All Groups\n"
                        "2. Show My Balance\n"
                        "3. Edit My Information\n"
                        "4. LogOut")
        choice: str = input(enter + "Enter: ")
        if choice == "1":
            main.get_all_groups_by_student(user.id_of)

        elif choice == "2":
            main.get_balance(user.id_of)

        elif choice == "3":
            main.edit_student(str(user.id_of))

        elif choice == "4":
            print(success + "Exiting...")
            break


def run():
    while True:
        print("Main/")
        print(command + "1. Login\n"
                        "2. Exit")
        choice: str = input(enter + "Enter: ")

        if choice == "1":
            username: str = input(enter + "Enter Your Username: ")
            password: str = input(enter + "Enter Your Password: ")

            user: User = main.login(username=username, password=password)
            if user:
                if user.status == UserStatus.ADMIN.value:
                    after_login_adm(user)

                elif user.status == UserStatus.SUPER.value:
                    after_login_super(user)

                elif user.status == UserStatus.TEACHER.value:
                    after_login_teacher(user)

                elif user.status == UserStatus.STUDENT.value:
                    after_login(user)

        elif choice == "2":
            print(success + "Exiting...")
            break


if __name__ == '__main__':
    run()
