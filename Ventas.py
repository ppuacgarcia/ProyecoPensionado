from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvas


hiColor='#65A0A3'

class Ventas:
    def __init__(self,ventanaPrincipal):
        self.w = Frame(ventanaPrincipal,width=1200,height=675,bg='#3F5657')
        self.w.place(x=0, y=0)
        self.fuenteG = font=('Arial', 19,'bold')
        self.fuenteP = font=('Arial', 15,'bold')
        self.bglabel = '#3F5657'
        self.fglabel = '#FFFFFF'
        self.posx = 80

        #Etiquetas
        self.lab('Ventas', self.fuenteG, self.bglabel, self.fglabel, 580, 10)
        self.lab('Nombre Comida', self.fuenteP, self.bglabel, self.fglabel, self.posx, 55)
        self.lab('Proteina', self.fuenteP, self.bglabel, self.fglabel, self.posx, 85)

        #Cuadros de texto
        self.nombreComida=self.Ent(65, 250, 60)
        
        
        #comboBox
        self.combProteina = ['Res','Pollo','Mariscos', 'Cerdo']
        self.comboRan = ttk.Combobox(self.w, value=self.combProteina, width=62)
        self.comboRan.place(x=250, y=90)
        self.comboRan["state"]="readonly"
        self.comboRan.current(1)
        
        
        #Botones
        self.Guardar = self.btn(975, 600, 'guardar', '#FFFFFF', hiColor, self.on_button_click, 'Arial', 12,'bold',18,2)

               
        
    def cmd(self):
        self.conn.commit()
        self.w.destroy()

    #Labels formulario
    def lab(self,text, font, bg, fg, x, y):
        labe = Label(self.w,text=text, font=font, bg=bg, foreground=fg)
        labe.pack()
        labe.place(x=x, y=y)
    
    #Cuadros de Texto
    def Ent(self, width, x, y):
        Entr = Entry(self.w,width=width)
        Entr.pack()
        Entr.place(x=x, y=y)
        return Entr

    #Funcion para crear botones
    def btn(self, x, y, text, bcolor, fcolor, command, font, siz, tipe,wdt,ht):
        #Botones para menu
        def on_enter(e):
            buttons['background'] = bcolor
            buttons['foreground'] = fcolor
            
        def on_leave(e):
            buttons['background'] = fcolor
            buttons['foreground'] = bcolor
            
            
        buttons = Button(self.w, width=wdt, height=ht, text= text, fg  = bcolor, bg=fcolor, command=command, border=0, activebackground=bcolor, activeforeground=fcolor,font=(font, siz, tipe))
        buttons.bind("<Enter>", on_enter)
        buttons.bind("<Leave>", on_leave)
        buttons.place(x=x, y=y)
        return buttons
    
    def tb(self,x,y):
        tabla=Listbox(self.w)
        tabla.place(x=x,y=y)
        tabla.config(height=1)
        return tabla
    
    

    def mayus(self,nombreB):
        result=""
        for i in range ( len (nombreB) ):
            if(ord(nombreB[i])>96 and ord(nombreB[i])<122):
               result+=chr(ord(nombreB[i])-32)
            else:
                result+=nombreB[i]
        return result
    
    def on_button_click(self):
        pass