#Importamos libreria Tkinter para hacer interfaces gráficas
from tkinter import *

#Creación de ventana de calculadora

ventana = Tk()
ventana.title("Calculadora")
i = 0 #Contador


#Entrada de texto
entrada_texto = Entry(ventana, font=("Calibri 20"))
#Poner en pantalla
entrada_texto.grid(row = 0, column  = 0, columnspan = 4, padx = 5, pady = 5)

#Conectar los botones a la ventana, que el texto de lo que aprete se vea en la ventana.

#Definimos una función para cuando hagamos click
"""Las variables globales son aquellas que se definen fuera de una función y pueden ser 
accedidas desde cualquier parte del código
"""
def click_button(valor):
 global i
 entrada_texto.insert(i, valor)
 i = i+1

def borrar():
 entrada_texto.delete(0, END)
 i = 0

 #Eval, evalua ecuasiones

def operasiones():
 ecuasiones = entrada_texto.get()
 resultado = eval(ecuasiones)
 entrada_texto.delete(0, END)
 entrada_texto.insert(0, resultado)
 i = 0


#lambda metodo que permite escribir una funcion en una linea

#Botones númericos

boton1  = Button(ventana, text ="1", width=5, height=2, command= lambda: click_button(1))
boton2  = Button(ventana, text ="2", width=5, height=2, command= lambda: click_button(2))
boton3  = Button(ventana, text ="3", width=5, height=2, command= lambda: click_button(3))
boton4  = Button(ventana, text ="4", width=5, height=2, command= lambda: click_button(4))
boton5  = Button(ventana, text ="5", width=5, height=2, command= lambda: click_button(5))
boton6  = Button(ventana, text ="6", width=5, height=2, command= lambda: click_button(6))
boton7  = Button(ventana, text ="7", width=5, height=2, command= lambda: click_button(7))
boton8  = Button(ventana, text ="8", width=5, height=2, command= lambda: click_button(8))
boton9  = Button(ventana, text ="9", width=5, height=2, command= lambda: click_button(9))
boton0  = Button(ventana, text ="0", width=13, height=2, command= lambda: click_button(0))

#Botones borrarm parentesis y punto

boton_borrar  = Button(ventana, text ="del", width=5, height=2, command= lambda: borrar())
boton_parentesis1 = Button(ventana, text ="(", width=5, height=2, command= lambda: click_button("()"))
boton_parentesis2 = Button(ventana, text =")", width=5, height=2, command= lambda: click_button(")"))
boton_punto = Button(ventana, text =".", width=5, height=2, command= lambda: click_button("."))

#Botones de operadores
boton_suma = Button(ventana, text ="+", width=5, height=2, command= lambda: click_button("+"))
boton_resta = Button(ventana, text ="-", width=5, height=2, command= lambda: click_button("-"))
boton_mul = Button(ventana, text ="*", width=5, height=2, command= lambda: click_button("*"))
boton_div = Button(ventana, text ="/", width=5, height=2, command= lambda: click_button("/"))
boton_igual = Button(ventana, text ="=", width=5, height=2, command= lambda: operasiones())

#Agregar botones a pantalla acomodados por fila
#Fila 1 
boton_borrar.grid(row = 1, column = 0, padx = 5, pady = 5)
boton_parentesis1.grid(row = 1, column = 1 , padx = 5, pady = 5)
boton_parentesis2.grid(row = 1, column = 2 , padx = 5, pady = 5)
boton_div.grid(row = 1, column = 3, padx = 5, pady = 5)

#Fila 2
boton7.grid(row = 2, column = 0, padx = 5, pady = 5)
boton8.grid(row = 2, column = 1 , padx = 5, pady = 5)
boton9.grid(row = 2, column = 2 , padx = 5, pady = 5)
boton_mul.grid(row = 2, column = 3, padx = 5, pady = 5)

#Fila 3
boton4.grid(row = 3, column = 0, padx = 5, pady = 5)
boton5.grid(row = 3, column = 1 , padx = 5, pady = 5)
boton6.grid(row = 3, column = 2 , padx = 5, pady = 5)
boton_resta.grid(row = 3, column = 3, padx = 5, pady = 5)

#Fila 4
boton1.grid(row = 4, column = 0, padx = 5, pady = 5)
boton2.grid(row = 4, column = 1 , padx = 5, pady = 5)
boton3.grid(row = 4, column = 2 , padx = 5, pady = 5)
boton_suma.grid(row = 4, column = 3, padx = 5, pady = 5)

#Fila 5
boton0.grid(row = 5, column = 0, columnspan= 2, padx = 5, pady = 5)
boton_igual.grid(row = 5, column = 2, padx = 5, pady = 5)
boton_punto.grid(row = 5, column = 3, padx = 5, pady = 5)

#mainloop, reconoce los eventos que pasen.
ventana.mainloop()