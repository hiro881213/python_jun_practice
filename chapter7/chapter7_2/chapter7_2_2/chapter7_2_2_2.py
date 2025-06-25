# 7.2. ファイルの活用
# 7.2.2. CSVファイルを操作する
# 7.2.2.2. CSVファイルの読み込み
import csv

with open('test.csv', 'w') as csv_file:
    fieldnames = ['Name', 'Count']

    writer = csv.DictWriter(csv_file, fieldnames)
    writer.writeheader()

    writer.writerow({'Name': 'A', 'Count': '1'})
    writer.writerow({'Name': 'B', 'Count': '2'})

with open('test.csv', 'r') as csv_file:
    reader = csv.DictReader(csv_file)

    for row in reader:
        print(row['Name'], row['Count'])