from cProfile import label
from multiprocessing.sharedctypes import Value
import tkinter
from tkinter import *
import math
from turtle import clear
from unittest import result


obj=Tk()
obj.title("Calculator")
obj.geometry("570x600+100+200")
obj.resizable(False,False)
obj.configure(bg="#17161b")



equation=""
def show(Value):
    global equation
    equation+=Value
    label_result.config(text=equation)
def clear():
    global equation
    equation=""
    label_result.config(text=equation)
    
    
def calculate():
    global equation
    result=""
    if equation !="":
        try:
            result=eval(equation)
        except:
            result="Error"
            equation=""
    label_result.config(text=result)

label_result=Label(obj,width=25,height=2,text="",font=("arial",30))
label_result.pack()

Button(obj,text="C",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#3697f5",command=lambda:clear()).place(x=10,y=100)
Button(obj,text="%",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda: show("%")).place(x=150,y=100)
Button(obj,text="/",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show("/")).place(x=290,y=100)
Button(obj,text="*",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda:show("*")).place(x=430,y=100)


Button(obj,text="7",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show("7")).place(x=10,y=200)
Button(obj,text="8",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show("8")).place(x=150,y=200)
Button(obj,text="9",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show("9")).place(x=290,y=200)
Button(obj,text="-",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show("-")).place(x=430,y=200)

Button(obj,text="4",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show("4")).place(x=10,y=300)
Button(obj,text="5",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show("5")).place(x=150,y=300)
Button(obj,text="6",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show("6")).place(x=290,y=300)
Button(obj,text="+",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show("+")).place(x=430,y=300)

Button(obj,text="1",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show("1")).place(x=10,y=400)
Button(obj,text="2",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show("2")).place(x=150,y=400)
Button(obj,text="3",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show("3")).place(x=290,y=400)
Button(obj,text="0",width=11,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show("0")).place(x=10,y=500)

Button(obj,text=".",width=5,height=1,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#2a2d36",command=lambda : show(".")).place(x=290,y=500)
Button(obj,text="=",width=5,height=3,font=("arial",30,"bold"),bd=1,fg="#fff",bg="#fe9037",command= lambda : calculate()).place(x=430,y=400)



obj.mainloop()