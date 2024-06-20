from customtkinter import *
from tkinter import messagebox, LabelFrame, ttk
import os
import sqlite3

WIDTH = 1440
HEIGHT = 768

root = CTk()
set_appearance_mode('dark')
set_default_color_theme('dark-blue')

root.geometry(f'{WIDTH}x{HEIGHT}')
root.title('USUÁRIOS -  ADMIN')
root.resizable(False, False)


# VARIAVEIS
username = StringVar()
role = StringVar()

id_Form = IntVar()
username_Form = StringVar()
password_Form = StringVar()
role_Form = StringVar()


# FUNÇÕES
def loadTable():
    table.delete(*table.get_children())
    try:
        conn = sqlite3.Connection('stock.db')
        cur = conn.cursor()
        cur.execute('SELECT id, username, role FROM user')
        row = cur.fetchall()

        for index, i in enumerate(row):
            table.insert('', END, text=index+1, values=(i[1], i[2]), tags='user')

    except:
        messagebox.showerror('BD ERRO', 'Banco de Dados não encontrado')

    finally:
        username.set('')
        role.set('')
        id_Form.set('')
        username_Form.set('') 
        password_Form.set('')
        conn.close()


def insertUser():

    confirm = messagebox.askyesno(
        'Salvar', f'Deseja salvar o usuário {username_Form.get()}')
    if username_Form.get() != '' or password_Form != '' or role_Form != '' and confirm == True:

        if role_Form.get() == 'ADMIN' or role_Form.get() == 'CAIXA':

            try:
                conn = sqlite3.Connection('stock.db')
                cur = conn.cursor()

                cur.execute('SELECT * FROM user WHERE username = ?',
                            (username_Form.get(),))
                print('assd')
                temp = cur.fetchone()
                print(temp)

                if temp != None:
                    messagebox.showerror('Usuário', 'Usuário já existente!')
                    conn.close()

                else:
                    cur.execute('INSERT INTO user(username, password, role) VALUES (?,?,?)',
                                (username_Form.get(), password_Form.get(), role_Form.get()))
                    conn.commit()

            except Exception as e:
                print(e)

                messagebox.showerror(
                    'Salvar Usuário', 'Problema ao salvar o Usuário')

            finally:
               loadTable()

        else:
            messagebox.showerror('Usuário', 'Tipo de ROLE inválida')

    else:
        messagebox.showerror(
            'Usuário', 'Não foi possivel salvar o usuário. Há Campos Vazios no Formulário!')


def updateUser():
    update = messagebox.askyesno(
        'Atualizar Usuário', f'Deseja atualizar o Usuário {username_Form.get()}?')

    if update:
        try:
            conn = sqlite3.Connection('stock.db')
            cur = conn.cursor()

            cur.execute('UPDATE user SET username = ? , password = ? , role = ? WHERE id = ? ',
                        (username_Form.get(), password_Form.get(), role_Form.get() ,  id_Form.get()))
            conn.commit()

            messagebox.showinfo('Usuário', 'Usuário Atualizado!')
        except Exception as e:
            print(e)
            messagebox.showerror(
                'Usuário', 'Não foi possível atualizar o Usuário')
        finally:
            loadTable()


def deleteUser():
    delete  = messagebox.askyesno('Deletar Usuário', f'Deseja deletar o usuário {username_Form.get()}?')

    if delete:
        try:
            conn = sqlite3.Connection('stock.db')
            cur = conn.cursor()
            cur.execute('DELETE FROM user WHERE username=?', (username_Form.get(),))
            conn.commit()

            messagebox.showinfo('Deletar Usuário', f'O Usuário {username_Form.get()} foi deletado ')
            
        
        except Exception as e:
            print(e)
            messagebox.showerror('Deletar Usuário', f'Não foi possivel deletar o usuário {username_Form.get()}')

        finally:
            conn.close()
            loadTable()



def search():
    query = username.get()
    selections = []
    for child in table.get_children():
        data = table.item(child)['values']
        try: 
            if data and query.lower() in  data[0].lower():
                selections.append(data)

        except Exception as e:
            # messagebox.showinfo('Usuário', 'Esse usuário não existe!')
            print(e)

    table.delete(*table.get_children())
    for index, item in enumerate(selections):
        table.insert('', END, text=index , values=(item[0], item[1]), tag='user')



def close_window():
    root.destroy()


# DESIGNER
title = CTkLabel(root, text='USUÁRIOS -  ADMIN', width=200)
title.pack(fill=X)

F1 = LabelFrame(root, text='', font=(
    'poppins', 18, 'bold'), bg='#2f2f2f')
F1.place(x=0, y=80, relwidth=1)

name_lb = CTkLabel(F1, text='Usuário', font=(
    'poppins', 18, 'bold'), width=200, height=45)
name_lb.grid(row=0, column=0, columnspan=2, pady=5)

name_entry = CTkEntry(F1, placeholder_text='Nome', font=(
    'poppins', 18, 'bold'), width=200, height=45, textvariable=username)
name_entry.grid(row=0, column=2, columnspan=1)

role_lb = CTkLabel(F1, text='Role', font=(
    'poppins', 18, 'bold'), width=200, height=45)
role_lb.grid(row=0, column=3, columnspan=2)

role_select = CTkComboBox(F1, width=200, height=45,
                          corner_radius=5, values=('ADMIN', 'CAIXA'))
role_select.grid(row=0, column=5, columnspan=1)

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

usernameForm_lb = CTkLabel(F2, text='Nome', height=45,
                           font=('poppins', 14, 'bold'))
usernameForm_entry = CTkEntry(F2, width=200, height=45, placeholder_text='nome de usuário', font=(
    'poppins', 14), textvariable=username_Form)

usernameForm_lb.grid(row=1, column=0, pady=5)
usernameForm_entry.grid(row=1, column=1, padx=16, pady=5)


senhaForm_lb = CTkLabel(F2, text='Senha', height=45,
                        font=('poppins', 14, 'bold'))
senhaForm_entry = CTkEntry(F2, width=200, height=45, placeholder_text='senha',
                           show='*', font=('poppins', 14), textvariable=password_Form)

senhaForm_lb.grid(row=2, column=0, pady=5)
senhaForm_entry.grid(row=2, column=1, pady=5)


roleForm_lb = CTkLabel(F2, text='Role', height=45,
                       font=('poppins', 14, 'bold'))
roleForm_entry = CTkComboBox(F2, width=200, height=45, font=(
    'poppins', 14),  values=('ADMIN', 'CAIXA'), variable=role_Form)

roleForm_lb.grid(row=3, column=0, pady=5)
roleForm_entry.grid(row=3, column=1, pady=5)


divider = CTkLabel(F2, text='', width=200,)
divider.grid(row=4, column=0, pady=50)


bt_insert = CTkButton(F2, text='Inserir', height=45,
                      font=('poppins', 14), command=insertUser)
bt_insert.grid(row=5, column=0, padx=60, pady=5)

bt_update = CTkButton(F2, text='Atualizar', height=45, font=('poppins', 14), command=updateUser)
bt_update.grid(row=5, column=1, padx=5, pady=5)

bt_delete = CTkButton(F2, text='Deletar', height=45, font=('poppins', 14), command=deleteUser)
bt_delete.grid(row=6, column=0, padx=5, pady=5)

bt_exit = CTkButton(F2, text='Sair', height=45, font=('poppins', 14), command=close_window)
bt_exit.grid(row=6, column=1, padx=5, pady=5)


# TABELA DE USUÁRIOS

# FUNCÕES DA TABELA

def item_selected(_):
    # global id_Form, username_Form, password_Form, role_Form
    row = table.item(table.selection())
    id_Form.set(row['text']) 
    username_Form.set(row['values'][0])
    role_Form.set(row['values'][1])
    


# DESIGNER DA TABELA
F3 = LabelFrame(root, text='', font=(
    'serif', 14, 'bold'), fg='#2f2f2f', bg='#125ff0')
F3.place(x=710, y=190, relwidth=0.6, relheight=.75)


table = ttk.Treeview(F3, columns=["Nome", 'Role'])

table.heading('#0', text='ID')
table.heading('Nome', text='Nome')
table.heading('Role', text='Role')

table.tag_bind("user", "<<TreeviewSelect>>", item_selected)

loadTable()

table.pack(expand=True, fill=BOTH, padx=10, pady=10)


root.mainloop()
