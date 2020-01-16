"""
JSONファイルを読み書きする.
"""


import json

j = {
    "employee":
        [
            {"id": 111, "name": "Mike"},
            {"id": 222, "name": "Nancy"}
        ]
}


# 辞書型をJSON型に変換できる
a = json.dumps(j)
print(json.loads(a))

# JSONファイルの書き込み
with open('test.json', 'w') as f:
    json.dump(j, f)

# JSONファイルの読み込み
with open('test.json', 'r') as f:
    print(json.load(f))
