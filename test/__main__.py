from py_expression.core import Parser
from py_expression_opencv.lib import *


parser=Parser()
loadOpenCvExpressions(parser)

text='ws=Volume("data"); '\
     'pathImage=ws.fullpath("lena.jpg"); '\
     'image=cvImread(pathImage); '\
     'output=cvtColor(image,ColorConversion.BGR2RGB); '  
     
context = {}
expression = parser.parse(text)

expression.eval(context)
print(context['output'])