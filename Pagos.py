from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvas
from Conexion import conexion
from datetime import date
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
        AddPago= self.btn(350,self.celHt+20, '-', '#FFFFFF', self.colorbg, self.CmdPago, 'Arial', 12,'bold',10,1)
        #Tabla
        self.tabladata = ttk.Treeview(self.fVent)
        self.tabladata=ttk.Treeview(self.fVent,columns=("col1","col2","col3"), height=14)
        self.tabladata.column("#0", width=40)
        self.tabladata.column("col1",width=120, anchor=CENTER)
        self.tabladata.column("col2",width=80, anchor=CENTER)
        self.tabladata.column("col3",width=80, anchor=CENTER)
        self.tabladata.heading("#0",text="Id",anchor=CENTER)
        self.tabladata.heading("col1",text="Nombre",anchor=CENTER)
        self.tabladata.heading("col2",text="FechaPago",anchor=CENTER)
        self.tabladata.heading("col3",text="EstadoPago",anchor=CENTER)
        self.tabladata.place(x=20,y=20)
        cur = self.conn.consultaBD("SELECT id, Nombre,FechaPago,`Estado de pago_id` FROM Pensionado.Pensionistas")
        for row in cur:
            id, comida,FechaPago,Pago= row
            self.tabladata.insert('', 'end', text='', values=[comida, FechaPago,Pago])
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
    def CmdPago(self):
        hoy = date.today().strftime('%Y-%m-%d')
        print(self.tabladata.get_children())
        nombre = self.tabladata.item("I001", "values")[0]
        nombre_str = str(nombre)
        print(nombre_str)
        PagoC=self.conn.consultaBD("SELECT m_atrasado FROM  pensionistas  JOIN `Estado de pago` ON pensionistas.`Estado de pago_id`=`Estado de pago`.id where pensionistas.nombre ='"+nombre+"'")
        Pago=int(PagoC.fetchone()[0])
        print("----"+str(Pago))
        if(Pago>0):
            cur = self.conn.consultaBD("UPDATE pensionistas SET m_atrasado =(m_atrasado - 1) FROM pensionistas JOIN `Estado de pago` ON pensionistas.`Estado de pago_id`=`Estado de pago`.id  WHERE pensionistas.nombre = '" + nombre_str + "'")
        