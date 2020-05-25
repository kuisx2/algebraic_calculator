# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:26:00 2020

@author: facundo munho
"""
# =============================================================================# 
#imports 
# =============================================================================
import matplotlib.pyplot as plt
import random
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# =============================================================================
# =============================================================================
# funciones
# =============================================================================
def ingreso_vector_en_una_frase():
    vector=list(input())
    vector_lineal=[]
    i=0
    while i<=len(vector):
        if (i)<len(vector) and vector[i]!=",":
            numero=int(vector[i])
            while (i+1)<len(vector) and vector[i+1]!=",":
                d=int(vector[i+1])
                numero=(numero*10+d)
                i=i+1
            vector_lineal.append(numero)

        i=i+1
    return vector_lineal
# =============================================================================
def ingresar_vectores(dimension):
    vector=[]
    for i in range(dimension):
        posicion=i+1
        print("ingrese el valor de la posicion",posicion)
        x=int(input())
        vector.append(x)
    return vector
# =============================================================================
def suma_vectorial(vectores):
    resultado=[]
    for i in range(len(vectores[0])):
        suma=0
        for j in range(len(vectores)):
            vector=vectores[j]
            suma=suma+vector[i]
        resultado.append(suma)
    return resultado
# =============================================================================
def resta_vectorial(vectores):
    resultado=[]
    for i in range(len(vectores[0])):
        suma=0
        for j in range(len(vectores)):
            vector=vectores[j]
            suma=suma-vector[i]
        resultado.append(suma)
    return resultado
# =============================================================================
def producto_escalar(k,vector):
    resultado=[]
    for i in vector:
        numero = i
        resultado.append(k*numero)
    return resultado
# =============================================================================
def producto_interno(vectorA,vectorB):
    suma=0
    for i in range(len(vectorA)):
        producto=vectorA[i]*vectorB[i]
        suma=suma+producto  
    return suma
# =============================================================================
def norma(vector):
    suma=0
    for i in vector:
        cuadrado=i**2
        suma=suma+cuadrado
        resultado=np.sqrt(suma)
    return resultado
# =============================================================================
def distancia_entre_vectores(vectores):
    if len(vectores)<=2:
        vector=resta_vectorial(vectores)
        resultado=norma(vector)
        return resultado
    else:
        print("demasiado valores")       
# =============================================================================
def factor_vectorial(A,B,dimension):
    if dimension == 3:
        x=A[1]*B[2]-A[2]*B[1]
        y=A[2]*B[0]-A[0]*B[2]
        z=A[0]*B[1]-A[1]*B[0]
        vector_resultante=[x,y,z]
    return vector_resultante    
# =============================================================================
# programa
# =============================================================================    
def main():
    seguir="S"
    Vectores=[]
    arrastre=[]
    k=[]
# =============================================================================
    while seguir=="S":
        print("=============================================================================")
        print("seleccionar operacion(help para las opciones):")
        operacion=str(input())
# =============================================================================
        if operacion=="help":
            print("las posibles operaciones son")
            print("suma")
            print("resta")
            print("producto_escalar")
            print("producto_interno")
            print("producto_vectorial")
            print("norma")
            print("distancia_entre_vectores")
            print("=============================================================================")
            return main()
# =============================================================================
        if operacion=="suma":
            print("ingrese dimension")
            dimension=int(input())            
            agregarvector="S"
            while agregarvector=="S":
                vector=ingresar_vectores(dimension)
                Vectores.append(vector)
                print("¿agregar otro vector? S/N")
                agregarvector=str(input()).upper()
            resultado=suma_vectorial(Vectores)
            print (resultado)
# =============================================================================
        if operacion=="resta":
            print("ingrese dimension")
            dimension=int(input())
            agregarvector="S"
            while agregarvector=="S":
                vector=ingresar_vectores(dimension)
                Vectores.append(vector)
                print("¿agregar otro vector? S/N")
                agregarvector=str(input()).upper()
            resultado=resta_vectorial(Vectores)
            print (resultado)
# =============================================================================
        if operacion == "producto_escalar":
            print("ingrese dimension")
            dimension=int(input())
            print("ingrese un vector")
            vector=ingresar_vectores(dimension)
            if k==[]:
                print("inserte escalar")
                k=int(input())
            else:
                if arrastre!=[]:
                    k=arrastre
            resultado=producto_escalar(k,vector)
            print(resultado)
# =============================================================================
        if operacion=="producto_interno":
            print("ingrese dimension")
            dimension=int(input())
            print("ingrese_primer_vector")
            vectorA=ingresar_vectores(dimension)
            print("ingrese_segundo_vector")
            vectorB=ingresar_vectores(dimension)
            resultado=producto_interno(vectorA,vectorB)
            print (resultado)
# =============================================================================
        if operacion=="norma":
            print("ingrese dimension")
            dimension=int(input())
            vector=ingresar_vectores(dimension)
            resultado=norma(vector)
            print (resultado)
# =============================================================================
        if operacion=="distacia_entre_vectores":
            print("seleccione dimension")
            dimensiones=int(input())
            vectores=[]
            for i in range (2):
                vectores.append(ingresar_vectores(dimensiones))
            resultado=(distancia_entre_vectores(vectores))
            print(resultado) 
# =============================================================================
        if operacion=="factor_vectorial":
            print("ingrese dimension")
            dimension=int(input())
            A=ingresar_vectores(dimension)
            B=ingresar_vectores(dimension)
            resultado=(factor_vectorial(A,B,dimensiones))
            print(resultado)
# =============================================================================
        print("=============================================================================")
        print("¿desea guardar resultado? S/N")
        Vectores.clear()
        Guardar_valor=str(input()).upper()      
        if Guardar_valor=="S":
            if len(resultado)>1:
                Vectores.append(resultado)
            else:
                arrastre=resultado            
#                print(Vectores)
        print("=============================================================================")
        print("¿desea seguir? S/N")
        seguir=str(input()).upper()
        print("=============================================================================")

    return print("gracias por usar este programa")
# =============================================================================

