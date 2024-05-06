import funciones.globales as Fg
import modules.data_C as Mc
import ui.citas as UIC
def registrocita(op):
    title="""
    --------------------------------
     *      REGISTRO CITA           *
    --------------------------------
    """
    Fg.borrar_pantalla()
    print(title)
    try:
        Identificacion = input("ingrese Nro de Identificacion : ")
        print("Seleccione el Género:")
        print("  1. Hombre")
        print("  2. Mujer")
        print("  3. Otro")
    
        opcion_genero = input("Ingrese el número de la opción correspondiente: ")
    
        if opcion_genero == "1":
            Genero = "Hombre"
        elif opcion_genero == "2":
            Genero = "Mujer"
        elif opcion_genero == "3":
            Genero = "Otro"
        else:
            print("Opción no válida. Se asignará género como 'No especificado'.")
            Genero = "No especificado"
    
        Nombre = input("ingrese Nombre: ")
        Apellido = input("ingrese Apellido: ")
        Ntelefono = input("ingrese Nro de telefono: ")
        Fnacimiento = input("ingrese fecha nacimento D/M/A: ")
        dia, mes, año = Fnacimiento.split('/')

        Fnacimiento = f"{dia}/{mes}/{año}"
        Edad = input("ingrese Edad: ")
        print("Seleccione el Horario:")
        print("  1. Mañana (0:00 - 11:59)")
        print("  2. Tarde (12:00 - 23:59)")
        opcion_horario = input("Ingrese la Opcion: ")
        
        if opcion_horario == "1":
                HorarioA = "Mañana"
                print("Horario de consulta: 0:00 - 11:59")
                print("tienes 20min por consulta")
        elif opcion_horario == "2":
                HorarioA = "Tarde"
                print("Horario de consulta: 12:00 - 23:59")
                print("tienes 20min por consulta")
        else:
                print("Opción no válida")
                registrocita(0)
        fecha= input("ingrese la fecha de la cita dia/mes :")
    except ValueError:
        print ("opcion invalidad")
        registrocita(0)
    menuEspecialidad=("*especialidades\n1.Pediatria\n2. Ginecologia\n3.Dermatologia\n4. Endocrinologia\n5. Optometria")
    if(op!=5):
        print(title)
        print(menuEspecialidad)
        try:
            opcion = int(input(">"))
        except ValueError:
            print("error de opcion")
            registrocita(0)
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
                    print("opciones ingresadas no pertenece al menu del centro medico")
                    registrocita(0)

        citas = {
            'Identificacion': Identificacion,
            'Genero': Genero,
            'Nombre': Nombre,
            'Apellido' : Apellido,
            'Ntelefono' : Ntelefono,
            'Fnacimiento' : Fnacimiento,
            'Edad' : Edad,
            'fecha' : fecha,
            'espacialidad' : especialidad
        }
    Mc.AddData("Datas_citas",Identificacion,citas)
    Fg.centroMedico.get("Datas_citas").update({Identificacion:citas})
    if(bool(input("desea agendar otra cita S(si) o Enter(no): "))):
        registrocita()
    else:
        UIC.Menucitas(0)

def searchData():
    datos= input('Ingrese el Nro de identificacion del paciente: ')
    data=(Fg.centroMedico.get('Datas_citas').get(datos))
    return data

def modificardatas():
    datasU = searchData()
    Identificacion, Genero, Nombre, Apellido, Ntelefono, Fnacimiento, Edad, fecha, especialidad = datasU.values()
    for key in datasU.keys():
        if (key != 'Identificacion'and key !='tiempo'):
            if(bool(input(f'Desea modificar el{key} S(si) o Enter No: '))):
                datasU[key]= input(f'Ingrese el nuevo valor para{key}: ')
    Fg.centroMedico.get("Datas_citas").update({Identificacion:datasU})
    Mc.updateFile(Fg.centroMedico)
    UIC.Menucitas

def eliminar_cita():
    identificacion = input("Ingrese el número de identificación del paciente de la cita que desea eliminar: ")
    centro_medico = Fg.centroMedico.get('Datas_citas')
    if identificacion in centro_medico:
        confirmacion = input(f"¿Está seguro que desea eliminar la cita del paciente con Identificación {identificacion}? (S/N): ").lower()
        if confirmacion == 's':
            del centro_medico[identificacion]
            print("Cita eliminada correctamente.")
            Mc.updateFile(Fg.centroMedico) 
        else:
            print("No se ha eliminado la cita.")
    else:
        print(f"No se encontró ninguna cita asociada al paciente con la Identificación {identificacion}.")
