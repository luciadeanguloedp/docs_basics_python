

# -*- coding: utf-8 -*-
"""
PRÁCTICA EXAMEN FINAL - 17/01/2023
PROGRAMACIÓN II
PROFESORA: CYNTHYA GARCÍA DE JESÚS

EXAMEN FINAL - INTERFAZ PARA CREAR PLAYLIST DE CANCIONES EN EXCEL (contiene cancion, album y autor),
ELIMINAR ELEMENTOS, MODIFICARLOS Y AÑADIR NUEVOS
 Y MOSTRARLOS

@author: Lucía de Angulo, Paula Diz, Jimena Miniño
"""

from tkinter import*
import pandas as pd
#CREAMOS LA VENTANA (RAÍZ)
win = Tk()
win.config(bg='pink')
win.geometry('800x400')
win.title('Guardar datos de la playlist en Excel')
win.iconbitmap("playlist.ico")
cancion1,autor1,album1= [],[],[]


def agregardatos():
	global cancion1, autor1, album1

	cancion1.append(cancion.get())
	autor1.append(autor.get())
	album1.append(album.get())
    
    #se borran los elementos de la interfaz para poder añadir otros nuevos 
	cancion.delete(0,END)
	autor.delete(0,END)
	album.delete(0,END)

def guardardatos():	
	global cancion1,autor1,album1
	datos = {'Cancion':cancion1,'Autor':autor1, 'Album':album1} 
	nomfich  = str(fich.get() + ".xlsx")	
	df = pd.DataFrame(datos,columns = ['Cancion', 'Autor', 'Album']) 
	df.to_excel(nomfich)
	fich.delete(0,END)


#CREAMOS DOS FRAMES
frame1 = Frame(win, bg='pink')
frame1.grid(column=0, row=0, sticky='nsew')
frame2 = Frame(win, bg='pink')
frame2.grid(column=1, row=0, sticky='nsew')

texto = Label(frame1, text ='El Excel entregado ya tiene datos, \npero si desea puede introducir los suyos propios', width=40).grid(column=1, row=6, pady=20, padx= 20)


cancion = Label(frame1, text ='Cancion', width=10).grid(column=0, row=0, pady=20, padx= 10)
cancion = Entry(frame1,  width=20, font = ('Arial',12))
cancion.grid(column=1, row=0)

autor = Label(frame1, text ='Autor', width=10).grid(column=0, row=1, pady=20, padx= 10)
autor = Entry(frame1, width=20, font = ('Arial',12))
autor.grid(column=1, row=1)

album = Label(frame1, text ='Album', width=10).grid(column=0, row=2, pady=20, padx= 10)
album = Entry(frame1,  width=20, font = ('Arial',12))
album.grid(column=1, row=2)



agregar = Button(frame1, width=20, font = ('Arial',12, 'bold'), text='Agregar', bg='pink',bd=5, command =agregardatos)
agregar.grid(columnspan=2, row=5, pady=20, padx= 10)

archivo = Label(frame2, text ='Ingrese nombre del archivo\n donde desea guardar los datos\n(en este caso escriba "playlist")', width=25, bg='pink',font = ('Arial',12, 'bold'), fg='black')
archivo.grid(column=0, row=0, pady=10, padx= 10)

fich = Entry(frame2, width=23, font = ('Arial',12),highlightbackground = "green", highlightthickness=4)
fich.grid(column=0, row=1, pady=1, padx= 10)
nomfich  = str(fich.get() + ".xlsx")

guardar = Button(frame2, width=20, font = ('Arial',12, 'bold'), text='Guardar', bg='pink',bd=5, command =guardardatos)
guardar.grid(column=0, row=2, pady=20, padx= 10)


win.mainloop()

#MENÚ DE OPCIONES
df = pd.read_excel("playlist.xlsx")
op = 0
while(op!=5):
    op = int(input("\nAhora introduzca qué desea hacer:\n\t1.Eliminar elemento\n\t2.Modificar elemento\n\t3.Visualizar canciones\n\t4.Introducir otra canción\n\t5.Salir  "))
    if(op==1):
        print("ELIMINAR ELEMENTO\n")
        elem_elim = input("Introduzca el nombre de la canción que desea eliminar: ")
        df.drop(df[(df['Cancion'] == elem_elim)].index, inplace=True)
        df.to_excel("playlist.xlsx", index = False)
        
    elif(op==2):
        cancion_modif = input("Introduzca la cancion que desea modificar: ")
        index = df.index[df['Cancion'] == cancion_modif].tolist()[0]
        #print(indice) #indice de la fila del excel donde se encuentra la cancion a modificar
        canc_modif = input("\nIntroduzca la nueva canción: ")
        autor_modif = input("\nIntroduzca el nuevo autor: ")
        album_modif = input("\nIntroduzca el nuevo album: ")
        df.iat[index, 1] = canc_modif
        df.iat[index, 2] = autor_modif
        df.iat[index, 3] = album_modif
        df.to_excel("playlist.xlsx", index = False)
    elif(op==3):
        print("VISUALIZANDO CONTENIDO DE LA PLAYLIST...")
        print(df)
    elif(op==4):
        print("INTRODUCIR OTRA CANCIÓN: ")
        nueva_cancion = input("\nIntroduzca el nombre de la canción: ")
        nuevo_autor = input("\nIntroduzca el nombre del autor: ")
        nuevo_album = input("\nIntroduzca el nombre del album: ")
        num_filas = len(df)
        contenido_celda =int(df.at[num_filas,"Unnamed: 0"])
        datos2 = pd.DataFrame({'Unnamed: 0':[contenido_celda+1],'Cancion':[nueva_cancion],'Autor':[nuevo_autor],'Album':[nuevo_album]})
        df = pd.concat([df,datos2],ignore_index=True)
        df.to_excel("playlist.xlsx", index = False,engine='openpyxl')
        
    elif(op==5):
        print("Saliendo...")
    else:
        print("Opción incorrecta.  Escoja otra.\n")
    

    