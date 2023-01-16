# # МОДУЛЬ ВОССТАНОВЛЕИЯ ДАННЫХ (обратное преобразование)

with open('rle_input1.txt', 'r', encoding='utf-8') as file:
    s = str(file.read())                
    print(f'{s} ({len(s)} symbols)')

i = 0
s_rle = ''
while i < len(s):
    s_int = ''
    a = s[i]
    while '0' <= a <= '9':
        s_int += a
        i += 1
        if i < len(s):
            a = s[i]
        else:
            break
    i += 1
    if s_int != '':
        s_rle = s_rle + int(s_int)*s[i-1]
print(f'{s_rle} ({len(s_rle)} symbols)')
with open('rle_output1.txt', 'w', encoding='utf-8') as data:
    data.writelines(s_rle)




# text = text + '.'
# count = 1
# ind = 0
# s = ''    
# while ind < len(text) - 1:
#     if text[ind] == text[ind + 1]:
#         count += 1
#     else:
#         s = s + str(count) + text[ind]
#         count = 1
#     ind += 1
# print(f'{s} ({len(s)} symbols)')
# with open('rle_output1.txt', 'w', encoding='utf-8') as data:
#     data.writelines(s)