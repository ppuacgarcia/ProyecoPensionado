from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvas
class Ventas:
    def __init__(self,ventanaPrincipal):
        table = ttk.Treeview(ventanaPrincipal)
        table['columns'] = ('player_id', 'player_name', 'player_Rank', 'player_states', 'player_city')
        table.column("#0", width=0,  stretch=NO)
        table.column("player_id",anchor=CENTER, width=80)
        table.column("player_name",anchor=CENTER,width=80)
        table.column("player_Rank",anchor=CENTER,width=80)
        table.column("player_states",anchor=CENTER,width=80)
        table.column("player_city",anchor=CENTER,width=80)

        table.heading("#0",text="",anchor=CENTER)
        table.heading("player_id",text="Id",anchor=CENTER)
        table.heading("player_name",text="Name",anchor=CENTER)
        table.heading("player_Rank",text="Rank",anchor=CENTER)
        table.heading("player_states",text="States",anchor=CENTER)
        table.heading("player_city",text="States",anchor=CENTER)
        table.pack()
        


       
      
