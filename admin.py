from customtkinter import *
from tkinter import messagebox, LabelFrame
import os 
# from login_admin import get_username


root = CTk()

WIDTH = 1440 
HEIGHT = 768

root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('PAINEL DE CONTROLE -  ADMIN')


## Variables



## Function
def estoque():
    root.withdraw()
    os.system('python estoque.py ')
    root.deiconify()

def notas():
    root.withdraw()
    os.system('python notas.py ')
    root.deiconify()

def usuario():
    root.withdraw()
    os.system('python usuario.py ')
    root.deiconify()



## INTERFACE

F1 = CTkFrame(root, width=WIDTH, height=HEIGHT, fg_color='#2f2f2f')
F1.pack(expand=True, fill=BOTH)


title = CTkLabel(F1, text='PAINEL DE CONTROLE -  ADMIN', width=200)
title.pack(expand=True, fill=X, pady=0.5 )

F2 = CTkFrame(F1, width=600, fg_color='#2a2a2a')
F2.pack(fill=X, expand=True)

bt_estoque = CTkButton(F2, text='ESTOQUE', width=200, height=45, command=estoque)
bt_notas = CTkButton(F2, text='NOTAS', width=200, height=45, command=notas)
bt_usuario = CTkButton(F2, text='USUÁRIOS', width=200, height=45, command=usuario)
# print(get_username())

bt_estoque.place(relx=.07, rely=0.5)
bt_notas.place(relx=.44, rely=0.5)
bt_usuario.place(relx=.8, rely=0.5)

root.mainloop()