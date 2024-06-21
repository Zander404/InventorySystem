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
def admin():
    root.withdraw()
    os.system('python login_admin.py')
    root.deiconify()

def caixa():
    root.withdraw()
    os.system('python login_cashier.py ')
    root.deiconify()



## INTERFACE

F1 = CTkFrame(root, width=WIDTH, height=HEIGHT, fg_color='#2f2f2f')
F1.pack(expand=True, fill=BOTH)


title = CTkLabel(F1, text='LOJA', width=200)
title.pack(expand=True, fill=X, pady=0.5 )

F2 = CTkFrame(F1, width=600, fg_color='#2a2a2a')
F2.pack(fill=X, expand=True)

bt_admin = CTkButton(F2, text='ADMIN', width=200, height=45, command=admin)
bt_caixa = CTkButton(F2, text='CAIXA', width=200, height=45, command=caixa)
# print(get_username())

bt_admin.place(relx=.07, rely=0.5)

bt_caixa.place(relx=.8, rely=0.5)

root.mainloop()