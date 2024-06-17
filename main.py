import tkinter
import customtkinter
from CTkTable import *
from tkinter import ttk

DARK_MODE = "dark"
customtkinter.set_appearance_mode(DARK_MODE)
customtkinter.set_default_color_theme("dark-blue")


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
        # self.state('withdraw')
        self.title("Change Frames")

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
        bt_from_main = customtkinter.CTkButton(App.frames['info'], text="Info", command=lambda:print("info") )
        bt_from_main.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)



        ## CADASTRO DE PRODUTOS 
        App.frames['produto'] = customtkinter.CTkFrame(main_container, fg_color="red")
        bt_from_produto = customtkinter.CTkButton(App.frames['produto'], text="Produtos", command=lambda:print("produto") )
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
        bt_from_pedido = customtkinter.CTkButton(App.frames['pedido'], text="Pedidos", command=lambda:print("pedido") )
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
        bt_from_usuario = customtkinter.CTkButton(App.frames['usuario'], text="usuarios", command=lambda:print("usuario") )
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