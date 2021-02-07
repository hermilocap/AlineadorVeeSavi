#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mysql.connector

#conexion a la base de datos
conn=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="bdalineador")

def consultarcorpusespaniol(): 
    print("entrando al corpus espaniol-----")
    global conn
    puntero=conn.cursor()
    #conn.text_factory = str
    puntero.execute("select oracioncorpusespaniol from corpusespaniol")
    datos=puntero.fetchall()
    for dato in datos:
        print("corpus espaniol")
        #print(d[0])
        print(dato)

def consultarcorpusmixteco(): 
    print("entrando al corpus mixteco-----")
    global conn
    puntero=conn.cursor()
    #conn.text_factory = str
    puntero.execute("select oracioncorpusmixteco from corpusmixteco")
    datos=puntero.fetchall()
    for dato in datos:
        print("corpus mixteco")
        #print(d[0])
        print(dato)


def obteneroracionespaniol(idoracion):
    print("enetrando a obetener oracion en español")
    global conn
    cursor=conn.cursor()
    cursor.execute("select*from corpusespaniol where Idcorpusespaniol=%s",(idoracion,))
    consulta=cursor.fetchall()
    for oracion in consulta:
        print(str(oracion))
        
def obteneroracionmixteco(id):
    print("entrando a obtener oracion en mixteco")
    global conn
    cursor=conn.cursor()
    cursor.execute("select*from corpusmixteco where Idcorpusmixteco=%s",(id,))
    for sentencia in cursor:
        print(sentencia)
        
def alinear(idoracionespaniol,idoracionmixteco):    
    print("entrando a alinear oracion")
    if idoracionespaniol==idoracionmixteco:
        print("")


def guardarAlineaciones():
    global  totalelementos
    totalelementos+=1
    global conn
    posicion=conn.cursor()
    #cursor.text_factory = str
    posicion.execute("INSERT INTO alineados(idalineacion,oracionespaniol,oracionmixteco) values(%s,%s,%s)",(totalelementos,str(sentence_x),str(sentence_y)))
    conn.commit()
    print("alineaciones insertadas correctamente...")
                
