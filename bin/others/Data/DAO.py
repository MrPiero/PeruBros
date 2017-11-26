import requests
import bin.constants as GC


def list_users():
    return requests.get(GC.URL).json()
