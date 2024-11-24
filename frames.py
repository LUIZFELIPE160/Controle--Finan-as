from tkinter import *
from tkinter import ttk , Tk
from PIL import Image, ImageTk  # para rendenização de imagens
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from tkinter.ttk import Progressbar 
from tkcalendar import calendar_, DateEntry
from datetime import date







def criar_frames():

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

    janela = Tk()
    janela.title('Controle de Renda')
    janela.geometry('900x650')
    janela.configure(background=co9)
    janela.resizable(width=False , height=False)

    style = ttk.Style(janela)
    style.theme_use("clam")  # TEMA A SER USADO 

    frameCima = Frame(janela, width= 1043, height=50, bg=co1, relief="flat")
    frameCima.grid(row=0, column=0)
    # ordenação e alinhamento da imagem
    img = Image.open('log.png')
    img = img.resize((45, 45))
    app_img = ImageTk.PhotoImage(img)
    # titulo 
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

criar_frames()