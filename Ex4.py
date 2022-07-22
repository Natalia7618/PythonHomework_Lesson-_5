# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

text = 'fffhhhhhhhhhhaaaaaaaaaaaarrrrrrrrrrruuuuuuuuuuuufffffffffff'
data = open ('file4.txt', 'a', encoding ='utf-8')
data.writelines(text)
print(text)

def rle_algorithm(text): 
    res = '' 
    prev_char = '' 
    count = 1
    if not text: return ''
    for char in text:
        if char != prev_char:
            if prev_char: 
                res += str(count) + prev_char 
            count = 1 
            prev_char = char
        else: 
            count += 1
    else: 
        res += str(count) + prev_char 
        return res

new_text = rle_algorithm(text)
data = open ('file4.txt', 'a', encoding ='utf-8')
data.write("\n")
data.write(new_text)
print(new_text)

