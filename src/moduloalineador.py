#!/usr/bin/env python
# -*- coding: utf-8 -*-
#import sqlite3
import math
from itertools import izip
import mysql.connector
import modulopreprocesamiento
import codecs
#conexion a la base de datos
conn=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="bdveesavi")

#conn=sqlite3.connect("alineacionesdb.db")

def crearTablaAlineaciones():
    """Metodo para crear tabla de alineaciones"""
    global conn
    puntero=conn.cursor()
    puntero.execute("CREATE TABLE IF NOT EXISTS alineados(idalineacion int,oracionespaniol TEXT, oracionmixteco TEXT) ENGINE=InnoDB DEFAULT CHARSET=utf8;") 
    print("Tabla creada correctamente...")
 
crearTablaAlineaciones()

def consultarAlineaciones():
    """Metodo que permite consultar las alineaciones realizadas"""
    global conn
    puntero=conn.cursor()
    conn.text_factory = str
    puntero.execute('select oracionespaniol,oracionmixteco from alineados')
    datos=puntero.fetchall()
    listaalineaciones=[]
    for fila in datos:
        listaalineaciones.append(fila)
    return listaalineaciones

#consultarAlineaciones()
def consultar():
    global conn
    puntero=conn.cursor()
    #conn.text_factory = str
    print("alineaciones")
    puntero.execute('select*from alineados')
    for y in puntero:
        print(y)
    
consultar()

def consultaralineaciones():
    print("entrando a consultar")
    lista=[]
    lista=consultarAlineaciones()
    for fila in lista:
        print(str(fila[1]))
        
#consultaralineaciones()  
 
def eliminarTablaAlineaciones():
    global conn
    puntero=conn.cursor()
    puntero.execute("delete from alineados")
    conn.commit()
    print("se ha limpiado la tabla de alineados")

try:
    import scipy.stats.norm
    norm_logsf = scipy.stats.norm.logsf
except ImportError:
    def norm_cdf(z):
        """ Cumulative distribution for N(0, 1) """
        t = 1 / (1 + 0.2316419 * z)
        return (1 - 0.3989423 * math.exp(-z * z / 2) *
                ((((1.330274429 * t - 1.821255978) * t
                    + 1.781477937) * t - 0.356563782) * t + 0.319381530) * t)

    def norm_logsf(z):
        """ Logarithm of the survival function for N(0, 1) """
        try:
            return math.log(1 - norm_cdf(z))
        except ValueError:
            return float('-inf')

# Alignment costs: -100*log(p(x:y)/p(1:1))
bead_costs = {
     (1, 1): 0,
     (2, 1): 230,
     (1, 2): 230,
     (0, 1): 450,
     (1, 0): 450,
     (2, 2): 440
}

# Length cost parameters
mean_xy = 1
variance_xy = 6.8
LOG2 = math.log(2)

def length_cost(sx, sy):
    """ -100*log[p(|N(0, 1)|>delta)] """
    lx, ly = sum(sx), sum(sy)
    m = (lx + ly * mean_xy) / 2
    try:
        delta = (lx - ly * mean_xy) / math.sqrt(m * variance_xy)
    except ZeroDivisionError:
        return float('-inf')
    return - 100 * (LOG2 + norm_logsf(abs(delta)))


def _align(x, y):
    m = {}
    for i in range(len(x) + 1):
        for j in range(len(y) + 1):
            if i == j == 0:
                m[0, 0] = (0, 0, 0)
            else:
                m[i, j] = min((m[i-di, j-dj][0] +
                               length_cost(x[i-di:i], y[j-dj:j]) +
                               bead_cost,
                               di, dj)
                               for (di, dj), bead_cost in bead_costs.iteritems()
                               if i-di>=0 and j-dj>=0)

    i, j = len(x), len(y)
    while True:
        (c, di, dj) = m[i, j]
        if di == dj == 0:
            break
        yield (i-di, i), (j-dj, j)
        i -= di
        j -= dj


def char_length(sentence):
    """ Length of a sentence in characters """
    return sum(1 for c in sentence if c != ' ')

#metodo de alineacion 
def align(sx, sy):
    """ Align two groups of sentences """
    cx = map(char_length, sx)
    cy = map(char_length, sy)
    for (i1, i2), (j1, j2) in reversed(list(_align(cx, cy))):
        yield ' '.join(sx[i1:i2]), ' '.join(sy[j1:j2])

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
cuentaalineacion=0
def principal(rutasalida):
    
    listaespaniol=[]
    listamixteco=[]
    
    listaespaniol=modulopreprocesamiento.consultarcorpusespaniol()
    listamixteco=modulopreprocesamiento.consultarcorpusmixteco()
    
    for block_x,block_y in izip(listaespaniol,listamixteco):
        
        for (oracionorigen,oraciondestino) in align(block_x,block_y):
            
            global  totalelementos
            totalelementos+=1
            global conn
            posicion=conn.cursor()
            #cursor.text_factory = str
            
            oracionorigen=oracionorigen.encode("utf-8")
            oraciondestino=oraciondestino.encode("utf-8")
            
            posicion.execute("INSERT INTO alineados(idalineacion,oracionespaniol,oracionmixteco) values(%s,%s,%s)",(totalelementos,str(oracionorigen),str(oraciondestino)))
            
            print("----"+str(totalelementos))
            
            conn.commit()
            print("alineaciones insertadas correctamente...")

            print('%s ||| %s' % (oracionorigen, oraciondestino))
    
    archivo=codecs.open(rutasalida,encoding="utf8",mode="w")
    listaalineaciones=consultarAlineaciones()
    for x in listaalineaciones:
        global cuentaalineacion
        cuentaalineacion+=1
        texto=u"#espaniol##mixteco##"+x[0]+"##"+x[1]+'\n'
        archivo.write(texto)
        
    #archivo.write(" "+str(totalelementos)+" ")
    archivo.close()
    
eliminarTablaAlineaciones()
modulopreprocesamiento.limpiartablacorpusespaniol()
modulopreprocesamiento.limpiartablacorpusmixteco()
            
