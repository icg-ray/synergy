from tkinter import N


print('synergy\n\n')

action = input('(c)reate, (r)ead, (u)pdate, or (d)elete ')


def create_user(name, email, school):
    pass

def create_session(title, course, date, start_time, end_time, description):
    pass


if action == 'c':
    type = input('(u)ser/(s)ession')
    if type == 'u':
        name = input('name: ')
        email = input('email: ')
        school = input('school: ')
        create_user(name, email, school)
    elif type == 's':
        title = input('title: ')
        course = input('course: ')
        date = input('date: ')
        start_time = input('start time: ')
        end_time = input('end time: ')
        description = input('description: ')
        create_session(title, course, date, start_time, end_time, description)