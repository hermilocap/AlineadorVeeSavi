#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import mysql.connector
import codecs
rutacorpusmixteco=""
rutacorpusespaniol=""
rutasalidacorpusmixteco=""
rutasalidacorpusespaniol=""
titulosalidamixteco=""
titulosalidacorpusespaniol=""

preprocesadoespn="preprocesadoespaniol"
preprocesadomixteco="preprocesadomixteco"

conn=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="bdveesavi")

#este metodo permite crear la base de datos
def crearDB():
    global conn
    cursor=conn.cursor()
    cursor.execute("SET sql_notes = 0;")
    cursor.execute("CREATE DATABASE IF NOT EXISTS bdalineador ")
    cursor.commit()
#crearDB()

#este metodo permite crear la tabla de corpus español
def creartablacorpusespaniol():
    """Metodo para crear tabla de textos prealineados"""
    global conn
    puntero=conn.cursor()
    puntero.execute('''CREATE TABLE IF NOT EXISTS corpusespaniol(idcorpusespaniol int,oracioncorpusespaniol text,titulocorpusespaniol text) ENGINE=InnoDB DEFAULT CHARSET=utf8;''')
    print("Tabla del español creada..")
 
creartablacorpusespaniol()

def creartablacorpusmixteco():
    """Metodo para crear tabla de textos prealineados"""
    global conn
    puntero=conn.cursor()
    puntero.execute('''CREATE TABLE IF NOT EXISTS corpusmixteco(idcorpusmixteco int,oracioncorpusmixteco text,titulocorpusmixteco text) ENGINE=InnoDB DEFAULT CHARSET=utf8;''')
    print("Tabla de corpus del mixteco creada..")
 
creartablacorpusmixteco()

def obtenertotalparrafoespaniol(ruta):
    archivoespaniol=open(ruta,"r")
    parrafoespaniol=0
    lineasespaniol=archivoespaniol.readlines()
    
    for clavelinea,lineaespaniol in enumerate(lineasespaniol):
        if not lineaespaniol == '\n':
            coincidencia=re.search(r'\w',lineaespaniol)
            str=coincidencia.group(0)
        try:
            if lineamixteco == '\n' and str in lineasespaniol[clavelinea-1]:
                parrafoespaniol +=1
                
        except:
            pass
        
    if lineasespaniol[-1] !='\n':
        parrafoespaniol +=1
        
    return parrafoespaniol
    #print("El corpus en espanol tiene: "+str(parrafo)+"parrafos")
    
def obtenertotalparrafomixteco(ruta):
    archivomixteco=open(ruta,"r")
    parrafomixteco=0
    
    lineasmixteco=archivomixteco.readlines()
    
    for clave,lineamixteco in enumerate(lineasmixteco):
        if not lineamixteco == '\n':
            coincidencia=re.search(r'\w',lineamixteco)
            str=coincidencia.group(0)
        try:
            if lineamixteco == '\n' and str in lineasmixteco[clave-1]:
                parrafomixteco +=1
        except:
            pass
        
    if lineasmixteco[-1] !='\n':
        parrafomixteco +=1
    
    return parrafomixteco

def obtenertotalpalabrasespaniol(ruta):
    
    lineas,lineablanca,oraciones,palabras= 0,0,0,0
    archivo=open(ruta,"r")
    for linea in archivo:
        lineas+=1
        if linea.startswith('\n'):
            lineablanca+=1
        else:
            tempalabras=linea.split(None)
            palabras+=len(tempalabras)
            
    return palabras 

def obtenertotaloracionesespaniol(ruta):
    lineas,lineablanca,oraciones,palabras= 0,0,0,0
    archivo=open(ruta,"r")
    for linea in archivo:
        lineas+=1
        if linea.startswith('\n'):
            lineablanca+=1
        else:
            oraciones+=linea.count('.')+linea.count('!')+linea.count('?')
            
    return oraciones


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
        

def segmentarCorpusMixteco(rutacorpusmixteco):
    """ Este metodo se encarga de segmentar los textos en mixteco """
    rutacorpusmixteco=rutacorpusmixteco.encode("utf-8")
    archivomixteco=open(rutacorpusmixteco,'r')
    global titulosalidamixteco 
    titulosalidamixteco=rutacorpusmixteco+preprocesadomixteco
    archivosalidamixteco=open(titulosalidamixteco,'w')
    patron=r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"

    textomixteco=archivomixteco.readlines()
    textojoin=''.join(textomixteco)
    subst = "\\n"
    resultado = re.sub(patron, subst, textojoin, 0, re.MULTILINE)
    if resultado:
        print (resultado)
    archivosalidamixteco.write(str(resultado.strip()))
    archivosalidamixteco.close()
    archivomixteco.close()

def obtenertitulomixteco(ruta):
    archivo=open(ruta,"r")
    contenido=archivo.readline()
    return contenido

totaloracionmixteco=0
def  guardarPreprocesadomixteco():
    global titulosalidamixteco
    archivomixteco=open(titulosalidamixteco,'r')
    titulomixteco=obtenertitulomixteco(titulosalidamixteco)
    
    for oracionmixteco in archivomixteco.readlines():
        if oracionmixteco.strip():
            print("entrando a guardar preprocesado en mixteco")
            global totaloracionmixteco
            totaloracionmixteco+=1
            global conn
            posicion=conn.cursor()
            #cursor.text_factory = str
            posicion.execute("INSERT INTO corpusmixteco(idcorpusmixteco,oracioncorpusmixteco,titulocorpusmixteco) values(%s,%s,%s)",(totaloracionmixteco,oracionmixteco.strip(),titulomixteco))
            conn.commit()
        
totaloracionespaniol=0
def segmentarCorpusEspaniol(rutacorpusespaniol):
    """ Este metodo se encarga de segmentar los textos en español"""
    archivoespaniol=open(rutacorpusespaniol,'r')
    global titulosalidacorpusespaniol
    titulosalidacorpusespaniol=rutacorpusespaniol+preprocesadoespn
    archivosalidaespaniol=open(titulosalidacorpusespaniol,'w')
    patron=r"(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s"
    textoespaniol=archivoespaniol.readlines()
    oracionespanjoin=''.join(textoespaniol)
    subst = "\\n"
    res_segmentado = re.sub(patron, subst, oracionespanjoin, 0, re.MULTILINE)
    if res_segmentado:
        print (res_segmentado)
        archivosalidaespaniol.write(str(res_segmentado.strip()))
        
    archivosalidaespaniol.close()
    archivoespaniol.close()
    
def obtenertituloespaniol(ruta):
    archivo=open(ruta,"r")
    contenido=archivo.readline()
    return contenido

def guardarPreprocesadoespaniol():
    global titulosalidacorpusespaniol
    archivoespaniol=open(titulosalidacorpusespaniol,'r')
    tituloespaniol=obtenertituloespaniol(titulosalidacorpusespaniol)
    
    for oracionespaniol in archivoespaniol.readlines():
        if  oracionespaniol.strip():
            print("entrando a preprocesado en español")
            global totaloracionespaniol
            totaloracionespaniol+=1
            global conn
            posicion=conn.cursor()
            #cursor.text_factory = str
            posicion.execute("INSERT INTO corpusespaniol(idcorpusespaniol,oracioncorpusespaniol,titulocorpusespaniol) values(%s,%s,%s)",(totaloracionespaniol,str(oracionespaniol.strip()),tituloespaniol))
            conn.commit()
            
def consultarcorpusespaniol(): 
    print("entrando al corpus espaniol-----")
    global conn
    listacorpusespaniol=[]
    puntero=conn.cursor()
    #conn.text_factory = str
    puntero.execute("select oracioncorpusespaniol from corpusespaniol")
    datos=puntero.fetchall()
    
    for dato in datos:
        print("corpus espaniol")
        #print(d[0])
        print(dato)
        listacorpusespaniol.append(dato)
    return listacorpusespaniol

def consultarcorpusmixteco(): 
    print("entrando al corpus mixteco-----")
    global conn
    listacorpusmixteco=[]
    puntero=conn.cursor()
    #conn.text_factory = str
    puntero.execute("select oracioncorpusmixteco from corpusmixteco")
    datos=puntero.fetchall()
    for dato in datos:
        print("corpus mixteco")
        #print(d[0])
        print(dato)
        listacorpusmixteco.append(dato)
        
    return listacorpusmixteco
def limpiartablacorpusespaniol():
    """Metodo eliminar corpus epaniol"""
    global conn
    cursor=conn.cursor()
    cursor.execute("DELETE FROM corpusespaniol")
    conn.commit()
    print("Se ha limpiado el corpus español")

def limpiartablacorpusmixteco():
    """Metodo"""
    global conn
    cursor=conn.cursor()
    cursor.execute("DELETE FROM corpusmixteco")
    conn.commit()
    print("Se ha limpiado el corpus mixteco")
