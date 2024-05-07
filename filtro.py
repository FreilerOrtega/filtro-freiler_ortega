import json #importamos json para tener manejo de este formato 

with open("usuario.json","r") as miarachivo:  # este bloque de codigo nos permitira importar la informacion desde nuestrom archivo json 
  usuario=json.load(miarachivo)
  print("archivo obtenido con exito")
print(usuario)


with open("usuarios.json","w")as miarchivo: # este bloque de codigo  nos permitira gaurda o agregar informacion a nuestro json
  json.dump(usuario,miarchivo)
  print("archivo exportado")

print("--BIENVENIDO A MOVISTAR MAS CERCA DE TI--") # damos la bienvenida al administrador  a nuestro programa 
#mostramos el menu para que el usuario elija su opcion
print("----MENU----")
print("\n1.Manejo de usuarios\n2.historial de usuario\n3.personalizacion de servicios\n4.gestion de fidelizacion de clientes\n5.salir de el programa  ") 
z=int(input("elije una opcion por favor :"))
print("") # dependiendo de la opc elejida vamos mostrando las siguientes opciones con las  que cuenta cada modulo 
if z==1 :
    print("BIENVENIDO AL MANEJO DE USUARIOS QUE DESEAS HACER HOY ")
    print("\n1.crear un usuario \n2.ver los usuarios\n3.eliminar un usuario\n4.modificar usuario\n5.salir de el programa ")
    n=int(input("por favor seleciona una opcion :"))
    
    if n==1:
      print("")
      

    elif n==2:
       print(usuario)
    elif n==3:
       print("eliminar pendiente")
    elif n==4:
       print("modificar pendiente")
    elif n==5:
      exit

if z==2 : 
  print("----BIENVENIDO A HISTORIAL DE USUARIOS----") # este menu le dara la  posibilidad al administrador de ver el historial de los usuarios 
  print("\n1. ver usuarios registrados\n2.reclamos y sugerencias\n3.salir")   
  x=int(input("por favor elije una opcion :"))
  print("/////////////////////////////////////////////////////////////////////")
  if x==1:
    print("pendiente")

  if x==2:
    print("pendiente")
  elif x==3:
    exit     
elif z==3:
  print("---BIENBENIDO A PERZONALIZACION DE SERVICIOS---") # este menu servira para la perzonalizacion de servicios 
  print("/////////////////////////////////////////////////////////////////////")
  print("\n1.promociones y datos de clientes\n2.analizis de preferencias de los clientes\n3.salir de el programa")
  s=int(input("elije una opcion :"))

  if s== 1:
   print("pendiente")
  if s==2:
    print("pendiente ")
  elif s==3:
    print("pendiente") 
 
elif z==4:
  print("---BIENVENIDO A FIEDELIZACION DE LOS CLIENTES ---")
  print("/////////////////////////////////////////////////////////////////////")
  print("\n1.tiempo de vinculacion de los clientes a la empresa \n2.bonificacion para los clientes\n3.salir de el programa ")
  m=int(input("elije una opcion :"))
  if m==1:
    print("")
  if m==2:
    print("")
  elif m==3:
    exit


elif z==5:
 exit

 # hecho por freiler ortega cc.1010075774