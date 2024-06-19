from customtkinter import *
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk


root = CTk()
root.geometry('1366x768')
root.title('CONTROLE DE ADMIN')

WIDTH = '1366'
HEIGHT = '768'


def Exit(top):
    top.destroy()
    root.deiconify()


class Painel:
   
    def __init__(self, top: CTkToplevel=None):
        top.geometry(f'{WIDTH}x{HEIGHT}')
        top.title('MAIN CONTROL')

        self.controlesFrame = CTkFrame(top, height=200)

        self.logo = CTkImage(Image.open('./assets/logo.png'), size=(1366, 200))
        top.configure(image=self.logo)


        self.btn1 = CTkButton(self.controlesFrame, text='Produto', width=250,
                         height=100, command=lambda:product())
        self.btn2 = CTkButton(self.controlesFrame, text='Usuário',
                         width=250, height=100, command=lambda:user())
        self.btn3 = CTkButton(self.controlesFrame, text='Notas Fiscais',
                         width=250, height=100, command=lambda:invoice())
        self.btn4 = CTkButton(self.controlesFrame, text='Controle4',
                         width=250, height=100)

        self.controlesFrame.rowconfigure(1, weight=2)
        self.controlesFrame.columnconfigure(0, weight=0)

        self.title = CTkLabel(top, text='Login ADMIN')

        self.btn1.grid(row=0, column=1, padx=10)
        self.btn2.grid(row=0, column=2, padx=10)
        self.btn3.grid(row=0, column=3, padx=10)
        self.btn4.grid(row=0, column=4, padx=10)

        # logo_frame.pack(expand=True, padx=10, pady=10)
        self.title.pack(expand=True, padx=10, pady=10)
        self.controlesFrame.pack(expand=True, padx=10, pady=10)

        top.mainloop()

class Product:

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=inv)
        if sure == True:
            inv.destroy()
            adm.deiconify()

    def __init__(self, top=None):
        top.geometry('1366x768')
        title = CTkLabel(top, text='PRODUTOS')
        teste_btn = CTkButton(top, text='Teste', command=lambda:self.Exit())

        title.pack()
        teste_btn.pack()

        top.mainloop()


class Login_page:

    def login(self):
        root.withdraw()
        global adm
        global page1
        adm = CTkToplevel()
        page1 = Painel(adm)
        adm.mainloop()
        

    def __init__(self, top=None):
        top.geometry(f'{WIDTH}x{HEIGHT}')
        title = CTkLabel(top, text='Login')
        teste_btn = CTkButton(top, text='Teste', command=lambda:self.login())

        title.pack()
        teste_btn.pack()

        top.mainloop()



class User:

    def __init__(self, top=None):
        top.geometry(f'{WIDTH}x{HEIGHT}')
        title = CTkLabel(top, text='User')
        teste_btn = CTkButton(top, text='Teste', command=lambda:self.Exit())

        title.pack()
        teste_btn.pack()

        top.mainloop()

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=inv)
        if sure == True:
            inv.destroy()
            adm.deiconify()




class Invoice:
  
    def __init__(self, top=None):
        top.geometry(f'{WIDTH}x{HEIGHT}')
        title = CTkLabel(top, text='INVOICE')
        teste_btn = CTkButton(top, text='Teste', command=lambda:self.Exit())

        title.pack()
        teste_btn.pack()

        top.mainloop()

    def Exit(self):
        sure = messagebox.askyesno("Exit","Are you sure you want to exit?", parent=self)
        if sure == True:
            self.destroy()
            adm.deiconify()




def product():
    adm.withdraw()
    global inv
    global page2

    inv = CTkToplevel()
    page2 = Product(inv)
    inv.protocol('WM_DELETE_WINDOW', Exit(inv))
    inv.mainloop()

    

def user():
    adm.withdraw()
    global user
    global page3

    user = CTkToplevel()
    page3 = User(user)
    user.protocol('WM_DELETE_WINDOW', Exit(inv))
    user.mainloop()

    

def invoice():
    adm.withdraw()
    global invoice
    global page4

    invoice = CTkToplevel()
    page4 = Invoice(invoice)
    invoice.protocol('WM_DELETE_WINDOW', Exit(inv))
    invoice.mainloop()

    





# page1 = Login_page(root)

page2 = User(root)

# page3 = Invoice(root)

# page4 = Painel(root)