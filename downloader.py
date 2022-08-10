import requests
from bs4 import BeautifulSoup
import os
from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *

pbar = ttk.Window(themename="darkly")
pbar.overrideredirect(True)
pbar.title("PoE Builds Downloader")
pbar.geometry("400x200")
my_progress = ttk.Progressbar(pbar, bootstyle="striped", orient=HORIZONTAL, length=200, mode='determinate')
my_progress.pack()
pbarlab = ttk.Label(pbar, text="PoE BUILDS DOWNLOADER")
pbarlab.pack()

tablist  = ["duelist", 'marauder', 'ranger', 'scion', 'templar', 'witch', 'shadow']

#download all builds
pbar.update()
def downloadbuilds():
    url = "https://www.poebuilds.cc/"
    try:
        for i in range (0, 6, 1):
            r = requests.get(url + tablist[i], headers={'User-Agent': 'Mozilla/5.0'}, verify=True, timeout=10, allow_redirects=True, proxies=None)
            pbarlab2 = ttk.Label(pbar, text="Downloading " + tablist[i] + " builds")
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

if not os.path.exists ('buildname.txt'):
    downloadbuilds()
pbar.destroy()

