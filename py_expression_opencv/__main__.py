from py_expression.core import Parser
import cv2 as cv
from enum import Enum

parser = Parser()

op = parser.parse('"expression".count("e")>= a+1')
vars = op.vars()
constants = op.constants()
# operators = op.operators()

result=op.eval({"a":1,"b":2,"c":3})

print(vars)
print(constants)
# print(operators)
print(result)