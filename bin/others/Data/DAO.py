import requests
import bin.constants as GC
import pymysql


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


# ejemplo al terminar 1-1 save_progress(id_char, (1,2))
# ejemplo al terminar 1-2 save_progress(id_char, (1,3))
# ejemplo al terminar 1-3 save_progress(id_char, (2,1))
def save_progress(id_char, progress):
    try:
        save = {'id_personaje': str(id_char), 'region': str(progress[0]), 'nivel': str(progress[1])}
        conn = pymysql.connect(host='tx6.fcomet.com', user='wecancom_soft', password='software2', db='wecancom_perubross')
        a = conn.cursor()
        sql = 'UPDATE progresos SET region=' + str(progress[0]) + ', nivel=' + str(progress[1]) + ' WHERE id_personaje=' + str(id_char)
        a.execute(sql)
        conn.commit()
        print(progress)
    except:
        pass

def save_score(id_char, score):
    try:
        save = {'id_personaje': str(id_char), 'score': str(score)}
        conn = pymysql.connect(host='tx6.fcomet.com', user='wecancom_soft', password='software2', db='wecancom_perubross')
        a = conn.cursor()
        sql = 'UPDATE personajes SET puntaje=' + str(score) + ' WHERE id=' + str(id_char)
        a.execute(sql)
        conn.commit()
        print(score)
    except:
        pass
