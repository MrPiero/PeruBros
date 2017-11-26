import requests
import bin.constants as GC


def list_users():
    return requests.get(GC.URL).json()


def get_user(id_user):
    users = list_users()
    for u in users:
        if u["id"] == id_user:
            return u


def get_saves(id_user):
    return requests.get(GC.URL_SAVES_USER + str(id_user)).json()


def get_progress(id_char):
    return requests.get(GC.URL_PROGRESS_SAVE + str(id_char)).json()


def save_progress(id_char, progress):
    save = {'id_personaje': str(id_char), 'region': str(progress[0]), 'nivel': str(progress[1])}
    r = requests.post(GC.URL_SAVE_PROGRESS_CHAR, json=save)
    print(r)