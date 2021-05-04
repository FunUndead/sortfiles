with open ('./sorted/1.txt', 'r', encoding='utf-8') as file_1:
    text_1 = file_1.readlines()

with open ('./sorted/2.txt', 'r', encoding='utf-8') as file_2:
    text_2 = file_2.readlines()

with open ('./sorted/3.txt', 'r', encoding='utf-8') as file_3:
    text_3 = file_3.readlines()


texts = [text_1, text_2, text_3]
texts.sort(reverse=True)

lines_1 = str(len(text_1))
text_1.insert(0, '\n')
text_1.insert(0, lines_1)
text_1.insert(0, '\n1.txt\n')

lines_2 = str(len(text_2))
text_2.insert(0, '\n')
text_2.insert(0, lines_2)
text_2.insert(0, '\n2.txt\n')

lines_3 = str(len(text_3))
text_3.insert(0, '\n')
text_3.insert(0, lines_3)
text_3.insert(0, '\n3.txt\n')

#print (texts)

with open ('./sorted/sorted.txt', 'w', encoding='utf-8' ) as f:
    for x in texts:
        f.writelines(x)

with open ('./sorted/sorted.txt', 'r', encoding='utf-8') as f:
    file_sort = f.read()

print(file_sort)
