# Напишите программу, удаляющую из текста все слова, содержащие ""abc"".

with open('text.txt', 'r', encoding='utf-8') as file:
    text = str(file.read())                
    some_list = list(text.split())
    print(some_list)
with open('letters.txt', 'r', encoding='utf-8') as file:
    text1 = str(file.read())                
    letters = list(text1.split())
    print(letters)

for el in letters:
    new_list = list(filter(lambda word: el not in word, some_list))
    some_list = new_list.copy()
print(new_list)

# some_list = ['hello', 'world', 'hi', 'banana', 'orange', 'big', 'cup', 'horse']
# new_list = filter(lambda word: 'a' not in word, some_list)
# some_list = new_list
# new_list = filter(lambda word: 'b' not in word, some_list)
# some_list = new_list
# new_list = filter(lambda word: 'c' not in word, some_list)
# print(list(new_list))