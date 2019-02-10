"""
conftest: pytestを拡張するためのファイル.

conftest を使用するには、いくつかルールがある.

～ルール～
1. pytest実行ファイル(calculation_test.py)と同じディレクトリに「conftest.py」ファイルを配置する.
2. pytest を実行する関数に request テクスチャを設置する.
"""


import os
import pytest


# parser.addoption(--'引数の名前(任意の名前)', default=(引数が渡されなかった時のデフォルト値), help=(引数の説明))
def pytest_addoption(parser):
    parser.addoption('--os-name', default='linux', help='os name')


# @pytest.fixtureとデコレータを付けると独自のfixtureを設定できる
@pytest.fixture
def csv_file(tmpdir):
    with open(os.path.join(tmpdir, 'test.csv'), 'w+') as f:
        print('before csv_file test')
        yield f
        print('after csv_file test')



