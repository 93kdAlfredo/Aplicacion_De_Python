#from tkinter import tk, Label,Button,Entry
from tkinter import *
vent = Tk()
vent.title("Ejemplo de place")
vent.geometry("400x200")

def fnsuma():

    n1=txt1.get()
    n2=txt2.get()  
    r=float(n1)+float(n2)
    txt3.delete(0,'end')
    txt3.insert(0,r)

# Crear la primera etiqueta del primer numero.

etiqueta =  Label(vent, text="Primer numero", bg="yellow")
etiqueta.place(x=10,y=10, width= 100, height=30)

#Se crea el campo donde seingresa el primer numero
txt1 = Entry(vent, bg="pink")
txt1.place(x=120, y=10, width="100", height=30)

#Crear la segunda etiqueta del segundo numero
etiqueta2 =  Label(vent, text="Segundo numero", bg="yellow")
etiqueta2.place(x=10,y=50, width= 100, height=30)

#Se crea el campo donde se ingresara el segundo numero
txt2 = Entry(vent, bg="pink")
txt2.place(x=120, y=50, width=100, height=30)

#Crea el boton suma, que hara la operacion
btn1 = Button(vent,text="Sumar", command=fnsuma)
btn1.place(x=240, y=50, width=80, height=30)
#Se crea la etiqueta del resultados
etiqueta3 =  Label(vent, text="Resultado", bg="yellow")
etiqueta3.place(x=10,y=120, width= 100, height=30)

#Se crea el campon donde se imprimira el resultado de la suma#
txt3 = Entry(vent, bg="pink")
txt3.place(x=120, y=120, width=100, height=30)

vent.mainloop()
