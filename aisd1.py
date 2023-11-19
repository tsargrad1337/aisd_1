# Натуральные числа, в которых строго чередуются четные и нечетные цифры. Список используемых в числах четных цифр выводить отдельно прописью.

buffer_len = 1 # размер буфера чтения
work_buffer = "" # рабочий буфер                  
def number_to_words(n): # все цифры в шестнадцатиричной СС и их пропись
    f = {0 : 'ноль', 1 : 'один', 2 : 'два', 3 : 'три', 4 : 'четыре', 5 : 'пять',
    6 : 'шесть', 7 : 'семь', 8 : 'восемь', 9 : 'девять'}
    return f.get(n)
a = []
res = []
with open("text.txt") as file: # открываем файл
    buffer = file.read(buffer_len) # читаем первый блок
    if not buffer: # если файл пустой
        print("Файл пустой")
        exit()
    while buffer: # пока файл не пустой
        while buffer >= '0' and buffer <= '9': # обрабатываем текущий блок
            work_buffer += buffer                
            buffer = file.read(buffer_len) # читаем очередной блок
        if len(work_buffer) >= 2:
            if int(work_buffer[0])%2==0 and int(work_buffer[1])%2!=0: # ищем числа
                a.append(work_buffer)
        work_buffer = ""
        buffer = file.read(buffer_len) # читаем очередной блок
    print('Список чисел, подходящих под условие: ', a)
    for i in a:
        print(i)
        for j in i:
            if int(j) % 2 == 0:
                evenNumber = number_to_words(int(j)) # четные цифры выводим словами
                print(evenNumber + ' - четная цифра')

