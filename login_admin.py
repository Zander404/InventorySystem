from customtkinter import *
from tkinter import messagebox
import sqlite3
import os

WIDTH = 1440
HEIGHT = 768
bg_color='#7b7b7b'

root = CTk()
root.title('LOGIN DE ADMINISTAÇÃO')
root.geometry(f'{WIDTH}x{HEIGHT}')

username = StringVar()
password = StringVar()

conn = sqlite3.Connection('stock.db') 
cursor = conn.cursor()

def authentic():
    if username.get() == '' or password.get() == '':
        messagebox.showerror('ERRO', 'USUÁRIO ou SENHA está em BRANCO!')

    else:
       try:
        cursor.execute('SELECT * FROM user WHERE username=? AND password=?', (username.get(), password.get()))
        row = cursor.fetchone()
        if row and row[3] == 'ADMIN':
            messagebox.showinfo('SUCESSO', 'LOGIN EFETUADO!')
            root.withdraw()
            os.system('python admin.py')
            root.deiconify()
        else:
           raise Exception('Usuario Inválido')
       except:
          messagebox.showerror('ERRO', 'Usuário Inválido!')


F1 = CTkFrame(root, width=WIDTH, height=HEIGHT)
# F1.place(relx=.45, rely=.5)
F1.pack(expand=True, anchor='c', )

title= CTkLabel(F1, width=200, text='LOGIN')
title.grid(row=0, column=0, columnspan=2, pady=40)

username_lb= CTkLabel(F1, text='Usuário')
username_lb.grid(row=1, column=0, padx=10, pady=5)

username_entry = CTkEntry(F1, width=200, textvariable=username)
username_entry.grid(row=1, column=1, padx=10, pady=5)

password_lb= CTkLabel(F1, text='Senha')
password_lb.grid(row=2, column=0, padx=10, pady=5)

password_entry = CTkEntry(F1, width=200, show='*', textvariable=password)
password_entry.grid(row=2, column=1, padx=10, pady=5)


btn_Login = CTkButton(F1, width=200, text='Login', command=authentic)
btn_Login.grid(row=3, column=0, columnspan=2, rowspan=2, pady=40)



# Login()
root.mainloop()


