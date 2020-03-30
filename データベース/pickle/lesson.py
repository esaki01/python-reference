"""
Python のデータ型をそのまま保持できる.
"""

import pickle

data = {"a": "a"}

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

with open('data.pickle', 'rb') as f:
    loaded = pickle.load(f)
    print(loaded)
