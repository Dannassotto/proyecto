import main
import funciones.especialistas as fe
import funciones.globales as gf
def menuDoctores(op):
    title = """
    >>==== REGISTRO MEDICOS  ====<<
    """
    menuDoctoresOp= '1. Agregar\n2. Editar\n3. Eliminar\n4. Salir'
    gf.borrar_pantalla()
    if(op !=4):
        print(title)
        print(menuDoctoresOp)
        try:
            opcion = int(input(">"))
        except ValueError:
            print("La opción no tiene formato adecuado")
            gf.pausar_pantalla()
            menuDoctores(0)
        else:
            if opcion == 1:
                    fe.Rdoctores(op)
            elif opcion == 2:
                    fe.modificar_datas()
            elif opcion == 3:
                    fe.eliminar_medico()
            elif opcion == 4:
                main.mainMenu(0)
            else:
                    print("Espero que hayas tenido un buen servicio")
            
                    menuDoctores(op)
