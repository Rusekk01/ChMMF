import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from Schemes import *
from PIL import Image, ImageTk
import tkinter.messagebox


class Window:
    def __init__(self, win_h, win_w, panel_w):
        self.win = tk.Tk()
        self.win.title("График")
        ico = Image.open('icon.jpg')
        photo = ImageTk.PhotoImage(ico)
        self.win.wm_iconphoto(False, photo)
        self.win.config(width=win_w, height=win_h)
        self.win.resizable(False, False)
        self.panel = tk.Frame(self.win, width=panel_w, height=win_h, bd=4, relief=tk.GROOVE)
        self.panel.place(x=0, y=0, width=panel_w, height=win_h)
        self.frame1 = tk.Frame(self.win)
        self.frame1.place(x=panel_w, y=0, width=win_w - 200, height=win_w-200)
        self.figure = plt.Figure(figsize=(1, 1), facecolor='wheat')
        self.canvas = FigureCanvasTkAgg(self.figure, self.frame1)
        self.canvas.get_tk_widget().place(x=0, y=0, width=win_w-200, height=win_h)
        self.ax = self.figure.add_subplot()
        self.ax.grid()

        self.type_ = tk.IntVar()
        self.type_.set(0)

        self.graph = []

    def run(self):
        self.draw()
        self.win.mainloop()

    def draw(self):
        lab01 = tk.Label(self.panel, text='График от фиксированного угла')
        lab01.place(x=0, width=190, height=30)
        lab1 = tk.Label(self.panel, text='θ:')
        lab1.place(x=5, y=25, width=10, height=30)
        lab2 = tk.Label(self.panel, text='R:')
        lab2.place(x=5, y=235, width=10, height=30)
        lab3 = tk.Label(self.panel, text='T_max:')
        lab3.place(x=5, y=265, width=35, height=30)
        lab4 = tk.Label(self.panel, text='k:')
        lab4.place(x=5, y=295, width=10, height=30)
        lab5 = tk.Label(self.panel, text='c:')
        lab5.place(x=5, y=325, width=10, height=30)
        lab6 = tk.Label(self.panel, text='L:')
        lab6.place(x=5, y=355, width=10, height=30)
        lab8 = tk.Label(self.panel, text='I:')
        lab8.place(x=5, y=385, width=10, height=30)
        lab9 = tk.Label(self.panel, text='K:')
        lab9.place(x=5, y=415, width=10, height=30)

        ent1 = tk.Entry(self.panel, bd=2)
        ent1.place(x=40, y=30, width=45)
        ent1.insert(0, '1.56')
        ent2 = tk.Entry(self.panel, bd=2)
        ent2.place(x=40, y=240, width=45)
        ent2.insert(0, '8')
        ent3 = tk.Entry(self.panel, bd=2)
        ent3.place(x=40, y=270, width=45)
        ent3.insert(0, '130')
        ent4 = tk.Entry(self.panel, bd=2)
        ent4.place(x=40, y=300, width=45)
        ent4.insert(0, '0.59')
        ent5 = tk.Entry(self.panel, bd=2)
        ent5.place(x=40, y=330, width=45)
        ent5.insert(0, '1.65')
        ent6 = tk.Entry(self.panel, bd=2)
        ent6.place(x=40, y=360, width=45)
        ent6.insert(0, '0.2')
        ent8 = tk.Entry(self.panel, bd=2)
        ent8.place(x=40, y=390, width=45)
        ent8.insert(0, '40')
        ent9 = tk.Entry(self.panel, bd=2)
        ent9.place(x=40, y=420, width=45)
        ent9.insert(0, '6400')


        r1 = tk.Radiobutton(text='Простейшая', variable=self.type_, value=0)
        r1.place(x=15, y=480, width=90)
        r2 = tk.Radiobutton(text='Модифицированная', variable=self.type_, value=1)
        r2.place(x=12, y=510, width=140)

        but1 = tk.Button(self.panel, text='Отобразить', command=lambda: self.do_plot_t(float(ent1.get())))
        but1.place(x=80, y=65, width=100, height=30)
        but2 = tk.Button(self.panel, text='Отобразить', command=lambda: self.do_plot_teta(float(ent7.get())))
        but2.place(x=80, y=160, width=100, height=30)
        but3 = tk.Button(self.panel, text='Очистить', command=lambda: self.plot_delete())
        but3.place(x=80, y=648, width=100, height=30)
        but4 = tk.Button(self.panel, text='Подсчитать', command=lambda: self.build_scheme(self.type_.get()))
        but4.place(x=80, y=540, width=100, height=30)

        lab02 = tk.Label(self.panel, text='График от фиксированного t')
        lab02.place(x=0, y=95, width=190, height=30)
        ent7 = tk.Entry(self.panel, bd=2)
        ent7.place(x=40, y=125, width=45)
        ent7.insert(0, '10')
        lab7 = tk.Label(self.panel, text='t:')
        lab7.place(x=5, y=120, width=10, height=30)

        lab03 = tk.Label(self.panel, text='Константы и размерность сетки')
        lab03.place(x=0, y=200, width=190, height=30)

        lab04 = tk.Label(self.panel, text='Выбор разностной схемы')
        lab04.place(x=0, y=450, width=190, height=30)

    def build_scheme(self, type_):
        print(type_)
        print(self.panel.winfo_children())
        r = float(self.panel.winfo_children()[10].get())
        print(r, 'r')
        t_max = float(self.panel.winfo_children()[11].get())
        print(t_max, 't_max')
        k = float(self.panel.winfo_children()[12].get())
        print(k, 'k')
        c = float(self.panel.winfo_children()[13].get())
        print(c, 'c')
        l = float(self.panel.winfo_children()[14].get())
        print(l, 'l')
        I_ = int(self.panel.winfo_children()[15].get())
        print(I_, 'I')
        K_ = int(self.panel.winfo_children()[16].get())
        print(K_, 'K')
        if type_ == 0:
            self.graph = DifferenceScheme(R=r, k=k, c=c, l=l, I=I_, K=K_)
            print("DONE")
        else:
            self.graph = DifferenceScheme_MOD(R=r, k=k, c=c, l=l, I=I_, K=K_)
            print("DONE")

    def do_plot_t(self, teta):
        # ax.clear()
        try:
            self.ax.plot(self.graph.arr_t_k, self.graph.v[:, int(teta / self.graph.h_teta)],
                    label='Простейшая ' + 'teta = ' + str(teta) + ', I = ' + str(self.graph.I) + ', K = ' + str(self.graph.K) if self.type_.get() == 0
                    else 'Модифицированная ' + 'teta = ' + str(teta) + ', I = ' + str(self.graph.I) + ', K = ' + str(self.graph.K))
        except AttributeError:
            tkinter.messagebox.showerror(title="Ошибка", message="Сначала подсчитайте сетку")
        except IndexError:
            tkinter.messagebox.showerror(title="Ошибка", message="Значение не должно превышать PI/2")
        self.figure.legends = []
        # figure.grid()
        self.figure.legend()
        self.canvas.draw()

    def do_plot_teta(self, t):
        try:
            self.ax.plot(self.graph.arr_teta_i, self.graph.v[int(t / self.graph.h_t)],
                    label='Простейшая ' + 't = ' + str(t) + ', I = ' + str(self.graph.I) + ', K = ' + str(self.graph.K) if self.type_.get() == 0
                    else 'Модифицированная ' + 't = ' + str(t) + ', I = ' + str(self.graph.I) + ', K = ' + str(self.graph.K))
        except AttributeError:
            tkinter.messagebox.showerror(title="Ошибка", message="Сначала подсчитайте сетку")
        except IndexError:
            tkinter.messagebox.showerror(title="Ошибка", message="Значение не должно превышать T_max = " + str(self.graph.T))
        self.figure.legends = []
        self.figure.legend()
        self.canvas.draw()

    def plot_delete(self):
        self.ax.clear()
        self.ax.grid()
        self.figure.legends = []
        self.canvas.draw()
