import tkinter as tk
from turtle import bgcolor, width
from tkinter import *
from PIL import Image, ImageTk
import os
from datetime import datetime
#import de pestañas
from MenuPrincipal import *
pw = Tk()
pw.geometry('1200x675')
pw.configure(bg='#3F5657')
pw.resizable(0,0)
pw.title('Pensionado')
pw.iconbitmap('Images/user.ico')
fonttxt = 'Arial'
posx=430
posy=100
hiColor='#65A0A3'
colorbg="#3F5657"
flog = Frame(pw,width=1200,height=675,bg=colorbg)
flog.place(x=0, y=0)
def Correcto():
    if(Username.get()=="" and Password.get()==""):
        MenP(pw)
        flog.destroy()
        print("entro")
    else:
        print("no entro")
def hi(x = None, y = None, event = None):
    #print(conn.getPass+"contrasenia")
    now = datetime.now() # current date and time
#Labels
#imagenes
global logoH
lgimg=Image.open('Images/user.ico')
lgimg.resize((100,100),Image.ANTIALIAS)
logoH = ImageTk.PhotoImage(lgimg)
bglabel=Label(flog,image=logoH, border=0,bg=colorbg).place(x=posx, y = posy)
#labels
#user label
UserLabel=Label(flog,text='Usuario')
UserLabel.place(x=posx,y=posy+260)
UserLabel.config(bg=colorbg,font=(fonttxt,15,'bold'))
#password label
PasswordLabel=Label(flog,text='Clave')      
PasswordLabel.place(x=posx,y=posy+315)
PasswordLabel.config(bg=colorbg,font=(fonttxt,15,'bold'))
#login label
LoginLablel=Label(flog, text='Inicio')
LoginLablel.place(x=posx+80,y=0)
LoginLablel.config(bg=colorbg,font=(fonttxt,40,'bold'))
#username enrty
Username=StringVar()
Username_entry = Entry(flog,textvariable=Username)
Username_entry.config(width=30,font=(fonttxt,12))
Username_entry.place(x=posx,y=posy+290)
#password entry
Password=StringVar()
EntryPassword=Entry(flog,textvariable=Username)
EntryPassword.config(width=30,font=(fonttxt,12),textvariable=Password,show='■')
EntryPassword.place(x=posx,y=posy+340)
#button
def btnLog(pw, x, y, text, bcolor, fcolor, command, font, siz, tipe):
        #Botones para menu
        def on_enter(e):
            buttons['background'] = bcolor
            buttons['foreground'] = fcolor
            
        def on_leave(e):
            buttons['background'] = fcolor
            buttons['foreground'] = bcolor
        buttons = Button(pw, width=15, height=1, text= text, fg  = bcolor, bg=fcolor, command=command, border=0, activebackground=bcolor, activeforeground=fcolor,font=(font, siz, tipe))
        buttons.bind("<Enter>", on_enter)
        buttons.bind("<Leave>", on_leave)
        buttons.place(x=x, y=y)
btnLog(pw,posx+25,posy+370,"Entrar", hiColor, '#FFFFFF', Correcto,'Arial', 16,'bold')
pw.mainloop()