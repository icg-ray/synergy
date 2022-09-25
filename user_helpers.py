import json


def create_user(name, email, school):
    with open('users.json', 'r') as file:
        users = json.load(file)
        users.append({
            'name': name,
            'email': email,
            'school': school,
            'joined sessions': []
        })
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4, separators=(',',': '))
    print(f'created user {name}:\nemail: {email}\nschool: {school}')


def read_user(email):
    with open('users.json', 'r') as file:
        users = json.load(file)
        for u in users:
            if u['email'] == email:
                name = u['name']
                print(f'{name} has successfully logged in!')
                return u


def update_user(user, name, email, school, session):
    with open('users.json', 'r') as file:
        users = json.load(file)
        for u in users:
            if u == user:
                if name != "":
                    u['name'] = name
                if email != "":
                    u['email'] = email
                if school != "":
                    u['school'] = school
                if session != "":
                    u['joined sessions'].append(session)
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4, separators=(',',': '))
        print(f'successfully updated profile!')


def delete_user(user):
    with open('users.json', 'r') as file:
        users = json.load(file)
        for u in users:
            if u == user:
                users.remove(user)
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4, separators=(',',': '))
        print(f'deleted user')