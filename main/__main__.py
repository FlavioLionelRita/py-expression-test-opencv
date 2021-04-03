
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedStyle

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from py_expression.core import Parser


class Event(object):   
    def __init__(self): 
        self.__handlers = []   
    def __iadd__(self, handler): 
        self.__handlers.append(handler) 
        return self  
    def __isub__(self, handler): 
        self.__handlers.remove(handler) 
        return self  
    def __call__(self, *args, **keywargs): 
        for handler in self.__handlers: 
            handler(*args, **keywargs) 

plt.style.use('dark_background')

class Main(tk.Frame):
    def __init__(self, master,**kw):
        super(Main, self).__init__(master, **kw)
        self.style = ThemedStyle(self)        
        self.graph = GraphPanel(self)
        self.control = ControlPanel(self)
        self.master.geometry("800x600")
        self.style.theme_use('black')
        self.master.title('Expression graph test')
        self.control.pack(side=tk.TOP, fill=tk.X, expand=True)
        self.graph.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        self.pack(fill=tk.BOTH, expand=tk.YES)

        self.control.onChange+=self.expression_change
        
    def expression_change(self,expression):
        self.graph.show(expression)


class ControlPanel(tk.Frame):
    def __init__(self, master, **kw):
        super(ControlPanel, self).__init__(master, **kw)
        self._onChange=Event()   
        self.bindVar = tk.StringVar()
        self.lbl = tk.Label(self.master, text='expression')
        self.txt = tk.Entry(self.master,textvariable=self.bindVar)
        self.btn = ttk.Button(self.master, text='Go',command=self.onGo)

        self.lbl.place(relx=0, y=0, relwidth=0.2, height=25)
        self.txt.place(relx=0.2, y=0, relwidth=0.7, height=25)      
        self.btn.place(relx=0.9, y=0, relwidth=0.2, height=25)
        self.pack()

        self.bindVar.set('x**2')

    @property
    def onChange(self):
        return self._onChange
    @onChange.setter
    def onChange(self,value):
        self._onChange=value       

    def onGo(self):
        expression = self.bindVar.get()
        self._onChange(expression)



class GraphPanel(tk.Frame):
    def __init__(self, master, **kw):
        super(GraphPanel, self).__init__(master, **kw)   
       
        self.figure = Figure(figsize=(5,5), dpi=100)
        self.plot = self.figure.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2TkAgg(self.canvas, self)
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def show(self,expression):
        try: 
            op = parser.parse(expression) 
            xs=[]
            ys=[] 
            for x in range(-100,100):
                y=op.eval({"x":x})
                xs.append(x)
                ys.append(y)  

            self.plot.clear()
            self.plot.plot(xs,ys) 
            self.canvas.draw() 
        except Exception as error:
            messagebox.showerror(title="Error", message=str(error))                   

parser=Parser()

main = Main(tk.Tk())
main.mainloop()



