from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvas
from MenuPrincipal import *
from Hospedaje import *
from Vender import *
from Conexion import conexion
hiColor='#65A0A3'

class Ventas:
    def __init__(self,ventanaPrincipal):
        self.conn = conexion()
        
        print("=================================================================================")
        self.w = Frame(ventanaPrincipal,width=1200,height=675,bg='#3F5657')
        self.w.place(x=0, y=0)
        self.fuenteG = font=('Arial', 19,'bold')
        self.fuenteP = font=('Arial', 15,'bold')
        self.bglabel = '#3F5657'
        self.fglabel = '#FFFFFF'
        self.posx = 50
        #Etiquetas
        self.lab('Ventas', self.fuenteG, self.bglabel, self.fglabel, 580, 10)
        self.lab('Nombre Comida', self.fuenteP, self.bglabel, self.fglabel, self.posx, 55)
        self.lab('Proteina', self.fuenteP, self.bglabel, self.fglabel, self.posx, 85)

        #Cuadros de texto
        self.nombreComida=self.Ent(65, 250, 60)
        #comboBox
        self.combProteina = ['Res','Pollo','Mariscos', 'Cerdo']
        self.comboProteina = ttk.Combobox(self.w, value=self.combProteina, width=62)
        self.comboProteina.place(x=250, y=90)
        self.comboProteina["state"]="readonly"
        self.comboProteina.current(1)

        #Botones
        self.Guardar = self.btn(975, 600, 'guardar', '#FFFFFF', hiColor, self.SearchOnTable, 'Arial', 12,'bold',18,2)
        self.vender = self.btn(675, 600, 'vender', '#FFFFFF', hiColor, self.Vender, 'Arial', 12,'bold',18,2)
        self.MenuP=self.btn(0, 0, 'Menu', '#FFFFFF', hiColor, self.Correcto, 'Arial', 12,'bold',8,2)
        #Tabla
        self.tabladata = ttk.Treeview(self.w)
        self.tabladata=ttk.Treeview(self.w,columns=("col1","col2","col3","col4","col5","col6"), height=21)
        self.tabladata.column("#0", width=40)
        self.tabladata.column("col1",width=150, anchor=CENTER)
        self.tabladata.column("col2",width=70, anchor=CENTER)
        self.tabladata.column("col3",width=45, anchor=CENTER)
        self.tabladata.column("col4",width=45, anchor=CENTER)
        self.tabladata.column("col5",width=45, anchor=CENTER)
        self.tabladata.column("col5",width=45, anchor=CENTER)
        self.tabladata.column("col6",width=85, anchor=CENTER)
        self.tabladata.heading("#0",text="Id",anchor=CENTER)
        self.tabladata.heading("col1",text="Comida",anchor=CENTER)
        self.tabladata.heading("col2",text="Proteina",anchor=CENTER)
        self.tabladata.heading("col3",text="Tipo 1",anchor=CENTER)
        self.tabladata.heading("col4",text="Tipo 2",anchor=CENTER)
        self.tabladata.heading("col5",text="Tipo 3",anchor=CENTER)
        self.tabladata.heading("col6",text="fecha",anchor=CENTER)
        self.tabladata.place(x=680,y=70)
        self.mostrarDatos()
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
    def Correcto(self): 
        #MenP(self.w)
        self.w.destroy()
        print("no entro")
    def Vender(self):
        sw = Toplevel()
        sw.geometry('500x350')
        sw.configure(bg=hiColor)
        sw.resizable(0,0)
        sw.title('Pensionado')
        sw.iconbitmap('Images/user.ico')
        
        Vender(sw)

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
        comida = self.nombreComida.get()
        Proteina = self.comboProteina.get()
        valor_Tipo1 = 0
        valor_Tipo2 = 0
        valor_Tipo3 = 0
        valor_Fecha = '2023/04/25'
        query = query = "INSERT INTO Pensionado.almuerzos (id, Nombre, Proteina, Tipo1, Tipo2, Tipo3, fecha) VALUES ({}, '{}', '{}', {}, {}, {}, '{}')".format(cantidad_filas, comida, Proteina, valor_Tipo1, valor_Tipo2, valor_Tipo3, valor_Fecha)
        self.conn.consultaBD(query)
        self.mostrarDatos()
        pass
    
    def SearchOnTable(self):
        resultado = False
        print("1")
        for child in self.tabladata.get_children():
            # Obtener los valores de las celdas de la fila
            nombre = self.tabladata.item(child, "values")[0]
            print("---"+nombre+"---")
            print(2)
            if(self.nombreComida.get() == nombre):
                print(3)
                resultado = True
                print("Esta comida ya se ha agregado anteriormente")
        if(resultado == False): 
            self.AddToTable()
            self.setPlots()
    def setPlots(self):
         ####Plot Pie####
        fig=plt.figure(figsize=(6,6),dpi=100)
        fig.set_size_inches(2.5,2.5)
        Prot=self.GetProt()
        colors=["#A85802","#33F551","#F58B1B","#5202F5"]
        explode=[0.2,0,0,0]
        plt.pie(Prot,explode=explode,labels=self.combProteina,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140)
        plt.axis('equal')
        canvasvar=FigureCanvas(fig,master=self.w)
        canvasvar.draw()
        canvasvar.get_tk_widget().place(anchor=CENTER,x=200,y=400)
        ####Plot Bar chart####
        figBar=plt.figure(figsize=(6,6),dpi=100)
        figBar.set_size_inches(2.5,2.5)
        labelpos=np.arange(len(self.combProteina))
        sizesPrecios=[Prot[0]*25,Prot[1]*25,Prot[2]*25,Prot[3]*25]
        colors=["#A85802","#33F551","#F58B1B","#5202F5"]
        explode=[0.2,0,0,0]
        plt.bar(labelpos,sizesPrecios,align=CENTER,alpha=1.0)
        plt.xticks(labelpos,self.combProteina)
        plt.ylabel('precios')
        plt.xlabel('tipos de proteina')
        plt.tight_layout(pad=2.2,w_pad=0.5,h_pad=0.1)
        plt.xticks(rotation=50,horizontalalignment='center')
        for index, datapoints in enumerate(sizesPrecios):
            plt.text(x=index,y=datapoints+0.3,s=f"{datapoints}",fontdict=dict(fontsize=10),ha='center',va='bottom')
        canvasvar=FigureCanvas(figBar,master=self.w)
        canvasvar.draw()
        canvasvar.get_tk_widget().place(anchor=CENTER,x=500,y=400)
#Suma el numero de ventas con cada proteina 
    def GetProt(self):
        resultS=[0,0,0,0]
        for child in self.tabladata.get_children():
            proteina = self.tabladata.item(child, "values")[1]
            #['Res','Pollo','Mariscos', 'Cerdo']

            if self.combProteina[0]==proteina:
                resultS[0]+=int(self.tabladata.item(child, "values")[2])+int(self.tabladata.item(child, "values")[3])+int(self.tabladata.item(child, "values")[4])
            elif self.combProteina[1]==proteina:
                 resultS[1]+=int(self.tabladata.item(child, "values")[2])+int(self.tabladata.item(child, "values")[3])+int(self.tabladata.item(child, "values")[4])
            elif self.combProteina[2]==proteina:
                resultS[2]+=int(self.tabladata.item(child, "values")[2])+int(self.tabladata.item(child, "values")[3])+int(self.tabladata.item(child, "values")[4])
            elif self.combProteina[3]==proteina:
                resultS[3]+=int(self.tabladata.item(child, "values")[2])+int(self.tabladata.item(child, "values")[3])+int(self.tabladata.item(child, "values")[4])               
        print("======================================\n")
        print(resultS)
        print("======================================\n")
        return resultS
    def clearAll(self):
        pass
    
    def mostrarDatos(self,where=""):
        registro=self.tabladata.get_children()
        for registro in registro:
            self.tabladata.delete(registro)
        if len(where)>0:
            cur=self.conn.consultaBD("SELECT id, Nombre, proteina, tipo1, tipo2, tipo3, fecha FROM Pensionado.almuerzos " + where + " ORDER BY id")
        else:
            cur=self.conn.consultaBD("SELECT id, Nombre, proteina, tipo1, tipo2, tipo3, fecha FROM Pensionado.almuerzos ORDER BY id")
        for (id, Nombre, proteina, tipo1, tipo2, tipo3, fecha) in cur:
            self.tabladata.insert('',0,text=id,values=[Nombre, proteina, tipo1, tipo2, tipo3, fecha])    