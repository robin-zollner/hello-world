from arrow import *
def drawText(t = arrow(1,2)):
    import PySimpleGUI as sg
    sg.Window(title="Drawing Text Arrows", layout=[[sg.Text(t)]], margins=(100, 50)).read()
    
