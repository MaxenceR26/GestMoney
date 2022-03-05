import json


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


def get_all_users():
    with open(r'..\..\data\users.json', 'r') as f:
        return json.load(f)


def dump_users(users):
    with open(r'..\..\data\users.json', 'w') as file:
        json.dump(users, file, indent=4)


def get_user(user_id):
    users = get_all_users()
    return users[user_id]


def set_user(user_id, old_id, new_user):
    users = get_all_users()
    del users[old_id]
    users[user_id] = new_user
    dump_users(users)


def update_user_id(old_id, new_id):
    with open(r'..\..\data\activity.json', 'r+') as file:
        data = json.load(file)
        data['activity_recent'][data['activity_recent'].index(old_id)] = new_id

    with open(r'..\..\data\activity.json', 'w') as file:
        json.dump(data, file, indent=4)


def _return_money(user):
    users = get_all_users()
    return users[user]['money']


def select_image_user(name):
    with open(r'..\..\data\users.json', 'r') as f:
        data = json.load(f)

    try:
        return data[name]['image']
    except KeyError:
        return "ressource\\img\\profile-base.png"


def change_money(user_id, amount: int):
    users = get_all_users()
    users[user_id]['money'] += amount
    dump_users(users)


def add_transaction(user_id, transaction):
    with open(r'..\..\data\transactions.json', 'r') as f:
        data = json.load(f)

    if data.get(user_id) is None:
        data[user_id] = []

    data[user_id].append(transaction)

    change_money(user_id, transaction['amount'])

    with open(r'..\..\data\transactions.json', 'w') as f:
        json.dump(data, f, indent=4)