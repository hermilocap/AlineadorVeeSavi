#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkFileDialog
import re
import tkFont
import tkMessageBox
import math
import os
from itertools import izip
import moduloalineador
import modulopreprocesamiento
import modulovalidaralineacion
import moduloalineacion

sourcecorpus=""
targetcorpus=""

salida=""

rutaguardarsource=""
rutaguardartarjet=""

procsource=""
proctarjet=""

rutasalidaeval=""

ventana = Tk()

def abrirTextoEspaniol():
    global sourcecorpus
    sourcecorpus=tkFileDialog.askopenfilenames()
    textoespn_str.set(sourcecorpus)
    return sourcecorpus

def abrirTextoMixteco():
    global targetcorpus
    targetcorpus=tkFileDialog.askopenfilenames()
    textomixteco_str.set(targetcorpus)
    return targetcorpus      

caracteres=["('","',)"]
def borrarCaracteres(texto):
    for caracter in caracteres:
        texto=texto.replace(caracter,"")
    return texto
    
def guardarCorpus():
    global salida
    salida=tkFileDialog.asksaveasfilename()
    textosalida_str.set(salida)
    return salida

def limpiaralineacion():
    moduloalineador.eliminarTablaAlineaciones()
    
def limpiarpreprocesado():
    modulopreprocesamiento.limpiartablacorpusespaniol()
    modulopreprocesamiento.limpiartablacorpusmixteco()
    tkMessageBox.showinfo("Información","Los textos se han limpiado")
    
def alinear():
   global sourcecorpus
   global targetcorpus
   global salida
   print(sourcecorpus)
   print(targetcorpus)
   print(salida)
   origen=borrarCaracteres(str(sourcecorpus))
   destino=borrarCaracteres(str(targetcorpus))
   memoria=borrarCaracteres(str(salida))
   
   if memoria=="":
       tkMessageBox.showwarning("Advertencia","Por favor, seleccione su ruta para guardar")
       
   else:
    
    modulopreprocesamiento.segmentarCorpusEspaniol(origen)
    modulopreprocesamiento.segmentarCorpusMixteco(destino)
    #guardando los procesados a bd
    modulopreprocesamiento.guardarPreprocesadoespaniol()
    modulopreprocesamiento.guardarPreprocesadomixteco()
    
    moduloalineador.principal(memoria)
    tkMessageBox.showinfo("Alinear","Textos alineados correctamente")
       

ventana.title("Sistema de alineación automático español-mixteco VE'E SAVI")

#ventana.config(bg="#c1bfea")
#ventana.geometry("500x300")
ventana.resizable(width=FALSE, height=FALSE)
#ventana.resizable(width=500,height=500)
ventana.winfo_screenwidth()
Arial = tkFont.Font(family="Arial", size=12, weight="bold")


rutaespnproc_label = Label(ventana,text="Archivo de texto en español:",font=Arial)
rutaespnproc_label.grid(row=0, column=0)

textoespn_str = StringVar()
txtespnproc_entry = Entry(ventana,textvariable=textoespn_str,font=Arial)
#txtespn_entry = Label(ventana,text=" ",font=Arial)
txtespnproc_entry.grid(row=0, column=1,ipadx=6, ipady=6)
txtespnproc_entry.configure(width=40)

btnAbrirespn = Button(ventana,text="Seleccionar",background="#207ce5",foreground="#fff",anchor="center",font=Arial,command=abrirTextoEspaniol)
btnAbrirespn.grid(row=0, column=2,ipadx=6, ipady=6)

rutamixtecoproc_label= Label(ventana,text="Archivo de texto en mixteco:",font=Arial)
rutamixtecoproc_label.grid(row=1, column=0)

textomixteco_str = StringVar()
txtmixtecoproc_entry = Entry(ventana,textvariable=textomixteco_str,font=Arial)
txtmixtecoproc_entry.grid(row=1, column=1,ipadx=6, ipady=6)
txtmixtecoproc_entry.configure(width=40)

btnrutamixteco = Button(ventana,text="Seleccionar", background="#207ce5",anchor="center",font=Arial,foreground="#fff",command=abrirTextoMixteco)
btnrutamixteco.grid(row=1, column=2,ipadx=6, ipady=6)

btnalinear = Button(ventana,text="Alinear", background="#207ce5",anchor="center",font=Arial,foreground="#fff",command=alinear)
btnalinear.grid(row=2, column=1,ipadx=6, ipady=6)

rutasalidamixteco_label= Label(ventana,text="Ruta de salida:",font=Arial)
rutasalidamixteco_label.grid(row=3, column=0)

textosalida_str = StringVar()
textosalida_entry = Entry(ventana,textvariable=textosalida_str,font=Arial)
textosalida_entry.grid(row=3, column=1,ipadx=6, ipady=6)
textosalida_entry.configure(width=40)

btnsalida = Button(ventana,text="Guardar", background="#207ce5",anchor="center",font=Arial,foreground="#fff",command=guardarCorpus)
btnsalida.grid(row=3, column=2,ipadx=6, ipady=6)
btnsalida.configure()

ventana.mainloop()
