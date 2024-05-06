import funciones.Rcitas as fr

def Menucitas(op):
    title="""
    >>==== REGISTRO CITAS ====<<
    """
    Menucitasop = "1.Registrar cita\n2. Cancelar cita\n3 Cambiar informacion\n4 ver fecha de atencion\n5 ir al menu principal"
    if (op!=4):
        print (title)
        print (Menucitasop)
        try:
            op=int(input(">"))
        except ValueError:
            print("Opcion invalidad")
            Menucitas(0)
        else:
            match op:
                case 1:
                    fr.registrocita(0)
                case 2:
                    fr.eliminar_cita()
                case 3:
                    fr.modificardatas()
                case 4:
                    print("lunes a viernes")
                    print("Horario de consulta: 0:00 - 11:59")
                    print("Horario de consulta: 12:00 - 23:59")
                case 5:
                    import main
                    main.mainMenu(0)
                case _:
                    print("Opcion no valida" )
                    Menucitas(op)
                


