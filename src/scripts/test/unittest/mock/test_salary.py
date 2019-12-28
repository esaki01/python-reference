import unittest
from unittest import mock
from unittest.mock import MagicMock

from scripts.test.unittest.mock import salary


class TestSalary(unittest.TestCase):

    def test_calculate_salary(self):
        s = salary.Salary(year=2019)
        s.bonus_api.bonus_price = MagicMock(return_value=1)  # 仮の値を返してくれる
        self.assertEqual(s.calculate_salary(), 101)  # base + return_value=1で 101が返る

        s.bonus_api.bonus_price.assert_called()  # メソッドが呼ばれたことを確認
        s.bonus_api.bonus_price.assert_called_once()  # メソッドが一度呼ばれたことを確認
        s.bonus_api.bonus_price.assert_called_with(2019)  # メソッドが指定の引数で呼ばれたことを確認
        self.assertEqual(s.bonus_api.bonus_price.call_count, 1)  # メソッドが何回呼ばれたかを確認

    def test_calculate_salary_BonusApi_is_not_called(self):
        s = salary.Salary(year=2050)
        s.bonus_api.bonus_price = MagicMock(return_value=None)
        self.assertEqual(s.calculate_salary(), 100)  # base + bonus=0で 100が返る

        s.bonus_api.bonus_price.assert_not_called()  # BonusApiが呼ばれていないことを確認

    # MagicMockなしでデコレータで書ける
    @mock.patch('scripts.test.unittest.mock.salary.BonusApi.bonus_price')
    def test_calculate_salary_patch(self, mock_bonus_price):
        mock_bonus_price.return_value = 1  # 仮の値を返してくれる

        s = salary.Salary(year=2019)
        salary_price = s.calculate_salary()

        self.assertEqual(salary_price, 101)  # base + return_value=1で 101が返る
        mock_bonus_price.assert_called()  # メソッドが呼ばれたことを確認

    """
    デコレータなしでこのようにも書ける.
    def setUp(self):
        self.patcher = mock.patch('scripts.test.unittest.mock.salary.BonusApi.bonus_price')
        self.mock_bonus_price = self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_calculate_salary_patch(self):
        self.mock_bonus_price.return_value = 1

        s = salary.Salary(year=2019)
        salary_price = s.calculate_salary()

        self.assertEqual(salary_price, 101)
        self.mock_bonus_price.assert_called()
    """

    # 仮の値を固定値にせず条件を付けたい場合
    @mock.patch('scripts.test.unittest.mock.salary.BonusApi.bonus_price')
    def test_calculate_salary_side_effect(self, mock_bonus_price):
        mock_bonus_price.side_effect = lambda year: 1 if year < 2020 else 0  # side_effect=return_valueに条件式付けたもの

        s = salary.Salary(year=2019)
        salary_price = s.calculate_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus_price.assert_called()

    # 仮の値を例外にしたい場合
    @mock.patch('scripts.test.unittest.mock.salary.BonusApi.bonus_price')
    def test_calculate_salary_side_effect_exception(self, mock_bonus_price):
        mock_bonus_price.side_effect = ConnectionRefusedError  # side_effectには例外も指定できる

        s = salary.Salary(year=2019)
        salary_price = s.calculate_salary()

        self.assertEqual(salary_price, 100)
        mock_bonus_price.assert_called()

    # クラスごとMockする
    @mock.patch('scripts.test.unittest.mock.salary.BonusApi', spec=True)
    def test_calculate_salary_class(self, mock_bonus_api):
        mock_bonus_api = mock_bonus_api.return_value
        mock_bonus_api.bonus_price.return_value = 1

        s = salary.Salary(year=2019)
        salary_price = s.calculate_salary()

        self.assertEqual(salary_price, 101)
        mock_bonus_api.bonus_price.assert_called()
