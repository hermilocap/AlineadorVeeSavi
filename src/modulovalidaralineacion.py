#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
from itertools import izip
import mysql.connector

#conexion a la base de datos
conn=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="bdveesavi")

def crearTablaPrealineado():
    """Metodo para crear tabla de textos prealineados"""
    global conn
    puntero=conn.cursor()
    puntero.execute('''CREATE TABLE IF NOT EXISTS prealineados(idprealineado int,preoracionespaniol text, preoracionmixteco text) ENGINE=InnoDB DEFAULT CHARSET=utf8;''')
    print("Tabla de prealineados creada..")
 
crearTablaPrealineado()

caracteres=["(u'","',)"]
def borrarCaracteres(texto):
    for caracter in caracteres:
        texto=texto.replace(caracter,"")
    return texto


diagonal=['\n']
def borrarDiagonal(oracion):
    for letra in diagonal:
        oracion=oracion.replace(letra,"")
    return oracion

def read_blocks(f):
    block = []
    for l in f:
        if not l.strip():
            yield block
            block = []
        else:
            block.append(l.strip())
    if block:
        yield block
        
totalelementos=0

def readfile():
    print("readfiles preadlineados")
    
    # open("prealineados/derechopacientemix.txt") as corpusespn:
    with open("prealineados/derechopacientes.txt") as corpusespn,open("prealineados/derechopacientemix.txt") as corpusmix:
            for line1,line2 in izip(corpusespn,corpusmix):
                if line1 and line2:
                    global conn 
                    global totalelementos
                    totalelementos+=1
                    cursor=conn.cursor()
                #   cursor.text_factory = str
                    cursor.execute("INSERT INTO prealineados(idprealineado,preoracionespaniol,preoracionmixteco) values(%s,%s,%s)",(totalelementos,line1.strip(),line2.strip()))
                    conn.commit()
                    
    print("Textos preallineados insertados correctamente")
  
def leerPrealineados():
    """Metodo para leer contenido prealineado y guardar en base de datos"""
    print("entrando a prealineados")
    archivoalineadoespn=open("prealineados/derechopacientes.txt","r")
    orespn=archivoalineadoespn.readlines()
    print("desde aqui empieza el salto de linea")
    print(orespn)
    archivoalineadoespn.close()
    
    archivoalineadomix=open("prealineados/derechopacientemix.txt","r")
    ormix=archivoalineadomix.readlines()
    archivoalineadomix.close()
    
    for x,y in izip(read_blocks(orespn),read_blocks(ormix)):
        print("blocks")
        print(x)
        global conn 
        global totalelementos
        totalelementos+=1
        cursor=conn.cursor()
    #   cursor.text_factory = str
        cursor.execute("INSERT INTO prealineados(idprealineado,preoracionespaniol,preoracionmixteco) values(%s,%s,%s)",(totalelementos,str(x),str(y)))
        conn.commit()
    
    print("Textos prealineados insertados correctamente...")

#leerPrealineados()

def consultarcorpusespaniol(): 
    global conn
    puntero=conn.cursor()
    #conn.text_factory = str
    puntero.execute("select*from Prealineados")
    datos=puntero.fetchall()
    for d in datos:
        print("corpusprealineadopruebaccdcd")
        #print(d[0])
        print(d)
#        cad=str(d)
#        cd=cad.strip()
#        print (cd)
        
consultarcorpusespaniol()

def consultarTablaPrealineados():
    """Metodo para consultar Prealineados"""
    global conn
    puntero=conn.cursor()
    #conn.text_factory = str
    puntero.execute("select preoracionespaniol,preoracionmixteco from prealineados")
    datos=puntero.fetchall()
    
    listaprealineados=[]
    
    for fila in datos:
        print("prealineados en español")
        print(str(fila))
        listaprealineados.append(fila)
        
    return listaprealineados

def consultarTablaPrealineadosmixteco():
    """Metodo para consultar Prealineados"""
    global conn
    puntero=conn.cursor()
    #conn.text_factory = str
    puntero.execute("select preoracionmixteco from prealineados")
    datos=puntero.fetchall()
    
    listaprealineados=[]
    
    for fila in datos:
        print("prealineados mixteco")
        print(fila)
        listaprealineados.append(fila)
        
    return listaprealineados

#consultarTablaPrealineados()

def consultarTablaAlineados():
    """Metodo para consultar alineados"""
    cursor=conn.cursor()
    #conn.text_factory=str
    cursor.execute("select oracionespaniol,oracionmixteco from alineados")
    almacen=cursor.fetchall()
    
    listaalineados=[]
    
    for row in almacen:
        print("alineados")
        print(str(row))
        listaalineados.append(row)
        
    return listaalineados

#consultarTablaAlineados()

def consultarTablaAlineadosmixteco():
    """Metodo para consultar alineados"""
    cursor=conn.cursor()
    #conn.text_factory=str
    cursor.execute("select oracionmixteco from alineados")
    almacen=cursor.fetchall()
    
    listaalineados=[]
    
    for row in almacen:
        print("alineados mixteco")
        print(row)
        listaalineados.append(row)
        
    return listaalineados

def calcularprecision(nalcorrecta,nalrecuperadas):
    """ PRECISION
    Número de alineaciones correctas
    Número de alineaciones propuestas	
    """
    precision=100*nalcorrecta/nalrecuperadas
    return precision

def calclularcobertura(nalcorrecta,nalpertrec):
    """
    COBERTTURA
    Número de alineaciones correctas
    Número de alineaciones de referencia=gual los ya alineados
    """
    cobertura=100*nalcorrecta/nalpertrec
    return cobertura

def evaluaralineador(rutaeval):
    
    print("entrando a evaluar")
    
    realineaciones=consultarTablaAlineados()
    reprealineados=consultarTablaPrealineados()
#    realineacionesmixteco=consultarTablaAlineadosmixteco()
#    reprealineadosmixteco=consultarTablaPrealineadosmixteco()
    
    sumacorrectos=0
    sumaincorrectos=0
    totalrecuperadas=0
    
    listacorrectos=[]
    listaincorrectos=["los niños son altos","na kuaxi"]
    
    for i,d in zip(realineaciones,reprealineados):
        print("entrando a comparar en mixteco")
        if i==d:
            print("son iguales")
            listacorrectos.append(i)
            archivoeval=open(rutaeval,"w")
            for x in listacorrectos:
                print("correctos")
                #cadena=x.encode("utf-8")
                #decodificado=cadena.decode("utf-8")
                cadena=str(x)
                cadlimpia=cadena.strip()
                cad=cadlimpia+'\n'
                archivoeval.write(str(cad.strip())+'\n')
                print(x)
            archivoeval.close()

            archivoeval=open(rutaeval,"a")
            for y in listaincorrectos:
                 print("incorrectos")
                 print(y)
                 if y!="":

                    archivoeval.write(str(y))
                 else:
                     print("este archivo esta vacio...")
            archivoeval.close()
        else:
            print("son diferentes")
            listaincorrectos.append(d)
    
    #sumando total correcos
    archivo=open(rutaeval,"a")
    
    sumacorrectos=len(listacorrectos)
    print("total de alineaciones correctas: "+str(sumacorrectos))
    
    sumaincorrectos=len(listaincorrectos)
    print("total de alineaciones incorrectas: "+str(sumaincorrectos))
    
    totalrecuperadas=sumacorrectos+sumaincorrectos
    print("total recuperadas: "+str(totalrecuperadas))
    
    precision=calcularprecision(sumacorrectos,totalrecuperadas)
    print("la precision en este documento fue de: "+str(precision))
    
    recall=calclularcobertura(sumacorrectos,12)
    print("la cobertura en este documento fue de: "+str(recall))
    
    archivo.write('\n'+"Precision: "+str(precision)+" "+"Recall: "+str(recall)) 
    archivo.close()
    
def eliminarTablaPrealineados():
    """Metodo"""
    global conn
    conn.execute("DELETE FROM Prealineados")
    conn.commit()
