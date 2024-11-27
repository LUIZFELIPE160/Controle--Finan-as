from tkinter import *
from tkinter import messagebox
from tkinter import ttk , Tk
from PIL import Image, ImageTk  # para rendenização de imagens
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from tkinter.ttk import Progressbar 
from tkcalendar import calendar_, DateEntry
from datetime import date
from view import * #del_despesas, inserir_categoria, inserir_receitas, ver_categoria, ver_despesas
import os

PATH = os.path.dirname(os.path.realpath(__file__))  # Path to images

co0 = "#2e2d2b"
co1 = "#feffff"
co2 = "#4fa882" 
co3 = "#38572b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#3fbfb9"
co8 = "#263238"
co9 = "#e9edf5"
colors = ["#5588bb","#66bbbb","#99bb55", "#ee9944","#444466","#bb5555"]

#criando janela
janela = Tk()
janela.title('Controle de Renda')
janela.geometry('900x650')
janela.configure(background=co9)
janela.resizable(width=False , height=False)

style = ttk.Style(janela)
style.theme_use("clam")  # TEMA A SER USADO 

# criando frames
frameCima = Frame(janela, width= 1043, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

#configuração do frame Cima 
img = Image.open(PATH + "/image/img_log.png")
#img = Image.open('img_log.png')
img = img.resize((45, 45))
app_img = ImageTk.PhotoImage(img)

label_img = Label(frameCima, image=app_img, text="Orçamento Pessoal", width= 900, compound= LEFT, padx=5, relief= RAISED, anchor= NW, font=('Verdana 20 bold'), bg=co1 , fg=co4)
label_img.place(x=0, y=0) 

frameMeio = Frame(janela, width= 1043, height=361, bg=co1, pady=20, relief="raised")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky= NSEW)

frameBaixo = Frame(janela, width= 1043, height=300, bg=co1, relief="flat")
frameBaixo.grid(row=2, column=0, pady=0, padx=10, sticky= NSEW)

frame_rosca = Frame(frameMeio, width=580, height=250, bg=co2)
frame_rosca.place(x=415,y=5)

frame_renda = Frame(frameBaixo, width=300, height=250, bg=co1)
frame_renda.grid(row=0, column=0)

frame_operacoes = Frame(frameBaixo, width=220, height=250, bg=co1)
frame_operacoes.grid(row=0, column=1, padx=5)

frame_conf = Frame(frameBaixo, width=220, height=250, bg=co1)
frame_conf.grid(row=0, column= 2, padx=5)

global tree 


# dinamicidade ==================================================================
def adicionar_categoria():

    nome = categoria_rec.get()  # Obtém o valor do campo de entrada
    lista_inserir = [nome]

    # Verifica se o campo está vazio
    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Insira uma categoria')
            return
        
    inserir_categoria(lista_inserir)
    messagebox.showinfo('Sucesso', 'Categoria adicionada com sucesso')
    categoria_rec.delete(0, 'end')
    categoria_funcao = ver_categoria()
    categoria= []

    for i in categoria_funcao:
        categoria.append(i[1])

    # Atualiza o combobox com a lista de categorias
    combo_categoria['values'] = (categoria)

    # Exibe mensagem de sucesso

def adicionar_receitas():
    nome = 'Receitas'
    data = combo_data_rec.get()
    valor = combo_quantia_rec.get()

    lista_inserir = [nome, data, valor]
    for i in lista_inserir:
        if i == '':
            messagebox.showerror('Erro', 'Preencha todos os campos')
            return
        
    inserir_receitas(lista_inserir)
    messagebox.showinfo('Sucesso', 'Receita adicionada com sucesso')

    combo_data_rec.delete(0, 'end')
    combo_quantia_rec.delete(0, 'end')

    mostrar_renda()
    porcentagem()
    grafico_bar()
    resumo()
    grafico_rosca()

def adicionar_despesas():
    nome = combo_categoria.get()
    data = combo_data_desp.get()
    quantia = combo_quantia_desp.get()

    lista_inserir = [nome, data, quantia]

    for item in lista_inserir:
        if item == '':
            messagebox.showerror("Erro", "Preencha todos os campos!")
            return

    inserir_despesas(lista_inserir)

    messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso!')

    combo_data_desp.delete(0, END)
    combo_quantia_desp.delete(0, END)
    combo_categoria.delete(0, END)

    mostrar_renda()
    porcentagem()
    grafico_bar()
    resumo()
    grafico_rosca()

def deletar_dados(): 
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor = treev_lista[0]
        nome = treev_lista[1]

        if nome == 'Receitas':
            deletar_receitas([valor])
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso!')

            mostrar_renda()
            porcentagem()
            grafico_bar()
            resumo()
            grafico_rosca()
        else:
            deletar_gastos([valor])
            messagebox.showinfo('Sucesso', 'Os dados foram deletados com sucesso!')

            mostrar_renda()
            porcentagem()    
            grafico_bar()
            resumo()
            grafico_rosca()
    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item na tabela')  

# interface/ graficos ==========================================================
def porcentagem():
    l_nome = Label(frameMeio, text= "porcentagem da receita gasta".upper(), height=1, anchor=NW, font=("verdana 12"), bg= co1, fg= co4)
    l_nome.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness = 25)
    bar = Progressbar(frameMeio, length=180, style='black.Horizontal.TProgressbar')  # cria a barra de progresso e define o tamanhon dela
    bar.place(x=15, y=35)  # coordenadas para o objeto 'bar'
    bar['value'] = percentagem_valor()[0]

    valor = percentagem_valor()[0]

    l_porcento = Label(frameMeio, text= "{:,.2f}%".format(valor), anchor=NW, font=("verdana 12"), bg= co1, fg= co4)
    l_porcento.place(x=200, y=35)
porcentagem()

def grafico_bar(): 
    lista_categorias = ['renda', 'despesas', 'saldo']
    lista_valores = bar_valores()

#faça figura e atribua objetos de eixo
    figura = plt.Figure(figsize=(4, 3.45), dpi=60)
    ax = figura.add_subplot(111)
    #ax.autoscale(enable=True, axis='both', tight=None)

    ax.bar(lista_categorias, lista_valores,  color=colors, width=0.9)  # cria o código de barras

    c = 0
    #set individual bar lables using above list
    for i in ax.patches:
        #get_x pulls left or right; get_height pushes up or down
        ax.text(i.get_x()-.001, i.get_height()+.5,
                str("{:,.0f}".format(lista_valores[c])), fontsize=17, fontstyle='italic',  verticalalignment='bottom',color='dimgrey')
        c += 1

    ax.set_xticklabels(lista_categorias,fontsize=16)

    ax.patch.set_facecolor('#ffffff')
    ax.spines['bottom'].set_color('#CCCCCC')
    ax.spines['bottom'].set_linewidth(1)
    ax.spines['right'].set_linewidth(0)
    ax.spines['top'].set_linewidth(0)
    ax.spines['left'].set_color('#CCCCCC')
    ax.spines['left'].set_linewidth(1)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(bottom=False, left=False)
    ax.set_axisbelow(True)
    ax.yaxis.grid(False, color='#EEEEEE')
    ax.xaxis.grid(False)

    canva = FigureCanvasTkAgg(figura, frameMeio)
    canva.get_tk_widget().place(x=10, y=70)
grafico_bar()

def resumo():
    valor= bar_valores()
    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')  # configuração da linha 
    l_linha.place(x=309, y=52)
    l_str = Label(frameMeio, text="Total Renda Mensal      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_str.place(x=309, y=35)
    l_valor = Label(frameMeio, text="R${:,.2f}".format(valor[0]), anchor=NW, font=("Arial 17"), bg=co1, fg='#83a9e6')
    l_valor.place(x=309, y=65)

    l_linha = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')  # configuração da linha 
    l_linha.place(x=309, y=140)
    l_str = Label(frameMeio, text="Total despesa Mensal      ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_str.place(x=309, y=123)
    l_valor = Label(frameMeio, text="R${:,.2f}".format(valor[1]), anchor=NW, font=("Arial 17"), bg=co1, fg='#83a9e6')
    l_valor.place(x=309, y=153)

    l_saldo = Label(frameMeio, text="", width=215, height=1, anchor=NW, font=('Arial 1'), bg='#545454')  # configuração da linha 
    l_saldo.place(x=309, y=228)
    l_str = Label(frameMeio, text="Saldo Total                 ".upper(), anchor=NW, font=('Verdana 12'), bg=co1, fg='#83a9e6')
    l_str.place(x=309, y=211)
    l_valor = Label(frameMeio, text="R${:,.2f}".format(valor[2]), anchor=NW, font=("Arial 17"), bg=co1, fg='#83a9e6')
    l_valor.place(x=309, y=241)
resumo()

def grafico_rosca():
    figura = plt.Figure(figsize=(5,3), dpi=90)
    ax = figura.add_subplot(111)

    lista_valores = pie_valores()[1]
    lista_categorias = pie_valores()[0]

    explode = []
    for i in lista_categorias:
        explode.append(0.05)

    ax.pie(lista_valores, explode=explode, wedgeprops=dict(width=0.2), autopct='%1.1f%%', colors=colors,shadow=True, startangle=90)
    ax.legend(lista_categorias, loc="center right", bbox_to_anchor=(1.55, 0.50))

    canva_categoria = FigureCanvasTkAgg(figura, frame_rosca)
    canva_categoria.get_tk_widget().grid(row=0, column=0)
grafico_rosca()

label_title = Label(
    frameMeio,
    text="Tabela Receitas e Despesas", 
    padx=5,
    anchor= NW, 
    font=('Verdana 20'), 
    bg=co1 , 
    fg=co4
    )
label_title.place(x=5, y=300) 

def mostrar_renda():
    tabela_head = ['#Id','Categoria','Data','Quantia']

    lista_itens = tabela()
    
    global tree  #definindo tree globalmente 

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings") 
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)   # vertical scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview) # horizontal scrollbar

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]  # configuracao dos nomes das colunas
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)
mostrar_renda()

# labels do frame baixo  DESPESAS =======================================================================
l_info = Label(frame_operacoes, text='Insira novas despesas', height=1, anchor= NW, font= ("verdana 12 bold"), bg=co1, fg=co4)
l_info.place(x=10, y=10)

categoria_funcao = ver_categoria() #funcao da view, para mostrar as categorias na combobox
categoria= []
for i in categoria_funcao:
    categoria.append(i[1])  

# imputs =======================================================================================
l_categoria = Label(frame_operacoes, text='Categoria', height=1, anchor=NW, font=("ivy 10"), bg=co1, fg=co4)
l_categoria.place(x=10, y=40)
combo_categoria =ttk.Combobox(frame_operacoes, width=10, font= ('ivy 10'))
combo_categoria['values'] = (categoria)
combo_categoria.place(x=110, y=41)

l_data = Label(frame_operacoes, text='Data', height=1, anchor=NW, font=("ivy 10"), bg=co1, fg=co4)
l_data.place(x=10, y=70)
combo_data_desp =DateEntry(frame_operacoes, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024)
combo_data_desp.place(x=110, y=70)

l_quantia = Label(frame_operacoes, text='Quantia(R$)', height=1, anchor=NW, font=("ivy 10"), bg=co1, fg=co4)
l_quantia.place(x=10, y=100)
combo_quantia_desp = Entry(frame_operacoes, width=14, justify='left', relief='solid')
combo_quantia_desp.place(x=110, y=100)

# icon adicionar
icon_add = Image.open(PATH + "/image/img_add.png")
#icon_add = Image.open('img_add.png')
icon_add = icon_add.resize((17, 17))
icon_add = ImageTk.PhotoImage(icon_add)

btn_add_1 = Button(frame_operacoes,command=adicionar_despesas, image=icon_add, text="Adicionar".upper(), width= 80, compound= LEFT, anchor= NW, font=('Ivy 7 bold'), bg=co1 , fg=co0, overrelief=RIDGE)
btn_add_1.place(x=110, y=130)

l_deletar = Label(frame_operacoes, text='Excluir Ação', height=1, anchor=NW, font=("verdana 9 bold"), bg=co1, fg=co4)
l_deletar.place(x=10, y=165)
icon_delete = Image.open(PATH + "/image/img_delete.png")
#icon_delete = Image.open('img_delete.png')  # icon deletar
icon_delete = icon_delete.resize((17, 17))
icon_delete = ImageTk.PhotoImage(icon_delete)
btn_delete = Button(frame_operacoes,command=deletar_dados, image=icon_delete, text="deletar".upper(), width= 80, compound= LEFT, anchor= NW, font=('Ivy 7 bold'), bg=co1 , fg=co0, overrelief=RIDGE)
btn_delete.place(x=10, y=195)

# labels do frame baixo  RECEITAS =======================================================================
l_info_rec = Label(frame_conf, text='Insira novas receitas', height=1, anchor= NW, font= ("verdana 12 bold"), bg=co1, fg=co4)
l_info_rec.place(x=10, y=10)

l_data_rec = Label(frame_conf, text='Data', height=1, anchor=NW, font=("ivy 10"), bg=co1, fg=co4)
l_data_rec.place(x=10, y=40)
combo_data_rec =DateEntry(frame_conf, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024)
combo_data_rec.place(x=110, y=40)

l_quantia_rec = Label(frame_conf, text='Quantia(R$)', height=1, anchor=NW, font=("ivy 10"), bg=co1, fg=co4)
l_quantia_rec.place(x=10, y=70)
combo_quantia_rec = Entry(frame_conf, width=14, justify='left', relief='solid')
combo_quantia_rec.place(x=110, y=70)

btn_add_2 = Button(frame_conf, command=adicionar_receitas, image=icon_add, text="Adicionar".upper(), width= 80, compound= LEFT, anchor= NW, font=('Ivy 7 bold'), bg=co1 , fg=co0, overrelief=RIDGE)
btn_add_2.place(x=110, y=95)

l_info_categoria = Label(frame_conf, text='Insira nova categoria', height=1, anchor= NW, font= ("verdana 9 bold "), bg=co1, fg=co4)
l_info_categoria.place(x=10, y=140)

l_categoria = Label(frame_conf, text='Categoria', height=1, anchor=NW, font=("ivy 10 bold"), bg=co1, fg=co4)
l_categoria.place(x=10, y=165)
categoria_rec =Entry(frame_conf, width=14,justify= LEFT, relief='solid')
categoria_rec.place(x=110, y=165)

btn_add_3 = Button(frame_conf,command=adicionar_categoria, image=icon_add, text="Adicionar".upper(), width= 80, compound= LEFT, anchor= NW, font=('Ivy 7 bold'), bg=co1 , fg=co0, overrelief=RIDGE)
btn_add_3.place(x=110, y=195)

janela.mainloop()
