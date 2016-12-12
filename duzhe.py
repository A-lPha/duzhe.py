from Tkinter import *
import urllib2
import os
from bs4 import BeautifulSoup
import webbrowser

top = Tk()
top.geometry('650x150')
def open_web():
    year = var1.get()
    mouth = var2.get()
    time = year + "_" + mouth
    baseurl = 'http://www.52duzhe.com/' + time +'/'
    firsturl = baseurl + 'index.html'
    webbrowser.open(firsturl)

def download_txt():
    year = var1.get()
    mouth = var2.get()
    time = year + "_" + mouth
    baseurl = 'http://www.52duzhe.com/' + time +'/'
    firsturl = baseurl + 'index.html'
    def urlBS(url):
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        return soup
    soup = urlBS(firsturl)
    link = soup.select('.booklist a')
    path = os.getcwd()+u'/读者文章保存/'
    if not os.path.isdir(path):
        os.mkdir(path)
    for item in link:
        newurl = baseurl + item['href']
        result = urlBS(newurl)
        title = result.find("h1").string
        writer = result.find(id="pub_date").string.strip()
        filename = path + title + '.txt'
        print filename.encode("gbk")
        new=open(filename,"w")
        new.write("<<" + title.encode("gbk") + ">>\n\n")
        new.write(writer.encode("gbk")+"\n\n")
        text = result.select('.blkContainerSblkCon p')
        for p in text:
            context = p.text
            new.write(context.encode("utf-8"))
        new.close()
var1=StringVar()
var2=StringVar()
label1 = Label(top,text='读者文章下载器',font='Helvetica -20 bold')
label2 = Label(text='请输入年份:',font='Helvetica -16 bold')
label3 = Label(text='请输入月份:',font='Helvetica -16 bold')
entry1 = Entry(top,text='',textvariable=var1,font='Helvetica -16 bold')
entry2 = Entry(top,text='',textvariable=var2,font='Helvetica -16 bold')
button1 = Button(text=' 打开 ',command=open_web,font='Helvetica -16 bold')
button2 = Button(text=' 退出 ',command=top.quit,activeforeground='white',activebackground='red',font='Helvetica -16 bold')
button3 = Button(text=' 下载 ',command=download_txt,font='Helvetica -16 bold')
label1.pack()
label2.pack(side='left')
entry1.pack(side='left')
label3.pack(side='left')
entry2.pack(side='left')
button1.pack()
button2.pack()
button3.pack()
top.mainloop()
