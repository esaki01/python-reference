"""
CSVファイルを読み書きする.
"""


import csv

# CSVファイルの書き込み
with open('test.csv', 'w', newline='') as f:
    field_names = ['Name', 'Count']
    writer = csv.DictWriter(f, fieldnames=field_names)
    writer.writeheader()
    writer.writerow({'Name': 'A', 'Count': 1})
    writer.writerow({'Name': 'B', 'Count': 2})

# CSVファイルの読み込み
with open('test.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Name'], row['Count'])
