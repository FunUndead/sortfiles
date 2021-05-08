def compile_files(files_list):
    data = {}

    for file in files_list:
        link = "./sorted/"
        file_l = link + file
        with open(file_l, encoding="utf-8") as f:
            file_data = f.readlines()

            data[(str(len(file_data)))] = [file, " ".join(file_data)]

    return data


file_list = ['1.txt', '2.txt', '3.txt'] #список файлов
data = compile_files(file_list)

keys = sorted(list(data.keys())) #сортировка по ключей

for key in data:                 #добавление количества строк в словарь
    data[key].insert(1, key)

#print(data)


with open ('./sorted/sorted.txt', 'w', encoding='utf-8') as f:
    for x in keys:
        data[x]
        for y in data[x]:
            f.write(y + '\n')

with open ('./sorted/sorted.txt', 'r', encoding='utf-8') as f:
     file_sort = f.read()

print(file_sort)