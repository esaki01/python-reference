import requests


class BonusApi(object):
    """Mock確認用に仮のAPIを実装."""
    @staticmethod
    def bonus_price(year):
        r = requests.get('http://localhost/bonus', params={'year': year})
        return r.json()['price']


class Salary(object):

    def __init__(self, base=100, year=2019):
        self.bonus_api = BonusApi()
        self.base = base
        self.year = year

    def calculate_salary(self):
        bonus = 0
        if self.year < 2020:
            try:
                bonus = self.bonus_api.bonus_price(self.year)
            except ConnectionRefusedError:
                bonus = 0
        return self.base + bonus
