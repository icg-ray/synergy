import json


def create_session(title, course, date, start_time, end_time, description, user):
    with open('sessions.json', 'r') as file:
        sessions = json.load(file)
        session = {
            "title": title,
            "course": course,
            "date": date,
            "time start": start_time,
            "time end": end_time,
            "description": description,
            "members": [user['name']]
        }
        sessions.append(session)
    with open('sessions.json', 'w') as file:
        json.dump(sessions, file, indent=4, separators=(',',': '))
    print(f'created session!')
    return session


def read_session(user):
    with open('users.json', 'r') as file:
        users = json.load(file)
        for u in users:
            if u == user:
                for session in u['joined sessions']:
                    print(session)


def update_session(title, course, date, start_time, end_time, description):
    with open('sessions.json', 'r') as file:
        sessions = json.load(file)
        for s in sessions:
            if s['title'] == title:
                if course != "":
                    s['course'] = course
                if date != "":
                    s['date'] = date
                if start_time != "":
                    s['time start'] = start_time
                if end_time != "":
                    s['time end'] = end_time
                if description != "":
                    s['description'] = description
    with open('sessions.json', 'w') as file:
        json.dump(sessions, file, indent=4, separators=(',',': '))
        print(f'successfully updated session!')


def delete_session(title, user):
    with open('sessions.json', 'r') as file:
        sessions = json.load(file)
        for s in sessions:
            if s['title'] == title:
                sessions.remove(s)
    with open('users.json', 'r') as file:
        users = json.load(file)
        for u in users:
            if u == user:
                for sesh in u['joined sessions']:
                    if sesh['title'] == title:
                        u['joined sessions'].remove(sesh)
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4, separators=(',',': '))
    with open('sessions.json', 'w') as file:
        json.dump(sessions, file, indent=4, separators=(',',': '))
        print(f'deleted session')
    
