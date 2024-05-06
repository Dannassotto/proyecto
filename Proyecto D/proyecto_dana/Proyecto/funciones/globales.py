from os import system
import sys
from enum import Enum

def borrar_pantalla():
    if sys.platform=="lunx" or sys.platform== "darwin":
        system("clear")
    else:
        system("cls")

def pausar_pantalla():
    if sys.platform =="linux" or sys.platform=="darwin":
        x=input("Presione enter para continuar ")
    else:
        system("pause ")

centromedico={
    "Datas_usuarios": {}
}


Centromedico={
    "Datos_medicos": {}
}


centroMedico={
    "Datas_citas": {}
}