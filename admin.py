from customtkinter import *
from tkinter import messagebox
import tkinter
from PIL import Image, ImageTk


root = CTk()
root.geometry('1366x768')
root.title('CONTROLE DE ADMIN')

WEIGHT = '1366'
HEIGHT = '768'


def Exit(top):
    top.destroy()
    root.deiconify()


class Painel:
   
    def __init__(self, top: CTkToplevel=None):
        top.geometry(f'{WEIGHT}x{HEIGHT}')
        top.title('MAIN CONTROL')

        frames = {'info': None, "produto": None,
            "pedido": None, 'usuario': None}

        controlesFrame = CTkFrame(top, height=200)

        logo = CTkImage(Image.open('./assets/logo.png'), size=(1366, 200))
        top.configure(image=logo)


        btn1 = CTkButton(controlesFrame, text='Controle1', width=250,
                         height=100, command=lambda:Exit(top))
        btn2 = CTkButton(controlesFrame, text='Controle2',
                         width=250, height=100)
        btn3 = CTkButton(controlesFrame, text='Controle3',
                         width=250, height=100)
        btn4 = CTkButton(controlesFrame, text='Controle4',
                         width=250, height=100)

        controlesFrame.rowconfigure(1, weight=2)
        controlesFrame.columnconfigure(0, weight=0)

        title = CTkLabel(top, text='Login ADMIN')

        btn1.grid(row=0, column=1, padx=10)
        btn2.grid(row=0, column=2, padx=10)
        btn3.grid(row=0, column=3, padx=10)
        btn4.grid(row=0, column=4, padx=10)

        # logo_frame.pack(expand=True, padx=10, pady=10)
        title.pack(expand=True, padx=10, pady=10)
        controlesFrame.pack(expand=True, padx=10, pady=10)

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
        top.geometry('1920x1400')
        title = CTkLabel(top, text='Login')
        teste_btn = CTkButton(top, text='Teste', command=lambda:self.login())

        title.pack()
        teste_btn.pack()

        top.mainloop()








page1 = Login_page(root)