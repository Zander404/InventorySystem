import tkinter
import customtkinter
from tkinter import ttk, messagebox
from CTkMessagebox import CTkMessagebox

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("dark-blue")



class NewProduct(customtkinter.CTkToplevel):

    def add_product(self, id:int, nome:str, preco:int, quant:int):
        if not id or not nome or not preco or not quant:
            CTkMessagebox(title='Campo Inválido',message='Há Campos Vazios no Formulário!', icon='cancel', justify='center') 

        elif not id.isnumeric() or not preco.isnumeric() or not  quant.isnumeric():
            CTkMessagebox(title='Campo Inválido',message='Campos \n CÓDIGO DE PRODUTO, PREÇO ou QUANTIDADE \n não estão com valores do tipo Inteiro/Real', icon='warning', justify='center')
        
        else:
            id = int(id)
            preco = round(float(preco.replace(',', '.')), 2)
            quant = int(quant)

            print(preco)
            print(quant)
        

    def __init__(self, master = None):
        super().__init__(master=master, )
        self.attributes('-topmost',True)
        

        self.title("Adicionar Produto")
        self.geometry(f'620x480')
        
        title = customtkinter.CTkLabel(self, text='Adicionar Novo Produto', font=('Sans-Serif', 20))


        id_produtoFrame = customtkinter.CTkFrame(self)
        nome_produtoFrame = customtkinter.CTkFrame(self)
        preco_produtoFrame  = customtkinter.CTkFrame(self)
        quant_produtoFrame = customtkinter.CTkFrame(self)


        id_produtoLabel = customtkinter.CTkLabel(id_produtoFrame, text='Codigo de Produto')
        nome_produtoLabel = customtkinter.CTkLabel(nome_produtoFrame, text='Nome do Produto')
        preco_produtoLabel = customtkinter.CTkLabel(preco_produtoFrame, text='Preço')
        quant_produtoLabel = customtkinter.CTkLabel(quant_produtoFrame, text='Quantidade')


        id_produtoEntry = customtkinter.CTkEntry(master=id_produtoFrame, placeholder_text='12345678', width=220, height=45, corner_radius=5, text_color='white', font=('Sans-Serif', 16))
        nome_produtoEntry = customtkinter.CTkEntry(master=nome_produtoFrame, placeholder_text='Nome do Produto', width=220,  height=45, corner_radius=5, text_color='white', font=('Sans-Serif', 16))
        preco_produtoEntry = customtkinter.CTkEntry(master=preco_produtoFrame, placeholder_text='0,00', width=220, height=45, corner_radius=5, text_color='white', font=('Sans-Serif', 16))
        quant_produtoEntry = customtkinter.CTkEntry(master=quant_produtoFrame, placeholder_text='0', width=220, height=45, corner_radius=5, text_color='white', font=('Sans-Serif', 16))

        btn_salvar = customtkinter.CTkButton(self, text=('SALVAR'), command=lambda:self.add_product(id=id_produtoEntry.get(), nome=nome_produtoEntry.get(), preco=preco_produtoEntry.get(), quant=quant_produtoEntry.get()))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(10, weight=1)

        title.grid(row=1, column=0 )

        
        id_produtoLabel.grid(row=0, column=0)
        id_produtoEntry.grid(row=1, column=0)


        nome_produtoLabel.grid(row=0, column=0)
        nome_produtoEntry.grid(row=1, column=0)

        preco_produtoLabel.grid(row=0, column=0)
        preco_produtoEntry.grid(row=1, column=0)

        quant_produtoLabel.grid(row=0, column=0)
        quant_produtoEntry.grid(row=1, column=0)


        id_produtoFrame.grid(row=0, column=0, pady=10)
        nome_produtoFrame.grid(row=1, column=0, pady=10)
        preco_produtoFrame.grid(row=2, column=0, pady=10)
        quant_produtoFrame.grid(row=3, column=0, pady=10)
        

        btn_salvar.grid(row=10, column=0)


        self.mainloop()


class NewUser(customtkinter.CTkToplevel):

    def add_user(self, username:str, password:str, conf_password:str):
        if username and password and conf_password:
            if password == conf_password:
                print(username)
                print(password)
                print(conf_password)

            else:
                CTkMessagebox(self, title='Senha Inválida',  message='Senhas não correspondente! Escreva a senha novamente.', icon='warning')
        else:
            CTkMessagebox(self, title='Campos Vazios', message='Há Campos Vazios no Formulário!', icon='cancel')

    def __init__(self, master = None):
        super().__init__(master=master, )
        self.attributes('-topmost',True)

        self.title("Novo Usuario")
        self.geometry('640x480')
        title = customtkinter.CTkLabel(self, text='Adicionar novo Usuário')

        nome_userFrame = customtkinter.CTkFrame(self)
        password_userFrame  = customtkinter.CTkFrame(self)
        conf_password_userFrame = customtkinter.CTkFrame(self)



        nome_userLabel = customtkinter.CTkLabel(nome_userFrame, text='Nome de Usuário')
        password_userLabel = customtkinter.CTkLabel(password_userFrame, text='Senha')
        conf_password_userLabel = customtkinter.CTkLabel(conf_password_userFrame, text='Confirmar Senha')



        nome_userEntry = customtkinter.CTkEntry(master=nome_userFrame, placeholder_text='Fulano', width=220,  height=45, corner_radius=5, text_color='white', font=('Sans-Serif', 16))
        password_userEntry = customtkinter.CTkEntry(master=password_userFrame, placeholder_text='*******', width=220, height=45, corner_radius=5, text_color='white', font=('Sans-Serif', 16))
        conf_password_userEntry = customtkinter.CTkEntry(master=conf_password_userFrame, placeholder_text='*******', width=220, height=45, corner_radius=5, text_color='white', font=('Sans-Serif', 16))

        btn_salvar = customtkinter.CTkButton(self, text=('SALVAR'), command=lambda:self.add_user(username=nome_userEntry.get(), password=password_userEntry.get(), conf_password=conf_password_userEntry.get()))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(4, weight=3)

        title.grid(row=0, column=0, pady=20 )

        nome_userLabel.grid(row=0, column=0)
        nome_userEntry.grid(row=1, column=0)

        password_userLabel.grid(row=0, column=0)
        password_userEntry.grid(row=1, column=0)

        conf_password_userLabel.grid(row=0, column=0)
        conf_password_userEntry.grid(row=1, column=0)


        nome_userFrame.grid(row=1, column=0, pady=10)
        password_userFrame.grid(row=2, column=0, pady=10)
        conf_password_userFrame.grid(row=3, column=0, pady=10)
        

        btn_salvar.grid(row=4, column=0)



class NewOrder(customtkinter.CTkToplevel):
    def __init__(self, master = None):
        super().__init__(master=master, )
        self.attributes('-topmost',True)

        self.title("Novo Pedido")
        self.geometry('640x480')
        title = customtkinter.CTkLabel(self, text='Adicionar Novo Pedido')

        cliente_orderFrame = customtkinter.CTkFrame(self)
        list_products_orderFrame  = customtkinter.CTkFrame(self)
        caixa_orderFrame = customtkinter.CTkFrame(self)

        cliente_orderList = customtkinter.CTkComboBox(cliente_orderFrame, values=['Fabio', 'Gabriel', 'Luann'])

        list_productsList = customtkinter.CTkLabel(list_products_orderFrame, text='sad')
        #  
        caixa_orderList = customtkinter.CTkComboBox(caixa_orderFrame, values=['Fabio', 'Gabriel', 'Luann'])
        

        btn_salvar = customtkinter.CTkButton(self, text=('Salvar'))


        self.columnconfigure(0, weight=1)
        self.rowconfigure(5, weight=3)
        
    
        title.grid(row=0, column=0, pady=20 )


        cliente_orderList.grid(row=0, column=0)
        caixa_orderList.grid(row=0, column=0)
        list_productsList.grid(row=0, column=0)


        cliente_orderFrame.grid(row=1, column=0)
        caixa_orderFrame.grid(row=2, column=0)
        list_products_orderFrame.grid(row=3, column=0)

        btn_salvar.grid(row=4, column=0)





class App(customtkinter.CTk):

    frames = {'info': None, "produto": None, "pedido": None, 'usuario': None}


    def main_selector(self):
        App.frames['info'].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        App.frames['produto'].pack_forget()
        App.frames["pedido"].pack_forget()
        App.frames["usuario"].pack_forget()


    def produto_selector(self):
        App.frames["info"].pack_forget()
        App.frames["produto"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        App.frames["pedido"].pack_forget()
        App.frames["usuario"].pack_forget()


    def pedido_selector(self):
        App.frames["info"].pack_forget()
        App.frames["produto"].pack_forget()
        App.frames["pedido"].pack(in_=self.right_side_container,side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
        App.frames["usuario"].pack_forget()

    def usuario_selector(self):
        App.frames['info'].pack_forget()
        App.frames['produto'].pack_forget()
        App.frames['pedido'].pack_forget()
        App.frames['usuario'].pack(in_=self.right_side_container, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)

    def __init__(self):
        super().__init__()
        self.state('withdraw')
        self.title("Sistema de Cadastro")

        self.geometry("{0}x{0}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))

        # contains everything
        main_container = customtkinter.CTkFrame(self)
        main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        # left side panel -> for frame selection
        left_side_panel = customtkinter.CTkFrame(main_container, width=150)
        left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=10, pady=10)

        # buttons to select the frames
        bt_frame_main = customtkinter.CTkButton(left_side_panel, text="Info", command=self.main_selector)
        bt_frame_main.grid(row=0, column=0, padx=20, pady=10)
        # buttons to select the frames

        bt_produto = customtkinter.CTkButton(left_side_panel, text="Produto", command=self.produto_selector)
        bt_produto.grid(row=1, column=0, padx=20, pady=10)

        bt_pedido = customtkinter.CTkButton(left_side_panel, text="Pedido", command=self.pedido_selector)
        bt_pedido.grid(row=2, column=0, padx=20, pady=10)

        bt_usuario = customtkinter.CTkButton(left_side_panel, text='Usuário', command=self.usuario_selector)
        bt_usuario.grid(row=3, column=0, padx=20, pady=10)

        # right side panel -> to show the produto or frame 2
        self.right_side_panel = customtkinter.CTkFrame(main_container)
        self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=10, pady=10)

        self.right_side_container = customtkinter.CTkFrame(self.right_side_panel,fg_color="#000811")
        self.right_side_container.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=0, pady=0)




        ## INFO
        App.frames['info']  = customtkinter.CTkFrame(main_container, fg_color="green")
        bt_from_main = customtkinter.CTkButton(App.frames['info'], text="Info", command=lambda:NewProduct(App.frames['info']))
        bt_from_main.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)




        ## CADASTRO DE PRODUTOS 
        App.frames['produto'] = customtkinter.CTkFrame(main_container, fg_color="red")
        bt_from_produto = customtkinter.CTkButton(App.frames['produto'], text="Produtos", command=(lambda: NewProduct(App.frames['produto'])) )
        bt_from_produto.pack(padx=5, pady=5)

        table_product = ttk.Treeview(App.frames['produto'], columns=('ID','Produto', 'Preço', 'Quantidade'), show='headings', )
        table_product.heading('ID', text='ID')
        table_product.heading('Produto', text='Produto')
        table_product.heading('Preço', text='Preço')
        table_product.heading('Quantidade', text='Quantidade')

        def item_select_product(_):
            print(table_product.selection())
            table_product.item(table_product.selection())

            for i in table_product.selection():
                print(table_product.item(i)['values'])

        # def delete_item(_):
        #     print('delete')
        #     for i in table_product.selection():
        #         table_product.delete(i)

            
        
        for i in range(100):
            table_product.insert(parent='', index='end', values=('ABC', 'BOLO', i, '10'))

        table_product.bind('<<TreeviewSelect>>', item_select_product)
        # table_product.bind('<Delete>', delete_item )
        table_product.pack(expand=True, fill='both', padx=10, pady=10)



        ## CADASTRO DE PEDIDOS
        App.frames['pedido'] = customtkinter.CTkFrame(main_container,fg_color="blue")
        bt_from_pedido = customtkinter.CTkButton(App.frames['pedido'], text="Pedidos", command=lambda:NewOrder(master=App.frames['pedido']) )
        bt_from_pedido.pack(padx=0.5, pady=0.5)


        table_pedidos = ttk.Treeview(App.frames['pedido'], columns=['ID', 'Lista de Produtos', 'Caixa'], show='headings')
        table_pedidos.heading('ID',text='ID')
        table_pedidos.heading('Caixa',text='Caixa')
        table_pedidos.heading('Lista de Produtos',text='Lista de Produtos')


        for i in range(100):
            table_pedidos.insert(parent='', index='end', values=('ABC', 'CAIXA', i))


        def item_select_pedido(_):
            print(table_pedidos.selection())
            table_pedidos.item(table_pedidos.selection())

            for i in table_pedidos.selection():
                print(table_pedidos.item(i)['values'])

        
        table_pedidos.bind('<<TreeviewSelect>>', item_select_pedido)
        table_pedidos.pack(expand=True, fill='both', padx=10, pady=10)
    




        ## CADASTRO DE USUÁRIOS
        App.frames['usuario'] = customtkinter.CTkFrame(main_container,fg_color="blue")
        bt_from_usuario = customtkinter.CTkButton(App.frames['usuario'], text="usuarios", command=lambda:NewUser(master=App.frames['usuario']))
        bt_from_usuario.pack(padx=0.5, pady=0.5)

        table_usuario = ttk.Treeview(App.frames['usuario'], columns=['ID', 'Nome', 'Email', 'Role'], show='headings')
        table_usuario.heading('ID',text='ID')
        table_usuario.heading('Nome',text='Nome')    
        table_usuario.heading('Email',text='Email')
        table_usuario.heading('Role',text='Role')

        
        for i in range(100):
            table_usuario.insert(parent='', index='end', values=(i, 'CAIXA', 'teste@teste.com', 'user'))



        def item_select_usuario(_):
            print(table_usuario.selection())
            table_usuario.item(table_usuario.selection())

            for i in table_usuario.selection():
                print(table_usuario.item(i)['values'])

        
        table_usuario.bind('<<TreeviewSelect>>', item_select_usuario)
        table_usuario.pack(expand=True, fill='both', padx=20, pady=20)


a = App()
a.main_selector()
a.mainloop()