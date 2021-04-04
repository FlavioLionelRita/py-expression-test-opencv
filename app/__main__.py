import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedStyle
from PIL import ImageTk, Image
from py_expression.core import Parser
from py_expression_opencv.lib import *
from tkinter import scrolledtext as st

class Main(tk.Frame):
    def __init__(self, master,**kw):
        super(Main, self).__init__(master, **kw)
        self.style = ThemedStyle(self)
        self.lbl = tk.Label(self, text='expression')
        self.txt = st.ScrolledText(self,height=7)
        self.btn = ttk.Button(self, text='Run',command=self.onRun)
        self.lblImage = tk.Label(self,bg="black") 

        self.master.geometry("800x600")
        self.style.theme_use('black')
        self.master.title('Expression graph test')

        self.lbl.pack()
        self.txt.pack()
        self.btn.pack()
        self.lblImage.pack(fill='both', expand=1)   
        self.pack(fill=tk.BOTH, expand=tk.YES)

        self.txt.insert(tk.INSERT,
'''\
ws=Volume("data");
pathImage=ws.fullpath("lena.jpg");
image=cvImread(pathImage);
output=cvtColor(image,ColorConversion.BGR2GRAY);    
''')     
        
    def onRun(self):
        try: 
            lines = self.txt.get("1.0", tk.END) 
            lines=lines.replace('\n','')
            op = parser.parse(lines)
            context = {}
            op.eval(context)
            value=context['output']
            _image = Image.fromarray(value)
            _image = _image.resize((self.lblImage.winfo_width(), self.lblImage.winfo_height()), Image.ANTIALIAS)
            image = ImageTk.PhotoImage(_image)
            self.lblImage.configure(image=image)
            self.lblImage.image = image
        except Exception as error:
            messagebox.showerror(title="Error", message=str(error)) 

parser=Parser()
loadOpenCvExpressions(parser)
main = Main(tk.Tk())
main.mainloop()