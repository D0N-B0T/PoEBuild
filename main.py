from textwrap import wrap
from time import sleep
import time
import requests, random, webbrowser, os
from bs4 import BeautifulSoup
from PIL import ImageTk, Image
import downloader as dwview
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
import tkinter as tk
from tkinter import Menu



# === functions ===
tablist  = ["duelist", 'marauder', 'ranger', 'scion', 'templar', 'witch', 'shadow']

def randombuild():            
    with open('buildname.txt', 'r', encoding='utf-8') as f:
        buildnamelab = ttk.Label(root, wrap = 300)
        buildnamelab.place(x=300, y=50)
        buildlinklab = ttk.Label(root, text=buildnamelab.cget("text"), cursor='hand2')
        buildlinklab.place(x=300, y=100)
        buildlinklab.bind("<Button-1>", lambda e: webbrowser.open_new(buildlinklab.get()))
        lines = f.readlines()
        rand = random.randint(0,len(lines)-1)
        buildnamelab.configure(text=lines[rand])
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

def update():
    #add label
    updatelab = ttk.Label(root, text='Updating your builds...')
    updatelab.place(x=0, y=20)
    time.sleep(3)
    updatelab.destroy()
    os.remove('buildname.txt')
    os.remove('buildlink.txt')
    updatelab3 = ttk.Label(root, text='Downloading new builds... Window can freeze for a while')
    updatelab3.place(x=0, y=20)
    sleep(3)
    updatelab3.destroy()
    downloadbuilds2()
    updatelab4 = ttk.Label(root, text='New builds have been downloaded')
    updatelab4.place(x=0, y=20)
    sleep(3)
    updatelab4.destroy()


    



def downloadbuilds2():
    url = "https://www.poebuilds.cc/"
    try:
        for i in range (0, 6, 1):
            r = requests.get(url + tablist[i], headers={'User-Agent': 'Mozilla/5.0'}, verify=True, timeout=10, allow_redirects=True, proxies=None)
            dwview.pbar.update_idletasks()
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

def search():
    with open ('buildname.txt', 'r', encoding='utf-8') as f:
        datafile = f.readlines()
        found = False
        for line in datafile:
            if search_entry.get().lower() in line.lower():
                found = True
                break
        if found:
            buildnamelab = ttk.Label(root,wrap=300)
            buildnamelab.place(x=300, y=50)

            buildlinklab = ttk.Label(root, text=buildnamelab.cget("text"), cursor='hand2')
            buildlinklab.place(x=300, y=90)
            buildlinklab.bind("<Button-1>", lambda e: webbrowser.open_new(buildlinklab.get()))
            buildnamelab.configure(text=line)
            with open ('buildlink.txt', 'r', encoding='utf-8') as f:
                buildlinklab.configure(text=f.readline())
                buildlinklab.bind("<Button-1>", lambda e: webbrowser.open_new(buildlinklab.cget("text")))
        else:
            label = ttk.Label(root, text="No build found", font=("Arial", 10))
            label.place(x=300, y=200)
            label.after(2000, lambda: label.destroy())
        search_entry.delete(0, END)

#  === root window ===
root = tk.Tk()
root.title("PoE BUILDS PICKER")
dwview.pbar.update_idletasks() 
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (300, 200, 500 , 100))
# root.resizable(False, False)
root.geometry("705x405")

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar)

file_menu.add_command(label="Update", command=update)



# === labels ===
img = ImageTk.PhotoImage(Image.open('img/default.png'))
imgP = ttk.Label(root, image = img)
imgP.place(x=0, y=0)
imgP.image = img

updatebuild_btn = ttk.Button(root, bootstyle="dark", text="!", compound=LEFT, command=update)
updatebuild_btn.place(x=650, y=380)

search_entry = ttk.Entry(root, width=30)
search_entry.place(x=300, y=220)
search_entry.focus_set()

search_button = ttk.Button(root,bootstyle="dark", text="Search", command=search)
search_button.place(x=300, y=240)

randombuild_button = ttk.Button(root, bootstyle="success-outline", text="Random Build", command=randombuild)
randombuild_button.place(x=300, y=280)




root.mainloop()