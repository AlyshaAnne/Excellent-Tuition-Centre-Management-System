import os
#Creating the file within the program automatically
def file_creation():
    files = ['tutors.txt', 'receptionist.txt', 'monthly income report.txt','payments.txt']
    for file in files:
        if not os.path.exists(file):
            with open(file, 'w') as f:
                pass


logged_in_user = None
login_attempts = 0

def loadUsers():
    users = {}
    with open("admin.txt", "r") as file:
        for line in file:
            name, password, mail, number, birthday = line.strip().split(",")
            users[name] = {"password": password, "mail": mail, "number": number, "birthday": birthday}
    return users
#Prompt user to insert login details
def login():
    global logged_in_user, login_attempts
    if login_attempts < 3:
        username = input("Enter username/email: ")
        password = input("Enter password: ")
        if authenticate(username, password):
            print(f"Welcome, {logged_in_user}!")
            print("━"*24)
            return True
        else:
            print("Invalid username/email or password. Please try again.")
            login_attempts += 1
            return login()
    else:
        print("Maximum login attempts reached. Exiting.")
        return False

def authenticate(username, password):
    global logged_in_user
    users = loadUsers()
    if username.lower() in users and users[username]["password"] == password:
        logged_in_user = username.lower()
        return True
    return False
#Show admin menu
def admin_menu():
    while True:
        print("Admin Menu".center(24))
        print("━"*24)
        print("1) Register tutors")
        print("2) Delete tutors")
        print("3) View tutors")
        print("4) Assign tutors to respective levels and subjects")
        print("5) Register receptionist/s")
        print("6) Delete receptionist/s")
        print("7) View Receptionist ")
        print("8) View monthly income report")
        print("9) Update own profile")
        print("10)Login Page")
        admin_menu_choice = input("Please choose one of the following by typing the number: ")

        if admin_menu_choice == "1":
            registerTutors()
        elif admin_menu_choice == "2":
            deleteTutors()
        elif admin_menu_choice == "3":
            viewTutors()
        elif admin_menu_choice == "4":
            assignTutors()
        elif admin_menu_choice == "5":
            registerReceptionist()
        elif admin_menu_choice == "6":
            deleteReceptionist()
        elif admin_menu_choice == "7":
            viewReceptionist()
        elif admin_menu_choice == "8":
            viewmontlyincomereport()
        elif admin_menu_choice == "9":
            updateownprofile()
        elif admin_menu_choice == "10":
            loginpage()
        else:
            print("Invalid input, please try again. ")
        # print(admin_menu_choice)
        # Implement admin functionalities here

#Register Tutor Option
def registerTutors():
    name = input("Enter name: ")
    mail = input("Enter mail: ")
    number = input("Enter number: ")
    subject1 = input("Enter first subject:")
    subject2 = input("Enter second subject:")
    subject3 = input("Enter third subject:")
    level = input ("Enter level:")
    with open ("tutors.txt", "a") as file:
        file.write(f"{name},{mail},{number},{subject1},{subject2},{subject3},{level}\n")
    choice = input("Repeat Program?(N to terminate, Y to repeat): ")
    if choice != "N":
        return
    else:
        exit()

def loadTutors():
    tutors = {}
    with open("tutors.txt", "r") as file:
        for line in file:
            name, mail, number, subject1,subject2,subject3, level = line.strip().split(",")
            tutors[name] = {"mail": mail, "number": number,"subject1":subject1,"subject2":subject2,"subject3":subject3,"level":level}
    return tutors


def savingData(file_name, data):
    with open(file_name, "w") as file:
        for key, value in data.items():
            file.write(f"{key},{value['mail']},{value['number']}\n")
#Delete Tutor Option
def deleteTutors():
    name = input("Enter tutor name to delete: ")
    tutors = loadTutors()

    if name not in tutors:
        print("Tutor not found.")
        return

    del tutors[name]
    savingData("tutors.txt", tutors)

    print("Tutor deleted successfully.")
#View Tutor Option
def viewTutors():
    with open("tutors.txt", "r") as file:
        for line in file:
            name, mail, number,subject1,subject2,subject3,level = line.strip().split(",")
            print(f"{name}|{mail}|{number}|{subject1}|{subject2}|{subject3}|{level}")

#Reassign Tutor Subject and Level (max 3)
def assignTutors():
    tutors = loadTutors()
    name = input("Enter tutor's name to reassign subject and level:")
    subject1 = input("Pick a subject:(options are math, chemistry, biology, physics,computer)")
    subject2 = input("Pick a subject:(options are math, chemistry, biology, physics,computer)")
    subject3 = input("Pick a subject:(options are math, chemistry, biology, physics,computer)")
    if subject1 :
        tutors[name] ["subject1"] = subject1
    if subject2:
        tutors[name]["subject2"] = subject2
    if subject3 :
        tutors[name] ["subject3"] = subject3

    level = input("Input new level:")
    if level :
        tutors[name] ["level"] = level
    savingTutors("tutors.txt",tutors)



def savingTutors(file_name, data):
    with open(file_name, "w") as file:
        for key, value in data.items():
            file.write(f"{key},{value['mail']},{value['number']},{value['subject1']},{value['subject2']},{value['subject3']},{value['level']}\n")

#View Monthly Income Report
def viewmontlyincomereport():
    with open("payments.txt","r") as file:
        for line in file:
            studentname,studentpassport,totalpayment,paymentpaid,paymentremaining = line.strip().split(",")
            print(f"{studentname}|{studentpassport}|{totalpayment}|{paymentpaid}|{paymentremaining}")

def savemonthlyincomereport(file_name, data):
    with open(file_name,"w") as file:
        for key, value in data.items():
            file.write(f"{key}, {value ['mail']},{value['number']}\n")

def saveProfile(file_name, data):
    with open(file_name, "w") as file:
        for key, value in data.items():
            file.write(f"{key},{value['password']},{value['mail']},{value['number']},{value['birthday']}\n")
#Update Own Profile
def updateownprofile():
    username = logged_in_user
    users = loadUsers()

    password = input("Enter new password: ")
    mail = input("Enter new mail: ")
    number = input("Enter new mobile number: ")
    birthday = input("Enter new birthday: ")
    
    if password: 
        users[username]["password"] = password
    if mail: 
        users[username]["mail"] = mail
    if number: 
        users[username]["number"] = number
    if birthday: 
        users[username]["birthday"] = birthday

    saveProfile("admin.txt", users)
#register receptionist
def registerReceptionist():
    name = input("Enter name: ")
    mail = input("Enter mail: ")
    number = input("Enter number: ")
    with open ("receptionist.txt", "a") as file:
        file.write(f"{name},{mail},{number}\n")
    choice = input("Repeat Program?(N to terminate, Y to repeat): ")
    if choice != "N":
        return
    else:
        exit()

def loadReceptionist():
    receptionist = {}
    with open("receptionist.txt", "r") as file:
        for line in file:
            name, mail, number = line.strip().split(",")
            receptionist[name] = {"mail": mail, "number": number}
    return receptionist
#view receptionist
def viewReceptionist():
    with open ("receptionist.txt", "r") as file:
        for line in file:
            name, mail, number = line.strip().split(",")
            print(f"{name}|{mail}|{number}")
#Delete Receptionist
def deleteReceptionist():
    name = input("Enter receptionist name to delete: ")
    receptionist = loadReceptionist()

    if name not in receptionist:
        print("Receptionist not found.")
        return

    del receptionist[name]
    savingData("receptionist.txt", receptionist)

    print("Receptionist deleted successfully.")
#Return to login page
def loginpage():
    global admin
    admin = None
    print("You have been successfully logged out.")
    login()

def receptionist_menu():
    print("    Recept. Menu    ")
    print("━━━━━━━━━━━━━━━━━━━━")
    print("1) Register a student")
    print("2) Update subject enrollment (if students request to change subject).")
    print("3) Accept payment from students and generate receipts.")
    print("4) Delete students who have completed their studies.")
    print("5)  Update own profile")
    receptionist_menu_choice = input("Please choose one of the following by typing the number: ")
    print(receptionist_menu_choice)
    # Implement receptionist functionalities here

def tutor_menu():
    print("     Tutor Menu     ")
    print("━━━━━━━━━━━━━━━━━━━━")
    print("1) Add class information")
    print("2) Update and delete class information")
    print("3) View the list of students enrolled in his/her subjects")
    print("4) Update own profile")
    tutor_menu_choice = input("Please choose one of the following by typing the number: ")
    print(tutor_menu_choice)
    # Implement tutor functionalities here

def student_menu():
    print("    Student Menu    ")
    print("━━━━━━━━━━━━━━━━━━━━")
    print("1) View the schedule")
    print("2) Send a request to the receptionist to change the enrolled subject.")
    print("3) Delete the request sent to the receptionist to change the subject(IF PENDING).")
    print("4) View student debt to be paid.")
    print("5) Update own profile.")
    student_menu_choice = input("Please choose one of the following by typing the number: ")
    print(student_menu_choice)
    # Implement student functionalities here

# def main():
#     global logged_in_user
#     logged_in_user = login()
#     if logged_in_user == 'admin':
#         admin_menu()
#     elif logged_in_user == 'receptionist':
#         receptionist_menu()
#     elif logged_in_user == 'tutor':
#         tutor_menu()
#     elif logged_in_user == 'student':
#         student_menu()

# logged_in_user = login()
file_creation()
if login():
    if logged_in_user == 'admin':
        admin_menu()
    elif logged_in_user == 'receptionist':
        receptionist_menu()
    elif logged_in_user == 'tutor':
        tutor_menu()
    elif logged_in_user == 'student':
        student_menu()