import funciones.globales as gf
import modules.data_M as mD
import ui.uidoctores as uD
def Rdoctores(op):
    title = """
     *****************************
     *  REGISTRO DE MEDICOS   *
     *****************************
    """
    gf.borrar_pantalla()
    print(title)
    try:
        Identificacion = int(input ("ingrese Nro de Identificacion : "))
        Nombre = input ("ingrese Nombre: ")
        Apellido = input("ingrese Apellido: ")
        Nconsultorio = int(input ("ingrese Nro del consultorios: "))
        CorreoE= input ("ingrese Correo Electronico: ")
        
        print("Seleccione el Horario:")
        print("  1. Mañana (0:00 - 11:59)")
        print("  2. Tarde (12:00 - 23:59)")

    
        opcion_horario = input("Ingrese la Opcion: ")
        
        if opcion_horario == "1":
                HorarioA = "Mañana"
                print("Horario de consulta: 0:00 - 11:59")
                print("tienes 20min de consulta")
        elif opcion_horario == "2":
                HorarioA = "Tarde"
                print("Horario de consulta: 12:00 - 23:59")
                print("tienes 20min de consulta")
        else:
                print("Opción no válida")
                Rdoctores(0)
    except ValueError:
        print("opcion invalida")             
    menuEspecialidad=("*especialidades\n1.Pediatria\n2. Ginecologia\n3.Dermatologia\n4. Endocrinologia\n5. Optometria")
    if(op!=6):
        print(title)
    print(menuEspecialidad)
    try: 
            opcion = int(input(">"))
    except ValueError:
            print("error de opcion")
            Rdoctores(0)
    else:
            match (opcion):
                case 1:
                    especialidad =("Pediatria")
                case 2:
                    especialidad = ("Ginecologia")
                case 3:
                    especialidad = ("Dermatologia")
                case 4:
                    especialidad = ("Endocrinologia")
                case 5:
                    especialidad = ("Optometria")
                case _:
                    print("opcion invalida")
                    Rdoctores(0)

    doctores = {
            'Identificacion': Identificacion,
            'Nombre': Nombre,
            'Apellido' : Apellido,
            'Nconsultorio' : Nconsultorio,
            'CorreoE' : CorreoE,
            'HorarioA' : HorarioA,
            "especialidad" : especialidad
            
        }
    
    mD.AddData("Datos_medicos",Identificacion,doctores)
    gf.Centromedico.get("Datos_medicos").update({Identificacion:doctores})
    if(bool(input("si quieres registrar otro especialista S(si) o Enter(no): "))):
            Rdoctores(0)
    else:
        uD.menuDoctores(0)
    
def searchData():
    datos= input('Ingrese el Nro de identificacion del paciente: ')
    data=(gf.Centromedico.get('Datos_medicos').get(datos))
    return data

def modificar_datas():
    datasM = searchData()
    Identificacion,Nombre,Apellido,Nconsultorio,CorreoE,HorarioA,especialidad= datasM.values()
    for key in datasM.keys():
        if (key != 'Identificacion'and key !='Nconsultorio'):
            if(bool(input(f'Desea modificar el{key} S(si) o Enter No: '))):
                datasM[key]= input(f'Ingrese el nuevo valor para{key}: ')
    gf.Centromedico.get("Datos_medicos").update({Identificacion:datasM})
    mD.updateFile(gf.Centromedico)
    uD.menuDoctores

def eliminar_medico():
    identificacion = input("Ingrese el número de identificación del médico que desea eliminar: ")
    centromedico = gf.Centromedico.get('Datos_medicos')
    if identificacion in centromedico:
        confirmacion = input(f"¿Está seguro que desea eliminar al médico con Identificación {identificacion}? (S/N): ").lower()
        if confirmacion == 's':
            del centromedico[identificacion]
            print("Médico eliminado correctamente.")
            mD.updateFile(gf.Centromedico)  
        else:
            print("No se ha eliminado al médico.")
    else:
        print(f"No se encontró ningún médico con la Identificación {identificacion}.")