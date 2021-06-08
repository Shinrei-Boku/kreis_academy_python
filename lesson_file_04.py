#kreis academy file操作

with open('./file/readwrite.txt', 'w+') as f:
    f.write("w+ テスト")
    #f.seek(0)
    print(f.read())

# with open('./file/readwrite2.txt', 'r+') as f:
#     s = f.read()
#     print(s)
#     f.seek(0)
#     f.write(s + "!! add")
