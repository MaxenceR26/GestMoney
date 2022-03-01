import json


def add_user_in_activity_recent(user):
    with open(r'..\..\data\activity.json', 'r+') as file:
        data = json.load(file)
        data['activity_recent'].insert(0, user)
        if len(data['activity_recent']) >= 4:
            x = data['activity_recent']
            x.remove(x[-1])
        file.seek(0)
        json.dump(data, file, indent=4)


def get_recent_user(number):
    with open(r'..\..\data\activity.json', 'r+') as file:
        data = json.load(file)

    return data['activity_recent'][number]
