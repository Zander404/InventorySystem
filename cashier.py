from customtkinter import *
from tkinter import messagebox, PhotoImage, LabelFrame, Frame
import os
from PIL import Image, ImageTk
import random
import sqlite3

root = CTk()



root.geometry('1280x720')
root.title('Comercio')
root.resizable(False, False)
bg_color = '#2f2f2f'

## VARIABLE 

c_name=StringVar()
c_phone = StringVar()

Item=StringVar()
Rate=IntVar( )
Quantity=IntVar()
search_code = StringVar()

bill_no = StringVar()
x=random.randint(1000, 9999)
bill_no.set(str(x))
global l, proutos
l = list()
produtos = list()
product_name = list()



def get_produtos():
    conn = sqlite3.Connection('stock.db')
    cur = conn.cursor()

    cur.execute('SELECT * FROM product')
    row = cur.fetchall()

    for product_item in row:
        produtos.append(product_item)
        product_name.append(product_item[1])
        

def product_info(_):
    for index, item in enumerate(produtos):
        if  itm_txt.get() == item[1]:
            Item.set(itm_txt.get())
            Rate.set(produtos[index][2])
            return
        

def search():
    # print(code)
    print(search_code.get())

    try:
        conn = sqlite3.Connection('stock.db')
        cur = conn.cursor()

        cur.execute('SELECT * FROM product WHERE id=?', (search_code.get(),))
        row = cur.fetchone()
        print(row)
        Item.set(row[1])
        Rate.set(row[2])

    except Exception as e:
        print(e)

    finally:
        search_code.set('')
        conn.close()




### FUNCTION
def welcome():
    textarea.delete(1.0, END)
    textarea.insert(END, '\t WELCOME COMMERCE RETAILS')
    textarea.insert(END, f'\n\nBill Number: \t\t{bill_no.get()}')
    textarea.insert(END, f'\nCustomer Name:\t\t{c_name.get()}')
    textarea.insert(END, f'\nPhone Number:\t\t{c_phone.get()}')
    textarea.insert(END, f'\n=======================================================')
    textarea.insert(END, f'\nProduct\t\t\tQTY \t\t\tPrice')
    textarea.insert(END, f'\n=======================================================')

    textarea.configure(font=('arial', 15, 'bold'))


def additem():
    n=Rate.get()
    m=Quantity.get()*n
    l.append(m)

    if Item.get() == '':
        messagebox.showerror('Error', message='Please Enter the item')
    else:
        textarea.insert((10.0+ float(len(l)-1)), f'\n {Item.get()}\t\t\t {Quantity.get()} \t\t\t{m}')



def gbill():
    if c_name.get() == '' or c_phone.get() == '':
        messagebox.showerror('ERROR', 'Customer Details are must ')
    else:
        text=textarea.get(10.0,(10.0+float(len(l))))
        welcome()
        textarea.insert(END, text)
        textarea.insert(END, f'\n=======================================================')
        textarea.insert(END, f'\nTotal Paybill Amount: \t\t\t {sum(l)}')
        textarea.insert(END, f'\n=======================================================\n')
        savebill()


def savebill():
    op=messagebox.askyesno('Save bill', 'Do You waint to save the bill')
    if op>0:
        bill_details=textarea.get(1.0, END)
        f1=open('bills/'+str(bill_no.get())+'.txt', 'w')
        f1.write(bill_details)
        f1.close()
        messagebox.showinfo('SAVED', f'Bill no: {bill_no.get()} Saved succesfully')
        textarea.delete(0.0, END)
        

    else:
        return

def clear():
    global l
    l.clear()
    c_name.set('')
    c_phone.set('')
    Item.set('')
    Rate.set(0)
    Quantity.set(0)
    welcome()

def exitt():
    op=messagebox.askyesno('EXIT', 'Do you really wanto to exit')

#========================================
get_produtos()
# TOP SECTION
title=CTkLabel(root, text='Billing Software', bg_color=bg_color, font=('times new romman', 25, 'bold') )
title.pack(fill='x')


#CUSTOMER DETAIL

F1=LabelFrame(root, text='Customer', font=('times new roman', 18, 'bold'), bg=bg_color, fg='gold', )
F1.place(x=0, y=80, relwidth=1)

cname_lbl = CTkLabel(F1, text='Customer Name', corner_radius=10, font=('times new roman', 18, 'bold'))
cname_txt = CTkEntry(F1, width=150, font=('arial', 15, 'bold'),textvariable=c_name )

cname_lbl.grid(row=0, column=0, ipadx=10, padx=10, pady=5)
cname_txt.grid(row=0, column=1, padx=16, pady=5)


cphone_lbl = CTkLabel(F1, text='Phone Number', corner_radius=10, font=('times new roman', 18, 'bold'))
cphone_txt = CTkEntry(F1, width=150, font=('arial', 15, 'bold'), textvariable=c_phone)

cphone_lbl.grid(row=0, column=2, ipadx=10, padx=10, pady=5)
cphone_txt.grid(row=0, column=3, padx=16, pady=5)

## Product Details

F2 = LabelFrame(root, text='Produtos Detail', font=('times new roman', 18, 'bold'), bd=10, bg=bg_color, fg='gold', relief=GROOVE)
F2.place(x=20, y=180, width=630, height=600)

### Produto
search_code_txt = CTkLabel(F2, text='Código do Produto', font=('times new roman', 18, 'bold'), text_color='green')
search_code_txt.grid(row=0, column=0, padx=30, pady=20)

search_code_entry=CTkEntry(F2,width=200, font=('arial', 15, 'bold'), textvariable=search_code, validate='focusout', validatecommand=(search))
search_code_entry.grid(row=0, column=1, padx=10, pady=20)

itm = CTkLabel(F2, text='Product Name', font=('times new roman', 18, 'bold'), text_color='green')
itm.grid(row=1, column=0, padx=30, pady=20)

itm_txt=CTkComboBox(F2,width=200, font=('arial', 15, 'bold'), values=(product_name), command=product_info)
itm_txt.grid(row=1, column=1, padx=10, pady=20)

## Rate
rate = CTkLabel(F2, text='Product Rate', font=('times new roman', 18, 'bold'), text_color='green')
rate.grid(row=2, column=0, padx=30, pady=20)

rate_txt=CTkEntry(F2,width=200, font=('arial', 15, 'bold'), textvariable=Rate, state='readonly')
rate_txt.grid(row=2, column=1, padx=10, pady=20)

## QUANTIDADE
quantity = CTkLabel(F2, text='Product Quantity', font=('times new roman', 18, 'bold'), text_color='green')
quantity.grid(row=3, column=0, padx=30, pady=20)

quantity_txt=CTkEntry(F2,width=200, font=('arial', 15, 'bold'), textvariable=Quantity)
quantity_txt.grid(row=3, column=1, padx=10, pady=20)


## BOTÃO

btn1= CTkButton(F2, text='Add Item', font=('arial', 15, 'bold'), text_color='lime', command=lambda:additem())
btn1.grid(row=4, column=0, padx=5, pady=30)

btn2= CTkButton(F2, text='Generate Bill', font=('arial', 15, 'bold'), text_color='lime', command=lambda:gbill())
btn2.grid(row=4, column=1, padx=5, pady=30)

btn3= CTkButton(F2, text='Clear', font=('arial', 15, 'bold'), text_color='lime', command=lambda:clear())
btn3.grid(row=5, column=0, padx=5, pady=30)

btn4= CTkButton(F2, text='Exit', font=('arial', 15, 'bold'), text_color='lime', command=lambda:exitt())
btn4.grid(row=5, column=1, padx=5, pady=30)


## BILL
F3 = CTkFrame(root, border_width=5, width=800, height=500, border_color='green')
F3.place(x=700, y=150, )

bill_title = CTkLabel(F3, text='Bill Area', font=('arial', 15, 'bold')).pack(fill='x')
scroll_y =CTkScrollbar(F3, orientation=VERTICAL)
textarea=CTkTextbox(F3, yscrollcommand=scroll_y, width=500, height=500)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_y.configure(command=textarea.yview)

textarea.pack(fill=BOTH)

welcome()

root.mainloop()