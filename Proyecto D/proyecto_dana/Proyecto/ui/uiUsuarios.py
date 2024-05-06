import funciones.usuarios as st
import funciones.globales as gf

def menuUsuarios(op):
    title = """
    >>==== REGISTRO USUARIOS  ====<<
    """
    menuUsuariosOp= '1.Agregar\n2. Editar\n3. Eliminar\n4. Salir'
    gf.borrar_pantalla()
    if(op !=4):
        print(title)
        print(menuUsuariosOp)
        try:
            op= int(input(":"))
        except ValueError:
            print("opcion no tiene formato adecuado")
            menuUsuarios(0)
        else:
            if op == 1:
                st.RUsuario(0)
            elif op == 2:
                st.modificar_data()
            elif op == 3:
                st.eliminar_usuario()
            elif op == 4:
                import main
                main.mainMenu(0)
            else:
                print("opcion no valida")
                menuUsuarios(op)