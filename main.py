from user_helpers import *
from session_helpers import *

print('synergy\n')

while True:
    action = input('(s)ign up/(l)og in ')

    if action == 's':
        name = input("name: ")
        email = input("email: ")
        school = input("school: ")
        create_user(name, email, school)
        continue

    elif action == 'l':
        email = input('email: ')
        user = read_user(email)
        while True:
            s_action = input('(u)pdate user/(c)reate session/(v)iew sessions/(d)elete user ')
            if s_action == 'u':
                new_name = input('name: ')
                new_email = input("email: ")
                new_school = input("school: ")
                update_user(user=user, name=new_name, email=new_email, school=new_school, session="")
            elif s_action == 'c':
                sesh_title = input('title: ')
                sesh_course = input('course: ')
                sesh_date = input('date: ')
                sesh_start_time = input('start time (hh:mm): ')
                sesh_end_time = input('end time (hh:mm): ')
                sesh_description = input('description: ')
                session = create_session(
                    sesh_title,
                    sesh_course,
                    sesh_date,
                    sesh_start_time,
                    sesh_end_time,
                    sesh_description,
                    user
                )
                update_user(user, "", "", "", session)
            elif s_action == 'v':
                read_session(user)
                sesh_action = input('(u)pdate session/(r)emove session/(b)ack ')
                if sesh_action == 'b':
                    continue
                elif sesh_action == 'u':
                    selected_sesh = input('enter session title: ')
                    course = input('course: ')
                    date = input('date: ')
                    start_time = input('start time (hh:mm): ')
                    end_time = input('end time (hh:mm): ')
                    description = input('description: ')
                    update_session(selected_sesh, course, date, start_time, end_time, description)
                elif sesh_action == 'r':
                    selected_sesh = input('enter session title: ')
                    delete_session(selected_sesh, user)
                    continue
            elif s_action == 'd':
                delete_user(user)
                break