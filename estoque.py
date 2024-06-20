from customtkinter import *
from tkinter import messagebox
import os


root = CTk()

WIDTH = 1440 
HEIGHT = 768

root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('ESTOQUE -  ADMIN')


F1 = CTkFrame(root, width=WIDTH, height=HEIGHT, fg_color='#2f2f2f')
F1.pack(expand=True, fill=BOTH)


title = CTkLabel(F1, text='ESTOQUE -  ADMIN', width=200)
title.pack(expand=True, fill=X, pady=0.5 )

F2 = CTkFrame(F1, width=600, fg_color='#2a2a2a')
F2.pack(fill=X, expand=True)






root.mainloop()