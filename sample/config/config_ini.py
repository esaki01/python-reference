"""
コンフィグファイルの設定と参照（ini）.
"""

import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {
    'debug': True
}
config['web_server'] = {
    'host': '127.0.0.1',
    'post': 80
}
config['db_server'] = {
    'host': '127.0.0.1',
    'post': 3306
}

with open('config.ini', 'w') as config_file:
    config.write(config_file)

with open('config.ini', 'r') as config_file:
    data = config_file.read()
    print(data)
