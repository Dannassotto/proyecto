import modules.corefiles as cf
import modules.data_M as M
import modules.data_C as md
import ui.uidoctores as D
import ui.citas as C
import ui.uiUsuarios as U
import ui.historial as H
import funciones.globales as gf

def mainMenu(op):
    title= """
    >>==== REGISTRO USUARIOS  ====<<
    """
    mainMenuOp= "1. Gestion de citas\n2 Registros de Usuarios\n3 Registro especialista\n4 Historial usuarios"
    if(op!=4):
        print(title)
        print(mainMenuOp)
        try:
            opcion = int(input(">"))
        except ValueError:
            print("error de opcion")
            mainMenu(0)
        else:
            if opcion ==1:
                C.Menucitas(0)
            elif opcion == 2:
                U.menuUsuarios(0)
            elif opcion == 3:
                D.menuDoctores(0)
            elif opcion == 4:
                H.menuhistorial(0)
            else:
                    print("La opcion no es correcta")
                    mainMenu(opcion)
if __name__=="__main__":
    cf.MY_DATABASE= "data/usuarios.json"
    M.MY_MEDICOS= "data/especialistas.json"
    md.MY_C= "data/citasp.json"
    cf.checkFile(gf.centromedico)
    md.checkFile(gf.centroMedico)
    M.checkFile(gf.Centromedico)
    mainMenu(0)                   