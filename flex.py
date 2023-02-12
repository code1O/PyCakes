import importlib
import os
import sys
from time import sleep
from termcolor import colored

def tupst(int, str, float):
    tup = (int, str, float)
    for i in tuple(tup):
        tup = (i)

def lst(int, str, float):
    lst = (int, str, float)
    for i in list(lst):
        lst = (i)

def imprtlst(module, name): # para importar modulos que se encuentren dentro de las listas

    mylst = (module, name)

    for i in list(mylst):
        importlib.import_module(i)
        importlib.import_module(i)

def imprt(module, name): # para importar un modulo a la vez (función basica de python)
    import importlib
    importlib.import_module(module)
    importlib.import_module(name)

def intfloat(int, char, float):
    integ = (int)
    floating = (float)
    character = (char)
    if character == "+":
        integ + floating
    elif character == "-":
        integ - floating
    elif character == "*":
        integ * floating
    elif character == "/":
        integ / floating
    elif character == "^":
        integ ** floating
    elif character == "%":
        integ % floating
    elif character == "//":
        integ // floating
    elif character == ">>":
        integ >> floating
    elif character == "<<":
        integ << floating
    elif character == "&":
        integ & floating
    elif character == "|":
        integ | floating

def transtr(str): # para convertir un string a un entero
    transt = (str)
    if transt == "True":
        transt = (True)
    elif transt == "False":
        transt = (False)
    elif transt == "None":
        transt = (None)
    elif transt == "":
        transt = (None)
    elif transt == "0":
        transt = (0)
    elif transt == "1":
        transt = (1)
    elif transt == "2":
        transt = (2)
    elif transt == "3":
        transt = (3)
    elif transt == "4":
        transt = (4)
    elif transt == "5":
        transt = (5)
    elif transt == "6":
        transt = (6)
    elif transt == "7":
        transt = (7)
    elif transt == "8":
        transt = (8)
    elif transt == "9":
        transt = (9)
    return transt

# convierte un entero a un string 

def intstr(int):
    intstr = (int)
    if intstr == 0:
        intstr = "0"
    elif intstr == 1:
        intstr = "1"
    elif intstr == 2:
        intstr = "2"
    elif intstr == 3:
        intstr = "3"
    elif intstr == 4:
        intstr = "4"
    elif intstr == 5:
        intstr = "5"
    elif intstr == 6:
        intstr = "6"
    elif intstr == 7:
        intstr = "7"
    elif intstr == 8:
        intstr = "8"
    elif intstr == 9:
        intstr = "9"
    return intstr