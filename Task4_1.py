# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# МОДУЛЬ СЖАТИЯ ДАННЫХ

with open('rle_input.txt', 'r', encoding='utf-8') as file:
    text = str(file.read())                
    print(f'{text} ({len(text)} symbols)')
text = text + '.'
count = 1
ind = 0
s = ''    
while ind < len(text) - 1:
    if text[ind] == text[ind + 1]:
        count += 1
    else:
        s = s + str(count) + text[ind]
        count = 1
    ind += 1
print(f'{s} ({len(s)} symbols)')
with open('rle_output.txt', 'w', encoding='utf-8') as data:
    data.writelines(s)
