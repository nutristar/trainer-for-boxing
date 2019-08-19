import datetime
import sys
sys.path.insert(0, "F:/lessons_pro/Sara/saravoice")
#import saravoice
import urllib.request
from bs4 import BeautifulSoup

def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()

def parse (html):
    soup = BeautifulSoup(html)
    table = soup.find("table", class_="auctions w100")
    rows = table.find_all("td")
    #print(rows)
    projects = []
    c=1
    for row in rows:#table.find_all("td"):

        if c==1:
            projects.append({
            "PRODUCT":row.text})
            c=c+1

        elif c==2:
             projects.append({
            "COMPANY":row.text})
             c=c+1
        elif c==3:
             c=c+1
        elif c==4:
             c=c+1
        elif c==5:
             c=c+1

        elif c==6:
             projects.append({
            "DEAD LINE":row.text})
             c=c-5


    #print(c)

    projects=str(projects)
    #print(projects)
    projects = projects.replace('t', '')
    projects = projects.replace('n', '')
    projects = projects.replace('r', '')
    f = open('text.txt', 'w')
    f.write(projects)
    print(projects)

def main():
    parse(get_html("http://www.icetrade.by/search/auctions?search_text=%D0%B7%D0%B0%D0%BA%D0%B2%D0%B0%D1%81%D0%BA%D0%B8&zakup_type%5B1%5D=1&zakup_type%5B2%5D=1&auc_num=&okrb=&company_title=&establishment=0&industries=&period=&created_from=&created_to=&request_end_from=&request_end_to=&t%5BTrade%5D=1&t%5BeTrade%5D=1&t%5BsocialOrder%5D=1&t%5BsingleSource%5D=1&t%5BAuction%5D=1&t%5BRequest%5D=1&t%5BcontractingTrades%5D=1&t%5Bnegotiations%5D=1&t%5BOther%5D=1&r%5B1%5D=1&r%5B2%5D=2&r%5B7%5D=7&r%5B3%5D=3&r%5B4%5D=4&r%5B6%5D=6&r%5B5%5D=5&sort=num%3Adesc&sbm=1&onPage=20"))

if __name__ == '__main__':
    main()




"""a=(datetime.datetime.today())
#print (a)

b = a.strftime("%Y-%m-%d--%H.%M")
print(b)
hour_now=b[12:14]
minut_now=b[15:17]

#print(hour_now)
#print(minut_now)

if minut_now == "30" and hour_now=="8":
    cc ="читать какие  тендера"
elif minut_now == "00" and hour_now=="11":
    cc ="читать какие  тендера"
elif minut_now == "00" and hour_now=="15":
    cc="читать какие тендера"
elif minut_now == "00" and hour_now=="17":
    cc ="читать какие  тендера"
    """

def saravoice():
    # Чтение вслух
    import os
    import regex as re
    from pygame import mixer
    import DateTime
    import time
    from gtts import gTTS

    # Для того чтобы не возникало коллизий при удалении mp3 файлов
    # заведем переменную mp3_nameold в которой будем хранить имя предыдущего mp3 файла
    mp3_nameold='111'
    mp3_name = "1.mp3"

    # Инициализируем звуковое устройство
    mixer.init()

    # Открываем файл с текстом и по очереди читаем с него строки в ss
    f = open("text.txt","r")
    ss = f.readline()
    while ss:
        # Делим прочитанные строки на отдельные предложения
        split_regex = re.compile(r'[!|?|…]')
        sentences = filter(lambda t: t, [t.strip() for t in split_regex.split(ss)])

        # Перебираем массив с предложениями
        for x in sentences:
            if(x!=""):
                print(x)
                # Эта строка отправляет предложение которое нужно озвучить гуглу
                tts=gTTS(text=x, lang='ru')
                # Получаем от гугла озвученное предложение в виде mp3 файла
                tts.save(mp3_name)
                # Проигрываем полученный mp3 файл
                mixer.music.load(mp3_name)
                mixer.music.play()
                while mixer.music.get_busy():
                    time.sleep(0.1)
                # Если предыдущий mp3 файл существует удаляем его
                # чтобы не захламлять папку с приложением кучей mp3 файлов
                if(os.path.exists(mp3_nameold) and (mp3_nameold!="1.mp3")):
                    os.remove(mp3_nameold)
                mp3_nameold=mp3_name
                # Формируем имя mp3 файла куда будет сохраняться озвученный текст текущего предложения
                # В качестве имени файла используем текущие дату и время
                now_time = DateTime.DateTime.now()
                mp3_name = now_time.strftime("%d%m%Y%I%M%S")+".mp3"

        # Читаем следующую порцию текста из файла
        ss = f.readline()

    # Закрываем файл
    f.close

    # Устанвливаем текущим файлом 1.mp3 и закрываем звуковое устройство
    # Это нужно чтобы мы могли удалить предыдущий mp3 файл без колизий
    mixer.music.load('1.mp3')
    mixer.stop
    mixer.quit

    # Удаляем последний предыдущий mp3 файл
    if(os.path.exists(mp3_nameold)):
        os.remove(mp3_nameold)

        #https://pythono.ru/tts-python/ """


saravoice()

