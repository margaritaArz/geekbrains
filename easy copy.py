# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.


import os

path_name = 'dir_'

def makeDir(path_name):
        os.mkdir(path_name)
        print('Уже существует')

print(makeDir(path_name))

def deleteDir(path_name):
    os.rmdir(path_name)
    print('Уже удален')

print(deleteDir(path_name))

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def folder():
    main_path = os.getcwd()
    list = os.listdir()
    for i in list:
        print('Папки в текущей директории:', i)

print(folder())

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный крипт.



import shutil

def makeCopy():
    shutil.copy('easy.py', 'easy_1.py', follow_symlinks=True)

print(makeCopy())