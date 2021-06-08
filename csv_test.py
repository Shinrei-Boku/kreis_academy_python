import csv

with open('./file/lesson.csv', encoding='utf-8-sig' ) as csv_file:
    read = csv.DictReader(csv_file)
    l = []
    for row in read:
        row['合計'] =  int(row['国語']) + int(row['数学']) + int(row['社会'])
        print( row['seq'], row['name'], row['合計'])
        l.append({'seq':row['seq'],'name':row['name'], '合計':row['合計']})

for i in l:
    print(list(i.values()))
    #print(type(list(i.values())))