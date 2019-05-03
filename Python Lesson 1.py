'''1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера
преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.
'''


a = 'разработка'
b = 'сокет'
c = 'декоратор'


print(type(a))
print(type(b))
print(type(c))

unicode_a = '%u0440%u0430%u0437%u0440%u0430%u0431%u043E%u0442%u043A%u0430%0A'
unicode_b = '%u0441%u043E%u043A%u0435%u0442%0A%0A'
unicode_c = '%u0434%u0435%u043A%u043E%u0440%u0430%u0442%u043E%u0440%0A%0A%0A'

print(type(unicode_a))
print(type(unicode_b))
print(type(unicode_c))

#Второй способ проверки:
if isinstance(a, str):
    print('True')

if isinstance(b, str):
    print('True')

if isinstance(c, str):
    print('True')

'''
2. Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
 (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
'''

word_1 = b'class'
word_2 = b'function'
word_3 = b'method'

print(len(word_1))
print(len(word_2))
print(len(word_3))

print(type(b))
print(type(a))
print(type(c))

'''
3. Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
'''
#нельзя в битовом режиме слова, написанные латиницей. utf-16
#import subprocess

#args = ['attribute', 'type', 'класс', 'функция']

#subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

#for line in subproc_ping.stdout:
#    print(line)

#for line in subproc_ping.stdout:
#    print(line.decode('utf-8'))

'''
4. Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
в байтовое и выполнить обратное преобразование (используя методы encode и decode).
'''
enc_str = 'разработка'

enc_str_bytes = enc_str.encode('utf-8')

print(enc_str_bytes)


dec_str_bytes = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'

dec_str = dec_str_bytes.decode('utf-8')

print(dec_str)

enc_str = 'администрирование'
enc_str_bytes = enc_str.encode('utf-8')

print(enc_str_bytes)

dec_str_bytes = b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'

dec_str = dec_str_bytes.decode('utf-8')

print(dec_str)

enc_str = 'protocol'
enc_str_bytes = enc_str.encode('utf-8')

print(enc_str_bytes)

dec_str_bytes = dec_str_bytes = b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'

dec_str = dec_str_bytes.decode('utf-8')

print(dec_str)


enc_str = 'standard'
enc_str_bytes = enc_str.encode('utf-8')

print(enc_str_bytes)


dec_str_bytes = dec_str_bytes = b'\x73\x74\x61\x6e\x64\x61\x72\x64'
dec_str = dec_str_bytes.decode('utf-8')

print(dec_str)

'''
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
PING yandex.ru (5.255.255.60): 56 data bytes
64 bytes from 5.255.255.60: icmp_seq=0 ttl=49 time=39.742 ms

'''



'''
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
«декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

'''

with open('test_file.txt', encoding='utf-8') as f_n:
    for el_str in f_n:
        print(el_str)

import locale

def_coding = locale.getpreferredencoding()

print(def_coding)


