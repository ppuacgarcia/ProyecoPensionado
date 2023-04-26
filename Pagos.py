from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvas
from Conexion import conexion
hiColor='#65A0A3'

class Pagos:
    conn = conexion()
    celHt=29
    hiColor='#65A0A3'
    colorbg="#3F5657"
    fonttxt = 'Arial'
    def __init__(self,sw):
        self.fVent = Frame(sw,width=500,height=350,bg=self.hiColor)
        self.fVent.place(x=0, y=0)
        #botones
        AddComida1= self.btn(350,self.celHt+20, '+', '#FFFFFF', self.colorbg, self.Cmd1Tp1, 'Arial', 12,'bold',10,1)
       
        #Tabla
        tabladata = ttk.Treeview(self.fVent)
        tabladata=ttk.Treeview(self.fVent,columns=("col1","col2"), height=14)
        tabladata.column("#0", width=40)
        tabladata.column("col1",width=200, anchor=CENTER)
        tabladata.column("col2",width=80, anchor=CENTER)
        tabladata.heading("#0",text="Id",anchor=CENTER)
        tabladata.heading("col1",text="Nombre",anchor=CENTER)
        tabladata.heading("col2",text="FechaPago",anchor=CENTER)
        tabladata.place(x=20,y=20)
        cur = self.conn.consultaBD("SELECT id, Nombre,FechaPago FROM Pensionado.Pensionistas")
        for row in cur:
            id, comida,FechaPago= row
            tabladata.insert('', 'end', text='', values=[comida, FechaPago])
    def btn(self,x, y, text, bcolor, fcolor, command, font, siz, tipe,wdt,ht):
            #Botones para menu
            def on_enter(e):
                buttons['background'] = bcolor
                buttons['foreground'] = fcolor
                
            def on_leave(e):
                buttons['background'] = fcolor
                buttons['foreground'] = bcolor
            buttons = Button(self.fVent, width=wdt, height=ht, text= text, fg  = bcolor, bg=fcolor, command=command, border=0, activebackground=bcolor, activeforeground=fcolor,font=(font, siz, tipe))
            buttons.bind("<Enter>", on_enter)
            buttons.bind("<Leave>", on_leave)
            buttons.place(x=x, y=y)
            return buttons
    def Cmd1Tp1(self):
        print("holamundo")
    def Cmd1Tp2(self):
        print("holamundo")
    def Cmd1Tp3(self):
        print("holamundo")
    def Cmd2Tp1(self):
        print("holamundo")
    def Cmd2Tp2(self):
        print("holamundo")
    def Cmd2Tp3(self):
        print("holamundo")
    def Cmd3Tp1(self):
        print("holamundo")
    def Cmd3Tp2(self):
        print("holamundo")
    def Cmd3Tp3(self):
        print("holamundo")