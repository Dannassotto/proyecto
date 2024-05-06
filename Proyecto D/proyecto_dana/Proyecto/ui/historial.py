import os
import json
import modules.corefiles as MC
import modules.data_M as MM
import modules.data_C as MCI
def menuhistorial(op):
    title = """
    *************
    * HISTORIAL *
    *************
    """
    menuhistorialop= ('VISUALIZAR\n1. citas\n2.usuarios\n3.medicos\n4.salir')
    if(op!=4):
        print(title)
        print(menuhistorialop)
        try:
            opcion = int(input(">"))
        except ValueError:
            print("error de opcion")
            menuhistorialop(0)
        else:
            if opcion ==1:
                MCI.ReadFile= "data/citasp.json"
                with open(MCI.ReadFile,"r") as uf:
                    datas= json.load(uf)
                    print(json.dumps(datas,indent=4))     
                    menuhistorial(0)
            elif opcion == 2:
                MC.ReadFile= "data/usuarios.json"
                with open(MC.ReadFile,"r") as uf:
                    datas= json.load(uf)
                    print(json.dumps(datas,indent=4)) 
                    menuhistorial(0)
            elif opcion == 3:
                MM.ReadFile= "data/especialistas.json"
                with open(MM.ReadFile,"r") as uf:
                    datas= json.load(uf)
                    print(json.dumps(datas,indent=4))
                    menuhistorial(0) 
            elif opcion == 4:
                    import main
                    main.mainMenu(0)
            else:
                    print("La opcion no es correcta")
                    menuhistorialop(opcion)