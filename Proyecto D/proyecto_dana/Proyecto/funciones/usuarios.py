import funciones.globales as gf
import modules.corefiles as cf
import ui.uiUsuarios as U

def RUsuario(op):
    title = """
    *****************************
    *  REGISTRO DE USUARIOS    *
    *****************************
    """ 
    gf.borrar_pantalla()
    print(title)
    try:
        Identificacion = int(input("ingrese Nro de Identificacion: "))
        print("Seleccione el Género:")
        print("  1. Hombre")
        print("  2. Mujer")
        print("  3. Otro")
    
        opcion_genero = input("Ingrese la Opcion: ")
        if opcion_genero == "1":
            Genero = "Hombre"
        elif opcion_genero == "2":
            Genero = "Mujer"
        elif opcion_genero == "3":
            Genero = "Otro"
        else:
            print("Opción no válida. Se asignará género como 'No especificado'.")
            Genero = "No especificado"

        Nombre = input("ingrese Nombre:  ")
        Apellido = input("ingrese Apellido:  ")
        Ntelefono = input("ingrese Nro de telefono: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento (D/M/A): ")

        dia, mes, año = fecha_nacimiento.split('/')

        Fnacimiento = f"{dia}/{mes}/{año}"
        Edad = input("ingrese Edad > ")
        diagnostico = input("Ingrese el dianostico para el paciente: ")
        tratamiento = input("Ingrese tratamiento: ")
        medicamentos = input("Ingrese medicamentos: ")
        usuarios ={
            'Identificacion': Identificacion,
            'Genero': Genero,
            'Nombre': Nombre,
            'Apellido' : Apellido,
            'Ntelefono' : Ntelefono,
            'Fnacimiento' : Fnacimiento,
            'Edad' : Edad,
            'diagnostico' : diagnostico,
            'tratamiento' : tratamiento,
            'medicamentos' : medicamentos
            
        }
    except ValueError:
        print("opcion invalidad")
        RUsuario(0)
    
    cf.AddData('Datas_usuarios', Identificacion,usuarios)
    gf.centromedico. get('Datas_usuarios').update({Identificacion:usuarios})
    if(bool(input('desea registrar otro Usuario S(si) o Enter (No):'))):
        RUsuario(0)
    else:
        U.menuUsuarios(0)
    
def searchData():
    criterio=input('Ingrese el Nro Identificacion del paciente :')
    data=(gf.centromedico.get('Datas_usuarios').get(criterio))
    return data

def modificar_data():
    data_U = searchData()
    Identificacion,Genero,Nombre,Apellido,Ntelefono,Fnacimiento,Edad,diagnostico,tratamiento,medicamentos = data_U.values()
    for key in data_U.keys():
        if (key != 'Identificacion' and key != 'Ntelefono'):
            if(bool(input(f'Desea modificar el {key} S(si) o Enter No: '))):
                data_U[key]=input(f'Ingrese el nuevo valor de {key} : ')
    gf.centromedico. get('Datas_usuarios').update({Identificacion:data_U})
    cf.updateFile(gf.centromedico)
    U.menuUsuarios

def eliminar_usuario():
    identificacion = input("Ingrese el número de identificación del usuario que desea eliminar: ")
    centromedico = gf.centromedico.get('Datas_usuarios')
    if identificacion in centromedico:
        confirmacion = input(f"¿Está seguro que desea eliminar al usuario con Identificación {identificacion}? (S/N): ").lower()
        if confirmacion == 's':
            del centromedico[identificacion]
            print("Usuario eliminado correctamente.")
            cf.updateFile(gf.centromedico)
        else:
            print("No se ha eliminado al usuario.")
    else:
        print(f"No se encontró ningún usuario con la Identificación {identificacion}.")
    gf.borrar_pantalla()