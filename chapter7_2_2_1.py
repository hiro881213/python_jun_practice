# 7.2. ファイルの活用
# 7.2.2. CSVファイルを操作する
# 7.2.2.1. CSVファイルへの書き込み
import csv

with open('test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']
    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()