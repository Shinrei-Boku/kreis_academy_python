#kreis academy file操作

import csv

with open('./file/test.csv', 'w') as csv_file:
    fieldnames= ['NAME','AGE','SCORE']
    writer = csv.DictWriter(csv_file, fieldnames= fieldnames)
    writer.writeheader()
#     writer.writerow({'NAME':'kondo', 'AGE':'20', 'SCORE':'100'})
#     writer.writerow({'NAME': 'kobayashi', 'AGE': '30', 'SCORE': '80'})
#     writer.writerow({'SCORE': '70','NAME': 'sato', 'AGE': '35'})
#
# with open('test.csv','r') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         print(row['NAME'],row['AGE'],row['SCORE'])
