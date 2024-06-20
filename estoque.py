from customtkinter import *
from tkinter import messagebox, LabelFrame, ttk
import os
import sqlite3


root = CTk()

WIDTH = 1440 
HEIGHT = 768

root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('ESTOQUE -  ADMIN')

## Variaveis

# VARIAVEIS
product = StringVar()
category_values = list()

productId_Form = StringVar(value=0)
productName_Form = StringVar()
stock_Form = StringVar(value=0)
price_Form = StringVar(value=0.0)



# FUNÇÕES
def loadTable():
    table.delete(*table.get_children())
    try:
        conn = sqlite3.Connection('stock.db')
        cur = conn.cursor()
        cur.execute('SELECT id, product_name, price, quantity FROM product')
        row = cur.fetchall()

        for i in row:
            table.insert('', END, text=i[0], values=(i[1], i[2], i[3]), tags='product')

    except:
        messagebox.showerror('BD ERRO', 'Banco de Dados não encontrado')

    finally:
        product.set('')
        productId_Form.set('')
        productName_Form.set('') 
        stock_Form.set('')
        price_Form.set('')
        conn.close()


def insertProduct():
    if productId_Form.get() != '' and productName_Form.get() != '' and stock_Form.get() != '' and price_Form.get() != '' and stock_Form.get().isnumeric() and price_Form.get().isnumeric():
            try:
                conn = sqlite3.Connection('stock.db')
                cur = conn.cursor()

                cur.execute('INSERT INTO product(id, product_name, price, quantity) VALUES (?,?,?,?)', (productId_Form.get(), productName_Form.get(), price_Form.get(), stock_Form.get()))
                conn.commit()
                messagebox.showinfo('Produto', 'O produto foi salvo')
            except Exception as e:
                print(e)
                messagebox.showerror('BD ERROR', 'Não foi possivel adicionar o PRODUTO no ESTOQUE!')
        
            finally:
                conn.close()
                loadTable()
    else:
        messagebox.showerror('CAMPO VAZIOS', 'Há Algum Campo com valor VAZIO ou ERRADO')

def updateProduct():
    if productId_Form.get() != '' and productName_Form.get() != '' and stock_Form.get() != '' and price_Form.get() != '' and stock_Form.get() != '' and price_Form.get() != '':
            try:
                conn = sqlite3.Connection('stock.db')
                cur = conn.cursor()

                price = float(price_Form.get())
                stock = int(stock_Form.get())

                cur.execute('UPDATE product SET product_name=?, price = ?, quantity = ? WHERE id = ?', (productName_Form.get(), price, stock, productId_Form.get( )))
                conn.commit()
                messagebox.showinfo('Produto', 'O produto foi atualizado')
            except Exception as e:
                print(e)
                messagebox.showerror('BD ERROR', 'Não foi possivel adicionar o PRODUTO no ESTOQUE!')
        
            finally:
                conn.close()
                loadTable()
    else:
        messagebox.showerror('Erro', 'Não foi possível atualizar o PRODUTO')


def deleteProduct():
        if productId_Form.get() != '':
            try:
                conn = sqlite3.Connection('stock.db')
                cur = conn.cursor()
                cur.execute('DELETE FROM product WHERE id=?', (productId_Form.get(), ))
                print('CU')
                conn.commit()
                messagebox.showinfo('Produto', 'O produto foi deletado')
            except Exception as e:
                print(e)
                messagebox.showerror('BD ERROR', 'Não foi possivel DELETAR o PRODUTO no ESTOQUE!')
        
            finally:
                conn.close()
                loadTable()
        else:
            messagebox.showerror('Erro', 'Não foi possível deletar o PRODUTO')

    
def search():
    query = product.get()
    selections = []
    for child in table.get_children():
        data = table.item(child)
        try: 
            if data and query.lower() in str(data['text']).lower():
                selections.append(data)

        except Exception as e:
          
            print(e)

    print(selections)
    table.delete(*table.get_children())
    for item in selections:
        table.insert('', END, text=item['text'], values=(item['values'][0], item['values'][1], item['values'][2]), tags='product')





def close_window():
    root.destroy()


# DESIGNER
title = CTkLabel(root, text='PRODUTOS -  ADMIN', width=200)
title.pack(fill=X)

F1 = LabelFrame(root, text='', font=(
    'poppins', 18, 'bold'), bg='#2f2f2f')
F1.place(x=0, y=80, relwidth=1)

product_lb = CTkLabel(F1, text='Produto', font=(
    'poppins', 18, 'bold'), width=200, height=45)
product_lb.grid(row=0, column=0, columnspan=2, pady=5)

product_entry = CTkEntry(F1, placeholder_text='Produto', font=(
    'poppins', 18, 'bold'), width=200, height=45, textvariable=product)
product_entry.grid(row=0, column=2, columnspan=1)

category_lb = CTkLabel(F1, text='Categoria', font=(
    'poppins', 18, 'bold'), width=200, height=45)
category_lb.grid(row=0, column=3, columnspan=2)

category_select = CTkComboBox(F1, width=200, height=45,
                          corner_radius=5, values=(category_values))
category_select.grid(row=0, column=5, columnspan=1)

divider = LabelFrame(F1, text='', width=200, height=0)
divider.grid(row=0, column=7, padx=30 )

bt_clear = CTkButton(F1, text='Limpar', width=200,
                      height=45, command=loadTable)
bt_clear.grid(row=0, column=8, padx=5)

bt_search = CTkButton(F1, text='Pequisar', width=200,
                      height=45, command=search)
bt_search.grid(row=0, column=9, padx=5)


# PAINEL DE COMANDOS
F2 = LabelFrame(root, text='', font=(
    'serif', 14, 'bold'), bg='#2f2f2f')
F2.place(x=10, y=190, relwidth=0.38, relheight=.75)

divider = CTkLabel(F2, text='', width=200,)
divider.grid(row=0, column=0, pady=50)



idProductForm_lb = CTkLabel(F2, text='Cód. Produto')
idProductForm_entry = CTkEntry(F2, width=200, height=45, placeholder_text='12345678',  textvariable=productId_Form)

idProductForm_lb.grid(row=1, column=0, pady=5)
idProductForm_entry.grid(row=1, column=1, padx=16, pady=5)



nameProductForm_lb = CTkLabel(F2, text='Nome')
nameProductForm_entry = CTkEntry(F2, width=200, height=45, placeholder_text='Nome', text_color='white', textvariable=productName_Form)

nameProductForm_lb.grid(row=2, column=0, pady=5)
nameProductForm_entry.grid(row=2, column=1, padx=16, pady=5)



priceProductForm_lb = CTkLabel(F2, text='Preço')
priceProductForm_entry = CTkEntry(F2, width=200, height=45, placeholder_text='0', textvariable=price_Form)

priceProductForm_lb.grid(row=3, column=0, pady=5)
priceProductForm_entry.grid(row=3, column=1, padx=16, pady=5)



stockProductForm_lb = CTkLabel(F2, text='Estoque')
stockProductForm_entry = CTkEntry(F2, width=200, height=45, placeholder_text='0', textvariable=stock_Form)

stockProductForm_lb.grid(row=4, column=0, pady=5)
stockProductForm_entry.grid(row=4, column=1, padx=16, pady=5)






########################################################

divider = CTkLabel(F2, text='', width=200,)
divider.grid(row=5, column=0, pady=35)


bt_insert = CTkButton(F2, text='Inserir', height=45,
                      font=('poppins', 14), command=insertProduct)
bt_insert.grid(row=6, column=0, padx=60, pady=5)

bt_update = CTkButton(F2, text='Atualizar', height=45, font=('poppins', 14), command=updateProduct)
bt_update.grid(row=6, column=1, padx=5, pady=5)

bt_delete = CTkButton(F2, text='Deletar', height=45, font=('poppins', 14), command=deleteProduct)
bt_delete.grid(row=7, column=0, padx=5, pady=5)

bt_exit = CTkButton(F2, text='Sair', height=45, font=('poppins', 14), command=close_window)
bt_exit.grid(row=7, column=1, padx=5, pady=5)


# TABELA DE USUÁRIOS

# FUNCÕES DA TABELA

def item_selected(_):
   row = table.item(table.selection())
   print(row)
   productId_Form.set(row['text'])
   productName_Form.set(row['values'][0])
   price_Form.set(row['values'][1])
   stock_Form.set(row['values'][2])


# DESIGNER DA TABELA
F3 = LabelFrame(root, text='', font=(
    'serif', 14, 'bold'), fg='#2f2f2f', bg='#125ff0')
F3.place(x=710, y=190, relwidth=0.6, relheight=.75)


table = ttk.Treeview(F3, columns=["Produto",'Quantidade','Preco'])

table.heading('#0', text='ID')
table.heading('Produto', text='Produto')
table.heading('Quantidade', text='Quantidade')
table.heading('Preco', text='Preço')

table.tag_bind("product", "<<TreeviewSelect>>", item_selected)

loadTable()

table.pack(expand=True, fill=BOTH, padx=10, pady=10)


root.mainloop()