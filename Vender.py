from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvas
from Ventas import *
from Conexion import conexion
class Vender:
    def __init__(self):
        def btn(x, y, text, bcolor, fcolor, command, font, siz, tipe,wdt,ht):
            #Botones para menu
            def on_enter(e):
                buttons['background'] = bcolor
                buttons['foreground'] = fcolor
                
            def on_leave(e):
                buttons['background'] = fcolor
                buttons['foreground'] = bcolor
            buttons = Button(fVent, width=wdt, height=ht, text= text, fg  = bcolor, bg=fcolor, command=command, border=0, activebackground=bcolor, activeforeground=fcolor,font=(font, siz, tipe))
            buttons.bind("<Enter>", on_enter)
            buttons.bind("<Leave>", on_leave)
            buttons.place(x=x, y=y)
            return buttons
        def Cmd1Tp1():
            print("holamundo")
        def Cmd1Tp2():
            print("holamundo")
        def Cmd1Tp3():
            print("holamundo")
        def Cmd2Tp1():
            print("holamundo")
        def Cmd2Tp2():
            print("holamundo")
        def Cmd2Tp3():
            print("holamundo")
        def Cmd3Tp1():
            print("holamundo")
        def Cmd3Tp2():
            print("holamundo")
        def Cmd3Tp3():
            print("holamundo")
        

        celHt=30
        hiColor='#65A0A3'
        colorbg="#3F5657"
        sw = Tk()
        sw.geometry('800x300')
        sw.configure(bg=hiColor)
        sw.resizable(0,0)
        sw.title('Pensionado')
        sw.iconbitmap('Images/user.ico')
        fonttxt = 'Arial'
        posx=430
        posy=100
        fVent = Frame(sw,width=800,height=300,bg=hiColor)
        fVent.place(x=0, y=0)
        #botones
        AddComida1= btn(350,celHt, '+', '#FFFFFF', colorbg, Cmd1Tp1, 'Arial', 12,'bold',10,1)
        AddComida2= btn(350,celHt*2, '+', '#FFFFFF', colorbg, Cmd1Tp2, 'Arial', 12,'bold',10,1)
        AddComida3= btn(350,celHt*3, '+', '#FFFFFF', colorbg, Cmd1Tp3, 'Arial', 12,'bold',10,1)
        AddComida4= btn(350,celHt*4, '+', '#FFFFFF', colorbg, Cmd2Tp1, 'Arial', 12,'bold',10,1)
        AddComida5= btn(350,celHt*5, '+', '#FFFFFF', colorbg, Cmd2Tp2, 'Arial', 12,'bold',10,1)
        AddComida6= btn(350,celHt*6, '+', '#FFFFFF', colorbg, Cmd2Tp3, 'Arial', 12,'bold',10,1)
        AddComida7= btn(350,celHt*7, '+', '#FFFFFF', colorbg, Cmd3Tp1, 'Arial', 12,'bold',10,1)
        AddComida8= btn(350,celHt*8, '+', '#FFFFFF', colorbg, Cmd3Tp2, 'Arial', 12,'bold',10,1)
        AddComida9= btn(350,celHt*9, '+', '#FFFFFF', colorbg, Cmd3Tp3, 'Arial', 12,'bold',10,1)
        #Tabla
        tabladata = ttk.Treeview(fVent)
        tabladata=ttk.Treeview(fVent,columns=("col1","col2"), height=21)
        tabladata.column("#0", width=40)
        tabladata.column("col1",width=200, anchor=CENTER)
        tabladata.column("col2",width=80, anchor=CENTER)
        tabladata.heading("#0",text="Id",anchor=CENTER)
        tabladata.heading("col1",text="Comida",anchor=CENTER)
        tabladata.heading("col2",text="Cantidad",anchor=CENTER)
        tabladata.place(x=10,y=0)
        
