from tkinter import *
from PIL import Image, ImageTk

def MenP(pw):
    bgcolor='#3F5657'
    hiColor='#65A0A3'
    fMenuP = Frame(pw,width=1200,height=675,bg=bgcolor)
    fMenuP.place(x=0, y=0)
    
    def cmd1():
        print("print hola")
       # AdolForm(pw).mostrarDatos()
        
    def cmd2():
        print("print hola")
       # ColForm(pw).mostrarDatos()

    def cmd3():
        print("print hola")
        #EvtForm(pw).mostrarDatos()
        
    def cmd4():
        print("print hola")
        #adolinfo(pw).mostrarDatos()
        
    def cmd5():
        print("print hola")
        #colabinfo(pw).mostrarDatos()
        
    def btnmenu(pw, x, y, text, bcolor, fcolor, command, font, siz, tipe):
        #Botones para menu
        def on_enter(e):
            buttons['background'] = bcolor
            buttons['foreground'] = fcolor
            
        def on_leave(e):
            buttons['background'] = fcolor
            buttons['foreground'] = bcolor
            
            
        buttons = Button(pw, width=30, height=2, text= text, fg  = bcolor, bg=fcolor, command=command, border=0, activebackground=bcolor, activeforeground=fcolor,font=(font, siz, tipe))
        buttons.bind("<Enter>", on_enter)
        buttons.bind("<Leave>", on_leave)
        buttons.place(x=x, y=y)
        
    Label(fMenuP, text='Menú',bg=bgcolor,fg='#FFFFFF', font=('Arial', 42,'bold') ).place(x=525,y=10)
    btnmenu(fMenuP, 400, 150, 'Ventas', hiColor, '#FFFFFF', cmd1,'Arial', 16,'bold',)
    btnmenu(fMenuP, 400, 250, 'Pensionistas', hiColor, '#FFFFFF', cmd2,'Arial', 16,'bold', )
    btnmenu(fMenuP, 400, 350, 'Hospedaje', hiColor, '#FFFFFF', cmd3,'Arial', 16,'bold',)
   
