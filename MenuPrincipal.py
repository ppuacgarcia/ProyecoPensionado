from tkinter import *
from PIL import Image, ImageTk
#import de clases Ventas Pensionistas y Hospedaje
from Ventas import *
from Pensionistas import *
from Hospedaje import *
class MenP:
    def __init__(self,pw):
        bgcolor='#3F5657'
        hiColor='#65A0A3'
        self.fMenuP = Frame(pw,width=1200,height=675,bg=bgcolor)
        self.fMenuP.place(x=0, y=0)
        #comando que entra a ventas
         #Label 'menu'
        Label(self.fMenuP, text='Menú',bg=bgcolor,fg='#FFFFFF', font=('Arial', 42,'bold') ).place(x=525,y=10)
        #Boton Ventas
        self.btnmenu(self.fMenuP, 400, 150, 'Ventas', hiColor, bgcolor, self.cmdVentas,'Arial', 16,'bold',)
        #Boton Pensionistas
        self.btnmenu(self.fMenuP, 400, 213, 'Pensionistas', hiColor, bgcolor, self.cmdHospedaje,'Arial', 16,'bold', )
        #Boton Hospedaje
        self.btnmenu(self.fMenuP, 400, 276, 'Hospedaje', hiColor,bgcolor, self.cmdPensionistas,'Arial', 16,'bold',)
    def cmdVentas(self):
       Ventas(self.fMenuP)
       self.pw.destroy() 
    #comando para entrar a Hospedaje
    def cmdHospedaje(self):
       Pensionistas(self.fMenuP)
       self.pw.destroy() 
    #Comando para entrar a Pensionistas
    def cmdPensionistas(self):
        Hospedaje(self.fMenuP)
        self.pw.destroy()     
    def btnmenu(self,fMenuP, x, y, text, bcolor, fcolor, command, font, siz, tipe):
        #Botones para menu
        def on_enter(e):
            buttons['background'] = bcolor
            buttons['foreground'] = fcolor
        def on_leave(e):
            buttons['background'] = fcolor
            buttons['foreground'] = bcolor    
        buttons = Button(fMenuP, width=100, height=2, text= text, 
                         fg  = bcolor, bg=fcolor, command=command, 
                         border=0, activebackground=bcolor, activeforeground=fcolor,font=(font, siz, tipe))
        buttons.bind("<Enter>", on_enter)
        buttons.bind("<Leave>", on_leave)
        buttons.place(x=600, y=y,anchor='center')
   
   
