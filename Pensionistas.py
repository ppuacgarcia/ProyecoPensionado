from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvas
from tkcalendar import *

hiColor='#65A0A3'

class Pensionistas:
    def __init__(self,ventanaPrincipal):
        self.w = Frame(ventanaPrincipal,width=1200,height=675,bg='#3F5657')
        self.w.place(x=0, y=0)
        self.fuenteG = font=('Arial', 19,'bold')
        self.fuenteP = font=('Arial', 15,'bold')
        self.bglabel = '#3F5657'
        self.fglabel = '#FFFFFF'
        self.posx = 50

        #Etiquetas
        self.lab('Pensionistas', self.fuenteG, self.bglabel, self.fglabel, 560, 10)
        self.lab('Nombre', self.fuenteP, self.bglabel, self.fglabel, self.posx, 55)
        self.lab('Fecha Nacimiento', self.fuenteP, self.bglabel, self.fglabel, self.posx, 85)
        self.lab('Fecha Pago', self.fuenteP, self.bglabel, self.fglabel, self.posx, 115)

        #Cuadros de texto
        self.nombrePens=self.Ent(65, 250, 60)
        
        #Calendarios
        self.calNac=DateEntry(self.w,width=61)
        self.calNac.place(x=250,y=90)
        self.calPago=DateEntry(self.w,width=61)
        self.calPago.place(x=250,y=120)
        
        
        #Botones
        self.Guardar = self.btn(975, 600, 'guardar', '#FFFFFF', hiColor, self.SearchOnTable, 'Arial', 12,'bold',18,2)
        
        #Tabla
        self.tabladata = ttk.Treeview(self.w)
        self.tabladata=ttk.Treeview(self.w,columns=("col1","col2","col3"), height=21)
        self.tabladata.column("#0", width=40)
        self.tabladata.column("col1",width=280, anchor=CENTER)
        self.tabladata.column("col2",width=70, anchor=CENTER)
        self.tabladata.column("col3",width=70, anchor=CENTER)
        self.tabladata.heading("#0",text="Id",anchor=CENTER)
        self.tabladata.heading("col1",text="Nombre",anchor=CENTER)
        self.tabladata.heading("col2",text="Nacimiento",anchor=CENTER)
        self.tabladata.heading("col3",text="Fecha pago",anchor=CENTER)
        self.tabladata.place(x=680,y=70)

               
        
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
    
    
    def AddToTable(self):
        cantidad_filas = len(self.tabladata.get_children())+1
        comida = self.nombrePens.get()
        Nac = self.calNac.get()+""
        pago = self.calNac.get()+""
        self.tabladata.insert("", tk.END, text=cantidad_filas, values=(comida, Nac, pago))
        pass
    
    def SearchOnTable(self):
        resultado = False
        print("1")
        for child in self.tabladata.get_children():
            # Obtener los valores de las celdas de la fila
            nombre = self.tabladata.item(child, "values")[0]
            print("---"+nombre+"---")
            print(2)
            if(self.nombrePens.get() == nombre):
                print(3)
                resultado = True
                print("Esta Persona ya se ha agregado anteriormente")
        if(resultado == False): 
            self.AddToTable()
        
    def clearAll(self):
        pass