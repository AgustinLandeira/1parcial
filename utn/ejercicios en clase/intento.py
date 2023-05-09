#print("esto funciona")
#nombre=input("ingrese su nombre: ")
#print(nombre)

#lista=list(["agus", "indepediente",2])
#for i in range(lista):
#  print(lista)
  
personas = [["Juan", 25], ["Maria", 30], ["Pedro", 20], ["Luisa", 28]]

personas.sort(key=lambda x: x[1])


print(personas)  



