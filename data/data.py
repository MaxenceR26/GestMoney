import json
import os


def add_user_in_activity_recent(user):
    with open(r'..\..\data\activity.json', 'r+') as file:
        data = json.load(file)
        if user not in data['activity_recent']:
            data['activity_recent'].insert(0, user)
        if len(data['activity_recent']) >= 4:
            x = data['activity_recent']
            x.remove(x[-1])

    with open(r'..\..\data\activity.json', 'w') as file:
        json.dump(data, file, indent=4)


def get_recent_user(number):
    with open(r'..\..\data\activity.json', 'r+') as file:
        data = json.load(file)

    return data['activity_recent'][number]


def get_users():
    with open(r'..\..\data\users.json', 'r') as f:
        return json.load(f)

def _return_money(user):
    with open(r'..\..\data\users.json', 'r+') as file:
        data = json.load(file)

    return data[user]['money']

def select_image_user(name):
    with open(r'..\..\data\users.json', 'r') as f:
        data = json.load(f)

    try:
        return data[name]['image']
    except KeyError as e:
        return "ressource\\img\\profile-base.png"