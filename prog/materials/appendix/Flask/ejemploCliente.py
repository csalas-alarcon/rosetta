import requests

URL = 'http://127.0.0.1:5000'
token = ''


def hello_world():
    r = requests.get(URL)
    print(r)
    print(r.status_code)
    print(r.text)


def create(id, value):
    global token
    r = requests.post(f'{URL}/data/{id}?value={value}', headers={'Authorization': 'Bearer ' + token})
    print(r.status_code)
    print(r.text)


def read(id):
    global token
    r = requests.get(f'{URL}/data/{id}', headers={'Authorization': 'Bearer ' + token})
    print(r.status_code)
    print(r.text)


def update(id, value):
    global token
    r = requests.put(f'{URL}/data/{id}?value={value}', headers={'Authorization': 'Bearer ' + token})
    print(r.status_code)
    print(r.text)


def delete(id):
    global token
    r = requests.delete(f'{URL}/data/{id}', headers={'Authorization': 'Bearer ' + token})
    print(r.status_code)
    print(r.text)


def singup(user, password):
    r = requests.post(f'{URL}/signup?user={user}&password={password}')
    print(r.status_code)
    print(r.text)


def signin(user, password):
    global token
    r = requests.get(f'{URL}/signin?user={user}&password={password}')
    print(r.status_code)
    print(r.text)
    token = r.text


def menu():
    while True:
        print("\n=== MENU ===")
        print("1. Hello World (Test Server)")
        print("2. Signup")
        print("3. Signin")
        print("4. Create Data")
        print("5. Read Data")
        print("6. Update Data")
        print("7. Delete Data")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            hello_world()
        elif choice == '2':
            user = input("Enter username: ")
            password = input("Enter password: ")
            singup(user, password)
        elif choice == '3':
            user = input("Enter username: ")
            password = input("Enter password: ")
            signin(user, password)
        elif choice == '4':
            id = input("Enter ID: ")
            value = input("Enter value: ")
            create(id, value)
        elif choice == '5':
            id = input("Enter ID: ")
            read(id)
        elif choice == '6':
            id = input("Enter ID: ")
            value = input("Enter new value: ")
            update(id, value)
        elif choice == '7':
            id = input("Enter ID: ")
            delete(id)
        elif choice == '8':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    menu()
