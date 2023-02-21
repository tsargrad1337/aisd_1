#Натуральные числа, в которых строго чередуются четные и нечетные цифры. Список используемых в числах четных цифр выводить отдельно прописью.
buffer_len = 1
Int = {'0':'ноль', '1':'один', '2':'два', '3':'три', '4':'четыре', '5':'пять', '6':'шесть' ,'7':'семь', '8':'восемь', '9':'девять'}
number = ""
check = False
try:
    with open('text.txt', 'r') as f:
        buffer = f.read(buffer_len)
        if not buffer:
            print('Выбранный файл пустой.')
        while buffer:
            for k in Int.keys():
                if buffer == k:
                    first = True
                    check = False
                    if first == True:
                        if int(buffer)%2==0 and int(buffer)!=0:
                            check = True
                            x = Int[buffer]
                        first == False
                    if check == False and first == False:
                        break
                    elif check == True and first == False:
                        if int(buffer)%2!=0:
                            x = Int(buffer)
                        else:
                            check = False
                            break
                    if check == True:
                        print(x)
                    else:
                        break
            if buffer == ' ':
                print(' ')    
            buffer = f.read(buffer_len)
except FileNotFoundError:
    print('Выбранный файл не обнаружен в заданной директории')

                
                
            
                
                    
                    
                    
                        
                        
            
                
                
                
            
    
            
            

