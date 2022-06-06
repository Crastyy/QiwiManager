# Запросы Qiwi (Qiwi requests)
import requests

class QiwiReq():
    def __init__(self):
        self.reqs = requests.Session()

    def get_balance(self, numebr, token):
        pass