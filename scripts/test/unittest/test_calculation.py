"""
unittest: method名は、test～ にすることに注意.
"""

import unittest

from scripts.test.unittest import calculation

release_name = 'lesson'


class TestCal(unittest.TestCase):

    def setUp(self):
        print('Set up test execution')
        self.cal = calculation.Cal()

    def tearDown(self):
        print('Tear down test execution')

    # @unittest.skip('skip!')
    @unittest.skipIf(release_name == 'lesson', 'add_num_and_double is skipped!')
    def test_add_num_and_double(self):
        # cal = calculation.Cal()
        self.assertEqual(self.cal.add_num_and_double(1, 1), 4)

    def test_add_num_and_double_raise(self):
        # cal = calculation.Cal()
        with self.assertRaises(ValueError):
            self.cal.add_num_and_double('1', '1')


if __name__ == '__main__':
    unittest.main()
