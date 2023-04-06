from tkinter import *
from PIL import Image, ImageTk
#import de clases Ventas Pensionistas y Hospedaje
from Ventas import *
from Pensionistas import *
from Hospedaje import *
def MenP(pw):
    bgcolor='#3F5657'
    hiColor='#65A0A3'
    fMenuP = Frame(pw,width=1200,height=675,bg=bgcolor)
    fMenuP.place(x=0, y=0)
    #comando que entra a ventas
    def cmdVentas():
       Ventas(pw)
       fMenuP.destroy() 
       fMenuP.pack_forget()
       fMenuP.grid_forget()
    #comando para entrar a Hospedaje
    def cmdHospedaje():
       Pensionistas(pw)
       fMenuP.destroy() 
    #Comando para entrar a Pensionistas
    def cmdPensionistas():
        Hospedaje(pw)
        fMenuP.destroy()     
    def btnmenu(pw, x, y, text, bcolor, fcolor, command, font, siz, tipe):
        #Botones para menu
        def on_enter(e):
            buttons['background'] = bcolor
            buttons['foreground'] = fcolor
        def on_leave(e):
            buttons['background'] = fcolor
            buttons['foreground'] = bcolor    
        buttons = Button(pw, width=100, height=2, text= text, 
                         fg  = bcolor, bg=fcolor, command=command, 
                         border=0, activebackground=bcolor, activeforeground=fcolor,font=(font, siz, tipe))
        buttons.bind("<Enter>", on_enter)
        buttons.bind("<Leave>", on_leave)
        buttons.place(x=600, y=y,anchor='center')
    #Label 'menu'
    Label(fMenuP, text='Menú',bg=bgcolor,fg='#FFFFFF', font=('Arial', 42,'bold') ).place(x=525,y=10)
    #Boton Ventas
    btnmenu(fMenuP, 400, 150, 'Ventas', hiColor, bgcolor, cmdVentas,'Arial', 16,'bold',)
    #Boton Pensionistas
    btnmenu(fMenuP, 400, 213, 'Pensionistas', hiColor, bgcolor, cmdHospedaje,'Arial', 16,'bold', )
    #Boton Hospedaje
    btnmenu(fMenuP, 400, 276, 'Hospedaje', hiColor,bgcolor, cmdPensionistas,'Arial', 16,'bold',)
   
