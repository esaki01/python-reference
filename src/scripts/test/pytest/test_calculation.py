"""
pytest: 実行コマンド -> pytest test_calculation.py --cov=calculation --cov-report term-missing
"""

import os

import pytest

from scripts.test.pytest import calculation

release_name = 'lesson'


class TestCal(object):

    @classmethod
    def setup_class(cls):
        print('TestCal - start')
        cls.cal = calculation.Cal()
        cls.file = 'test.txt'

    @classmethod
    def teardown_class(cls):
        print('TestCal - end')
        del cls.cal

    def setup_method(self, method):
        print('method={}'.format(method.__name__))
        # self.cal = calculation.Cal()

    def teardown_method(self, method):
        print('method={}'.format(method.__name__))
        # del self.cal

    def test_add_num_and_double(self):
        # cal = calculation.Cal()
        assert self.cal.add_num_and_double(1, 1) == 4

    # @pytest.mark.skip(reason='skip!')
    @pytest.mark.skipif(release_name == 'lesson', reason='test_add_num_and_double_raise is skipped!')
    def test_add_num_and_double_raise(self):
        with pytest.raises(ValueError):
            # cal = calculation.Cal()
            self.cal.add_num_and_double('1', '1')

    def test_save(self, tmpdir):
        self.cal.save(tmpdir, self.file)
        test_file_path = os.path.join(tmpdir, self.file)
        assert os.path.exists(test_file_path) is True

    # conftestのrequestテクスチャを試す
    def test_fixture_request(self, request):
        """
        --os-name=windows として実行時にオプションを指定できる.
        """
        os_name = request.config.getoption('--os-name')
        print('OS name is', os_name)

    # conftestの独自テクスチャを試す
    def test_fixture_csv_file(self, csv_file):
        print(csv_file)
