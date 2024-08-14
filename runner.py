from colorama import Fore, init

from main import Main

from User.classes import UserGender, UserStatus, User, Group, Student

init(autoreset=True)

error = Fore.RED
enter = Fore.CYAN
re_enter = Fore.MAGENTA
success = Fore.LIGHTGREEN_EX
prints = Fore.YELLOW
command = Fore.LIGHTCYAN_EX

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
