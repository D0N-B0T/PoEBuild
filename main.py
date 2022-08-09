from cProfile import label
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup
import random
from tkinter import *
import webbrowser
import os
import ttkbootstrap as ttk
import time
from PIL import ImageTk, Image
from ttkbootstrap.constants import *


pbar = Tk()
pbar.withdraw()
pbar.update_idletasks()  # Update "requested size" from geometry manager
pbar.deiconify()


pbar.title("Builds")
pbar.geometry("400x200")
my_progress = ttk.Progressbar(pbar, orient=HORIZONTAL, length=200, mode='determinate')
my_progress.pack()
pbarlab = Label(pbar, text="PoE BUILDS DOWNLOADER")
pbarlab.pack()

tablist  = ["duelist", 'marauder', 'ranger', 'scion', 'templar', 'witch', 'shadow']

#download all builds
pbar.update()
def downloadbuilds():
    url = "https://www.poebuilds.cc/"
    try:
        for i in range (0, 6, 1):
            r = requests.get(url + tablist[i], headers={'User-Agent': 'Mozilla/5.0'}, verify=True, timeout=10, allow_redirects=True, proxies=None)
            pbarlab2 = Label(pbar, text="Downloading " + tablist[i] + " builds")
            pbarlab2.pack()
            my_progress['value'] += 17
            pbar.update_idletasks()
            try:
                for j in range(20,40,2):                    
                    soup = BeautifulSoup(r.text, 'html.parser')
                    name_build = soup.find_all('a')[j].get('title')
                    link_build = soup.find_all('a')[j].get('href')
                    if link_build.startswith('https://www.poebuilds.cc/'):
                        continue
                    else:
                        with open('buildname.txt', 'a', encoding='utf-8') as f: 
                            f.write(tablist[i] + ' ')
                            f.write(name_build)
                            f.write('\n')
                        with open('buildlink.txt', 'a', encoding='utf-8') as f: 
                            f.write(link_build)
                            f.write('\n')
            except:
                pass
    except Exception as e:
        print(e)
        print('Error')

if not os.path.exists ('buildname.txt'):
    downloadbuilds()
pbar.destroy()

root = Tk()
pbar.update_idletasks()  # Update "requested size" from geometry manager
x = 600
y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
root.geometry("+%d+%d" % (x, y))
root.deiconify()
root.title("PoE Build Visor")
root.geometry("700x300")
root.configure(background='white')

def randombuild():            
    with open('buildname.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        rand = random.randint(0,len(lines)-1)
        buildnamelab.configure(text='Your class is ' + lines[rand])
        buildlinklab.bind("<Button-1>", lambda e: webbrowser.open_new(buildlinklab.cget("text")))
        if lines[rand].startswith('duelist'):
            img = ImageTk.PhotoImage(Image.open("img/duelist.png"))
            imgP.configure(image=img)
            imgP.image = img
        elif lines[rand].startswith('marauder'):
            img = ImageTk.PhotoImage(Image.open("img/marauder.png"))
            imgP.configure(image=img)
            imgP.image = img
        elif lines[rand].startswith('ranger'):
            img = ImageTk.PhotoImage(Image.open("img/ranger.png"))
            imgP.configure(image=img)
            imgP.image = img
        elif lines[rand].startswith('scion'):
            img = ImageTk.PhotoImage(Image.open("img/scion.png"))
            imgP.configure(image=img)
            imgP.image = img
        elif lines[rand].startswith('templar'):
            img = ImageTk.PhotoImage(Image.open("img/templar.png"))
            imgP.configure(image=img)
            imgP.image = img
        elif lines[rand].startswith('witch'):
            img = ImageTk.PhotoImage(Image.open("img/witch.png"))
            imgP.configure(image=img)
            imgP.image = img
        elif lines[rand].startswith('shadow'):
            img = ImageTk.PhotoImage(Image.open("img/shadow.png"))
            imgP.configure(image=img)
            imgP.image = img
        else:
            img = ImageTk.PhotoImage(Image.open("img/default.png"))
            imgP.configure(image=img)
            imgP.image = img

    with open('buildlink.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        buildlinklab.configure(text=lines[rand])
        buildlinklab.bind("<Button-1>", lambda e: webbrowser.open_new(buildlinklab.cget("text")))
        

        
startbuild = Label (root, text="Welcome", font=("Arial", 30), bg='white')
startbuild.pack()

img = ImageTk.PhotoImage(Image.open("img/default.png"))
imgP = Label(root, image = img)
imgP.pack()
imgP.image = img

buildnamelab = Label(root, text="", font=("Arial", 10),bg='white')
buildnamelab.pack()

buildlinklab = Label(root, text=buildnamelab.cget("text"), font=("Arial", 10), fg='blue', cursor='hand2', bg='white')
buildlinklab.pack()
buildlinklab.bind("<Button-1>", lambda e: webbrowser.open_new(buildlinklab.get()))

desiredbuild_button = Button(root, text="Random Build", command=randombuild)
desiredbuild_button.pack()

#resize update.png to fit in windo



def update():
    os.remove('buildname.txt')
    os.remove('buildlink.txt')
    downloadbuilds2()
    
    messagebox.showinfo("Update", "Builds updated")


def downloadbuilds2():
    url = "https://www.poebuilds.cc/"
    try:
        for i in range (0, 6, 1):
            r = requests.get(url + tablist[i], headers={'User-Agent': 'Mozilla/5.0'}, verify=True, timeout=10, allow_redirects=True, proxies=None)
            pbar.update_idletasks()
            try:
                for j in range(20,40,2):                    
                    soup = BeautifulSoup(r.text, 'html.parser')
                    name_build = soup.find_all('a')[j].get('title')
                    link_build = soup.find_all('a')[j].get('href')
                    if link_build.startswith('https://www.poebuilds.cc/'):
                        continue
                    else:
                        with open('buildname.txt', 'a', encoding='utf-8') as f: 
                            f.write(tablist[i] + ' ')
                            f.write(name_build)
                            f.write('\n')
                        with open('buildlink.txt', 'a', encoding='utf-8') as f: 
                            f.write(link_build)
                            f.write('\n')
            except:
                pass
    except Exception as e:
        print(e)
        print('Error')






updatebuild_btn = Button(root, text="Update Builds", compound=LEFT, command=update)
updatebuild_btn.pack(side=TOP)


#get image


root.mainloop()