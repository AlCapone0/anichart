#!/usr/bin/python3
# -*- coding: utf-8 -*-

#import scriptQTJPEG
import urllib.request
import os
import time
import sys
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
from PyQt5.QtGui import QIcon

class anychart(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        #Параметры первой кнопки
        btn1 = QPushButton('Скачать anychart-bundlle.min.js с cdn.anychart.com', self)
        btn1.move(10, 30)
        btn1.adjustSize()

        #Параметры второй кнопки
        btn2 = QPushButton('Генерируем HTML файл', self)
        btn2.move(10, 70)
        btn2.adjustSize()

        #Параметры третей кнопки
        btn3 = QPushButton('Используя PhantomJS генерируем screenshot', self)
        btn3.move(10, 110)
        btn3.adjustSize()

        #Параметры четвертой кнопки
        btn4 = QPushButton('Показать screenshot', self)
        btn4.move(10, 150)
        btn4.adjustSize()

        #Сигналы четырех кнопок
        btn1.clicked.connect(self.btnjs)
        btn2.clicked.connect(self.btnhtm)
        btn3.clicked.connect(self.bthjpeg)
        btn4.clicked.connect(self.btnshow)

        menuUI = self.menuBar()
        menuUI.addMenu('Menu')
        menuUI.addMenu('Help')
        menuUI.addMenu('About')

        #Параметры основного окна
        self.statusBar()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('anychart.com')
        self.setWindowIcon(QIcon('web.png'))
        self.menuBar()
        self.show()


#-----------------------------------------------------------------------------------------------------------------------
    #функция первой кнопки
    def btnjs(self):
        #проверяем доступность хоста anychart.com и скачиваем JS скрипт
        host = "cdn.anychart.com"
        pinghost = os.system("ping -n 1 " + host) #отправляем в ОС команду Ping в один пакет, если возрат 0 то GOOT.
        if pinghost == 0:
            js = urllib.request.urlopen("http://cdn.anychart.com/js/latest/anychart-bundle.min.js").read() #создали файлоподобный объект
            falejs = open("anychart-bundle.min.js", "wb") #создаём фаил js на запись
            falejs.write(js) #записываем файл js
            falejs.close()   #закрываем файл js
            js = urllib.request.urlopen("http://cdn.anychart.com/js/latest/anychart-bundle.min.js").close() #закрыли файлоподобный объект
            print (host, u'хост доступен') #выводим сообщение в консоль если все ОК
            self.statusBar().showMessage(u'хост доступен')#выводим сообщение в statusBar
        else:
            print (host, u'ошибка: хост недоступен') #выводим сообщение в консоль если Ping не прошёл
            self.statusBar().showMessage(u'ошибка: хост недоступен') #выводим сообщение в statusBar


#-----------------------------------------------------------------------------------------------------------------------
    #функция второй кнопки
    def btnhtm(self):
        #создаём index.htm
        faletext = open("text.txt", "r").read() #открыли файл на чтение
        falehtm = open("index.htm", "w") #открыли файл на запись
        falehtm.write(faletext) #записали файл
        falehtm.close() #закрыли файл
        #проверяем наличия фаила index.htm
        if os.path.exists("index.htm"): #оправляем команду ОС чтобы проверила наличия файла index.htm
            print(u'файл создан  index.htm') #выводим сообщение в консоль если все ОК
            self.statusBar().showMessage(u'файл создан  index.htm') #выводим сообщение в statusBar
        else:
            print(u'ошибка:файл не оздан  index.htm') #выводим сообщение в консоль если все BAD
            self.statusBar().showMessage(u'ошибка:файл не оздан  index.htm') #выводим сообщение в statusBar


#-----------------------------------------------------------------------------------------------------------------------
    #функция третей кнопки
    def bthjpeg(self):
        #создаём скриншот index.htm
        os.popen(r"phantomjs.exe screenshot.js") #отправляем команду ОС на открытие программы PhantomJS с параметром screenshot.js
        time.sleep(5) #дадим ОС 5 сек. для создания скриншота, но это неправельно
        #проверяем наличия фаила index.htm
        if os.path.exists("Index.jpeg"): #оправляем команду ОС чтобы проверила наличия файла Index.jpeg
            print(u'файл создан  index.jpeg') #выводим сообщение в консоль если все ОК
            self.statusBar().showMessage(u'файл создан  index.jpeg') #выводим сообщение в statusBar
        else:
            print(u'ошибка:файл не оздан  index.jpeg') #выводим сообщение в консоль если все BAD
            self.statusBar().showMessage(u'ошибка:файл не оздан  index.jpeg') #выводим сообщение в statusBar


#-----------------------------------------------------------------------------------------------------------------------
    #функция четвертой кнопки
    def btnshow(self):
        os.startfile('Index.jpeg')#отправляем команду ОС на открытие файла скриншота
        print(u'открытие файла index.jpeg') #выводим сообщение в консоль если все BAD
        self.statusBar().showMessage(u'открытие файла index.jpeg') #выводим сообщение в statusBar

#-----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':

    app = QApplication(sys.argv)
    scriptQT = anychart() #экземпляр  класса
    sys.exit(app.exec_())