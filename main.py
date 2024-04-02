from tkinter import messagebox

import customtkinter
from customtkinter import *
from wikipedia import set_lang
from wikipedia import summary

def find(mozoe):
    set_lang("fa")
    javab = summary(mozoe,sentences=1)

#functions
def lightdarkk():
    ld = customtkinter.get_appearance_mode()
    if ld == "Dark":
        customtkinter.set_appearance_mode("light")
    if ld == "Light":
        customtkinter.set_appearance_mode("dark")
def update():
    set_lang("fa")
    mozoee = mozoe.get()
    javab = summary(mozoee,sentences=1)
    messagebox.showinfo(mozoee,javab)
    return javab
def aboutme():
    aboutpage = CTkToplevel()
    aboutpage.title("about me")
    about = CTkLabel(aboutpage,text="created by samiyartey\ncreated at 2024 with love❤\npowered by wikipedia")
    about.pack()
    aboutpage.wm_transient(root)

#main codes

root = CTk()
root.config(cursor="circle")
root.title("X SEARCH")
root.geometry("530x245")
tabcontrol = CTkTabview(root)
tabcontrol.pack(fill="both")
#search codes
maintab = tabcontrol.add("search")
searchlbl = CTkLabel(maintab,text="search:")
searchlbl.pack(fill="both")
mozoe = CTkEntry(maintab)
mozoe.pack(fill="both")
setbut=CTkButton(maintab,text="show",command=update)
setbut.pack(fill="both")
#settings
setttab = tabcontrol.add("settings")
aboutbut = CTkButton(setttab,text="about me",command=aboutme)
aboutbut.pack()
darklightbut = CTkButton(setttab,text="change between dark and light mode",command=lightdarkk)
darklightbut.pack()


root.mainloop()