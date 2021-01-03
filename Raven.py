import os
import time
import requests
import html2text
import termcolor
from termcolor import colored
from time import sleep, strftime
from glob import glob
color_red='\033[31m'
#-1-modul
os.system('clear')
mb='1.69 мб'
progs=('\n\033[32m\n   сканер сайтов- - -\033[31mscan yzel\033[32m.\n   сканер портов- - -\033[31mscan port\033[32m.\n   сканер ip- - - - - -\033[31mscan ip\033[32m.\n   сканер номера- - -\033[31mscan tp\033[32m.')
ver='1.6'
def code_200():
    try:
        requests.get("https://google.com", timeout=4)
        print('\033[32mподключенно к сети')
    except:
        print('\033[31mне подключенно к сети')
code_200()
print('''
\033[32mдоступ к системе voron открыт.
\033[35mверсия 1.6
\033[32m
''')
print('\033[32m-v-o-r-o-n-\n')
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
#-2-start_comands
def a_1():
#-3-start_progs-a_1
    def enter():
#-4-start_enter
        enter=input('--'+strftime('\033[31m%H:%M')+'\n\033[32mdark@root- ')
        if enter=='help' or enter=='h' or enter=='-h' or enter=='помощь' or enter=='помоги' or enter=='хелп' or enter=='he' or enter=='hr' or enter=='Help' or enter=='H' or enter=='-H' or enter=='Помощь' or enter=='Помоги' or enter=='Хелп' or enter=='He' or enter=='Hr':
            print('''доступные команды:
autors      - авторы программы voron.
-----------
ost         - основные команды системы.
-----------
voron       - полный доступ к системе.
ytil        - документация системы.
v-v         - обновления voron.
''')
        elif enter=='port_scan' or enter=='сканер портов' or enter=='port' or enter=='Port_scan' or enter=='Сканер портов' or enter=='Port' or enter=='scan port':
            try:
                internal_search_cat('scan_port.py')
            except:
                print(error)
        elif enter=='autors' or enter=='Autors':
            a=('T', 'To', 'Top', 'Topo', 'Topo1', 'Topo1u', 'Topo1us', 'Topo1us-', 'Topo1us- -')
            b=0
            while True:
                print(colored(a[b % len(a)], 'red'), sep='', end='\r')
                sleep(0.1)
                b+=1
                if b>9:
                    print('')
                    break
        elif enter=='ost' or enter=='Ost':
            print('''
o         - очистка экрана.
progs - показ установленых программ в Voron.
mb        - вес системы voron.''')  
        elif enter=='o' or enter=='O':
            os.system('clear')
        elif enter=='voron' or enter=='Voron':
            x=input('код доступа: ')
            print('\033[31mотказано в доступе.')
            print('\033[32m:).')
            print('за кодом доступа Вы можете обратиться к автору.\nтак как автор любит комедии, Вы должны пройти испытание.')
            time.sleep(5)
            os.system('clear')
            print('пасхалка.\nищите записи с кодовым словом \033[31mTopo1us\033[32m.')
        elif enter=='block_111' or enter=='progs' or enter=='Progs':
            print(progs)
        elif enter=='voron-inf' or enter=='voron-info' or enter=='inf' or enter=='info' or enter=='информация' or enter=='Ytil' or enter=='ytil':
            print('обновление voron будут релизоваться по выходным дням.\nверсия '+str(ver)+' содержит:'+str(progs))
        elif enter=='scan site' or enter=='yzel' or enter=='узел' or enter=='сканер сайта' or enter=='scan yzel':
            def re():
                f=input('ссылка: ')
                s=requests.get(f)
                print(s.text)
            def rer():
                f=input('ссылка: ')
                s=requests.get(f)
                d=html2text.HTML2Text().handle(s.text)
                print(d)
            try:
                cer=input('[1] код страницы.\n[2] текст страницы.\n\n~  ')
                if cer=='1':
                    re()
                elif cer=='2':
                    rer()
            except:
                print(color_red+'неправильная ссылка.')
        elif enter=='v-v':
            print('''
1.1 август 2020 год.
1.2 ноябрь 2020 год.
1.3 ноябрь 2020 год.
1.4 декабрь 2020 год.
1.5 декабрь 2020 год.
1.6 декабрь 2020 год.
''')
        elif enter=='mb' or enter=='Mb':
            print('вес системы voron составляет '+str(mb))
        elif enter=='scan ip' or enter=='Scan ip' or enter=='Ip' or enter=='ip':
            f=input('IP: ')
            f=('https://ipinfo.io/'+f+'/json')
            s=requests.get(f)
            s=s.text
            s=s.replace('"','')
            s=s.replace(' ','')
            s=s.replace('{','')
            s=s.replace('}','')
            s=s.replace(',','')
            s=s.replace(':',': ')
            s=s.replace('hostname: cloud.revoluz.io','-----')
            s=s.replace('city','город')
            s=s.replace('region','регион')
            s=s.replace('country','страна')
            s=s.replace('loc','геолокация')
            s=s.replace('readme: https: //ipinfo.io/missingauth','-----')
            s=s.replace('org: AS55688PT.BeonIntermedia','')
            s=s.replace('timezone','континент')
            print(s)
        elif enter=='scan tp' or enter=='Scan tp':
            import urllib.request
            import json
            print('пример::7 900 777 11 22\n')
            phone=input('номер: ')
            getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone
            infoPhone = urllib.request.urlopen( getInfo )
            infoPhone = json.load( infoPhone )
            print( u"Номер      --->", "+" + phone )
            print( u"Страна     ---> ", infoPhone["country"]["name"] )
            print( u"Регион     ---> ", infoPhone["region"]["name"] )
            print( u"Округ      ---> ", infoPhone["region"]["okrug"] )
            print( u"Оператор   ---> ", infoPhone["0"]["oper"] )
            print( u"Континент  ---> ", infoPhone["country"]["location"] )
        else:
            os.system(enter)
            print('\033[32m--внутрение команды os--')
#-5-inkor---
    while True:
        enter()
try:
    a_1()
except:
    print('ошибка 101.\nобратитесь к создателю.')
    renable=input('перезапустить voron?\n: ')
    renable=renable.lower()
   if renable=='y' or renable=='yes' or renable=='д' or renable=='да' or renable=='Y' or renable=='Yes' or renable=='Д' or renable=='Да':
        print('voron успешно перезагружен.')
        a_1()
   elif renable=='n' or renable=='no' or renable=='н' or renable=='нет' or renable=='N' or renable=='No' or renable=='Н' or renable=='Нет':
        print('voron закрыт.')
