#raven
import os,socket,time,requests,html2text,termcolor,glob
from termcolor import colored
from time import sleep, strftime
from glob import glob
#modul's
color_red='\033[31m'
color_green='\033[32m'
#error
error=(color_red+'ошибка доступа.')
#color_m
scan_folder=('cd /data/data/com.termux/files/home/Raven/scan')
def internal_search_cat(internal_search_def):
    try:
        work_file_is_finish=glob(internal_search_def)[0]
        os.system('cat '+work_file_is_finish+'\n')
    except:
        print('Raven не удалось найти файл: ',internal_search_cat)
def internal_search_py(internal_search_def):
    try:
        work_file_is_finish=glob(internal_search_def)[0]
        os.system('python '+work_file_is_finish)
    except:
        print('Raven не удалось найти файл: ',internal_search_py)
def net():
    try:
        os.system('clear')
        requests.get("https://pornhub.com", timeout=4)
        print(color_green+'подключенно к сети')
    except:
        print(color_red+'не подключенно к сети')
    print('''
\033[32mдоступ к системе Raven открыт.
\033[35mверсия 1.7
\033[32m
''')
def v_1():
    def bug_enter(bg_enter):
#-H-E-L-P-
        if bg_enter=='help' or bg_enter=='h' or bg_enter=='помощь':
            try:
                internal_search_cat('Raven_help.txt')
            except:
                print(error)
        else:
            os.system(bg_enter)
            print('Внутренние команды.')
    def enter():
        bug_enter(input('--'+strftime('\033[31m%H:%M')+'\n\033[32mdark@root- '))
    while True:
        enter()
net()
v_1()
