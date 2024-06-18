from customtkinter import *
from tkinter import messagebox, PhotoImage
import os
from PIL import Image, ImageTk


main = CTk()



main.geometry('1366x768')
main.title('Comercio - Main')
main.resizable(False, False)


def cashier():
    main.withdraw()
    os.system('python cashier.py ')
    main.deiconify()


def admin():
    main.withdraw()
    os.system('python admin.py')
    main.deiconify()


title = CTkLabel(main, width=1366, height=76, text='SELECIONE O USUÁRIO', font=('Poppins',24))

admin_btn = CTkButton(main, text='Admin', width=220, height=45, command=admin)
cashier_btn = CTkButton(main, text='Caixa', width=220, height=45, command=cashier)




title.place(relx=0, rely=0)
admin_btn.place(relx=.2, rely=.6)
cashier_btn.place(relx=.6, rely=.6)

main.mainloop()
