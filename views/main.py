import requests, random, webbrowser, os
from bs4 import BeautifulSoup
from PIL import ImageTk, Image
import downloader as dwview
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *

# === functions ===
tablist  = ["duelist", 'marauder', 'ranger', 'scion', 'templar', 'witch', 'shadow']

def randombuild():            
    with open('dyn/buildname.txt', 'r', encoding='utf-8') as f:
        buildnamelab = ttk.Label(root)
        buildnamelab.place(x=300, y=50)

        buildlinklab = ttk.Label(root, text=buildnamelab.cget("text"), cursor='hand2')
        buildlinklab.place(x=300, y=70)
        buildlinklab.bind("<Button-1>", lambda e: webbrowser.open_new(buildlinklab.get()))
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

    with open('dyn/buildlink.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        buildlinklab.configure(text=lines[rand])
        buildlinklab.bind("<Button-1>", lambda e: webbrowser.open_new(buildlinklab.cget("text")))

def update():
    os.remove('dyn/buildname.txt')
    os.remove('dyn/buildlink.txt')
    downloadbuilds2()
    MessageDialog("Update", "Builds updated")

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
                        with open('dyn/buildname.txt', 'a', encoding='utf-8') as f: 
                            f.write(tablist[i] + ' ')
                            f.write(name_build)
                            f.write('\n')
                        with open('dyn/buildlink.txt', 'a', encoding='utf-8') as f: 
                            f.write(link_build)
                            f.write('\n')
            except:
                pass
    except Exception as e:
        print(e)
        print('Error')

def search():
    with open ('dyn/buildname.txt', 'r', encoding='utf-8') as f:
        datafile = f.readlines()
        found = False
        for line in datafile:
            if search_entry.get().lower() in line.lower():
                found = True
                break
        if found:
            buildnamelab = ttk.Label(root)
            buildnamelab.place(x=300, y=50)

            buildlinklab = ttk.Label(root, text=buildnamelab.cget("text"), cursor='hand2')
            buildlinklab.place(x=300, y=70)
            buildlinklab.bind("<Button-1>", lambda e: webbrowser.open_new(buildlinklab.get()))
            buildnamelab.configure(text=line)
            with open ('dyn/buildlink.txt', 'r', encoding='utf-8') as f:
                buildlinklab.configure(text=f.readline())
                buildlinklab.bind("<Button-1>", lambda e: webbrowser.open_new(buildlinklab.cget("text")))
        else:
            label = ttk.Label(root, text="No build found", font=("Arial", 10))
            label.place(x=300, y=200)
            label.after(2000, lambda: label.destroy())
        search_entry.delete(0, END)

#  === root window ===
root = ttk.Window(themename="darkly")
root.title("PoE BUILDS PICKER")
dwview.pbar.update_idletasks() 
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (300, 200, 500 , 100))
root.resizable(False, False)
root.geometry("705x405")


# === labels ===
img = ImageTk.PhotoImage(Image.open("img/default.png"))
imgP = ttk.Label(root, image = img)
imgP.place(x=0, y=0)
imgP.image = img

updatebuild_btn = ttk.Button(root, bootstyle="dark", text="Update!", compound=LEFT, command=update)
updatebuild_btn.place(x=650, y=380)

search_entry = ttk.Entry(root, width=30)
search_entry.place(x=300, y=220)
search_entry.focus_set()

search_button = ttk.Button(root,bootstyle="dark", text="Search", command=search)
search_button.place(x=300, y=240)

randombuild_button = ttk.Button(root, bootstyle="success-outline", text="Random Build", command=randombuild)
randombuild_button.place(x=300, y=280)

root.mainloop()