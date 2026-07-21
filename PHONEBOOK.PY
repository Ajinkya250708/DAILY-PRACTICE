import pickle


def add():
    file = open("phonebook.dat", 'ab')
    d = {}
    ans = "y"

    while ans.upper() == "Y":
        phone_num = int(input("PHONE NUMBER:"))
        name = input("NAME:")
        address = input("ADDRESS:")

        d['NUMBER'] = phone_num
        d['NAME'] = name
        d['ADDRESS'] = address

        pickle.dump(d, file)
        ans = input("DO YOU WANT TO ADD MORE CONTACTS:")
    file.close()


def remove():
    rem = input("PLEASE MENTION NAME OF THE CONTACT YOU WANT TO REMOVE:")
    file = open("phonebook.dat", 'rb')
    records = []
    found = False

    try:
        while True:
            d = pickle.load(file)
            if d['NAME'] == rem:
                found = True
            else:
                records.append(d)
    except EOFError:
        pass
    file.close()

    file = open("phonebook.dat", 'wb')
    for d in records:
        pickle.dump(d, file)
    file.close()

    if found:
        print("CONTACT REMOVED")
    else:
        print("THERE IS NO SUCH CONTACT IN YOUR PHONE BOOK")



def showall():
    file = open("phonebook.dat", 'rb')
    print("CONTACTS:")
    try:
        while True:
            d = pickle.load(file)
            print(d)
    except EOFError:
        file.close()


def find1():
    d = {}
    found = False
    file = open('phonebook.dat', 'rb')
    person = input("Enter Name:")

    try:
        while True:
            d = pickle.load(file)
            if d['NAME'] == person:
                print(d)
                found = True
    except EOFError:
        if found == False:
            print("THERE IS NO SUCH CONTACT IN YOUR PHONE BOOK")

    file.close()


def modify():
    found = False
    file = open('phonebook.dat', 'rb')
    mod = input("NAME OF THE CONTACT YOU WANT TO MODIFY:")
    print("1.NUMBER")
    print("2.NAME")
    print("3.ADDRESS")
    SELCT = input("WHAT DO YOU WANT TO MODIFY:")

    records = []
    try:
        while True:
            d = pickle.load(file)
            if d['NAME'] == mod and not found:
                if SELCT == "1":
                    d['NUMBER'] = int(input("ENTER NEW NUMBER:"))
                elif SELCT == "2":
                    d['NAME'] = input("ENTER NEW NAME:")
                elif SELCT == "3":
                    d['ADDRESS'] = input("ENTER NEW ADDRESS:")
                found = True
            records.append(d)
    except EOFError:
        pass
    file.close()

    file = open('phonebook.dat', 'wb')
    for d in records:
        pickle.dump(d, file)
    file.close()

    if found:
        print("CHANGES ARE MADE")
    else:
        print("THERE IS NO SUCH CONTACT IN YOUR PHONE BOOK")


print("-------PHONE BOOK--------\t")

answer = "Y"
while answer.upper() == "Y":
    print("\n")
    print("1.ADD A CONTACT")
    print("2.DELETE A CONTACT")
    print("3.EDIT A CONTACT")
    print("4.FIND A CONTACT")
    print("5.SHOW ALL CONTACTS")
    print("6.EXIT")
    print("\n")
    choose = input("WHAT DO YOU WANT TO DO:")

    if choose == "1":
        add()
    elif choose == "2":
        remove()
    elif choose == "3":
        modify()
    elif choose == "4":
        find1()
    elif choose == "5":
        showall()
    elif choose == "6":
        print("THANK YOU FOR USING PHONE BOOK")
        break
    else:
        print("INVALID CHOICE, TRY AGAIN")

    answer = input("WANT TO DO ANYTHING ELSE(Y/N):")