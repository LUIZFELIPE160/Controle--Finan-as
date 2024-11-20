from tkinter import *
from tkinter import ttk , Tk
from PIL import Image, ImageTk  # para rendenização de imagens
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from tkinter.ttk import Progressbar 


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
img = Image.open('log.png')
img = img.resize((45, 45))
app_img = ImageTk.PhotoImage(img)

label_img = Label(
    frameCima, 
    image=app_img, 
    text="Orçamento Pessoal", 
    width= 900, 
    compound= LEFT, 
    padx=5, 
    relief= RAISED, 
    anchor= NW, 
    font=('Verdana 20 bold'), 
    bg=co1 , 
    fg=co4
    )
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

def porcentagem():
    l_nome = Label(frameMeio, text= "porcentagem da receita gasta".upper(), height=1, anchor=NW, font=("verdana 12"), bg= co1, fg= co4)
    l_nome.place(x=7, y=5)

    style = ttk.Style()
    style.theme_use('default')
    style.configure("black.Horizontal.TProgressbar", background='#daed6b')
    style.configure("TProgressbar", thickness = 25)
    bar = Progressbar(frameMeio, length=180, style='black.Horizontal.TProgressbar')  # cria a barra de progresso e define o tamanhon dela
    bar.place(x=15, y=35)  # coordenadas para o objeto 'bar'
    bar['value'] = 50

    valor = 50

    l_porcento = Label(frameMeio, text= "{:,.2f}%".format(valor), anchor=NW, font=("verdana 12"), bg= co1, fg= co4)
    l_porcento.place(x=200, y=35)
porcentagem()

def grafico_bar():
    lista_categorias = ['renda', 'despesas', 'saldo']
    lista_valores = [3000, 5050, 6235]

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
    valor= [560,600,352]
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

    lista_valores = [345,225,534]
    lista_categorias = ['Renda', 'Despesa', 'Saldo']

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

    lista_itens = [[0,2,3,4],[0,2,3,4],[0,2,3,4],[0,2,3,4]]
    
    global tree

    tree = ttk.Treeview(frame_renda, selectmode="extended",columns=tabela_head, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(frame_renda, orient="vertical", command=tree.yview)
    #horizontal scrollbar
    hsb = ttk.Scrollbar(frame_renda, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    hd=["center","center","center", "center"]
    h=[30,100,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in lista_itens:
        tree.insert('', 'end', values=item)
mostrar_renda()


janela.mainloop()