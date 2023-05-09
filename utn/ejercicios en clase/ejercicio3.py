#Es la gala final de Gran Hermano y la producción nos pide un programa para contar
#los votos de los televidentes y saber cuál será el participante que ganará el juego.
#Los participantes finalistas son: Nacho, Julieta y Marcos.
#El televidente debe ingresar:
#● Nombre del votante
#● Edad del votante (debe ser mayor a 13)
#● Género del votante (masculino, femenino, otro)
#● El nombre del participante a quien le dará el voto positivo.
#No se sabe cuántos votos entrarán durante la gala.
#Se debe informar al usuario:
#A. El promedio de edad de las votantes de género femenino
#B. Cantidad de personas de género masculino entre 25 y 40 años que votaron a
#Nacho o Julieta.
#C. Nombre del votante más joven que votó a Nacho.
#D. Nombre de cada participante y porcentaje de los votos qué recibió.
#E. El nombre del participante que ganó el reality (El que tiene más votos)

seguir="si"
acumulador_edad_fem=0
contador_femenino=0
contador_personas=0
bandera_primero=True
contador_votos=0
votos_a_marcos=0
votos_a_julieta=0
votos_a_nacho=0



while seguir == "si":
  
  nombre_del_votante=input("ingrese su nombre porfavor: ")
  
  edad_del_votante= int(input("ingrese su edad: "))
  
  genero_del_votante=input("ingrese su genero: ")
  
  nombre_del_participante=input("a quien queres votar? nacho, julieta y marcos: ")
  
  while nombre_del_participante !="nacho" and nombre_del_participante !="julieta" and nombre_del_participante !="marcos":
      nombre_del_participante=input("ERROR,porfavor eliga devuelta")
  
  if genero_del_votante == "femenino":
      acumulador_edad_fem+=edad_del_votante
      contador_femenino=contador_femenino+1
      
  if nombre_del_participante =="nacho" or nombre_del_participante == "julieta":
      if edad_del_votante>=25 and edad_del_votante <=40:
          contador_personas=contador_personas+1
          
  if nombre_del_participante=="nacho"  :
      if bandera_primero== True:
          edad_minima=edad_del_votante
          nombre_joven=nombre_del_votante
          bandera_primero== False
          votos_a_nacho=votos_a_nacho+1
      else:
          if(edad_del_votante<edad_minima):
              edad_minima=edad_del_votante
              nombre_joven=nombre_del_votante
              votos_a_nacho=votos_a_nacho+1
  elif nombre_del_participante == "marcos":
      votos_a_marcos=votos_a_marcos+1
  else:
      votos_a_julieta=votos_a_julieta+1
  
      
      
  
  contador_votos=contador_votos+1
  seguir=input("desea ingresar mas datos? ")
  
  

promedio_edad_femenino=acumulador_edad_fem/contador_femenino
julieta= (votos_a_julieta*100) /contador_votos
marcos= (votos_a_marcos*100) / contador_votos
nacho=(votos_a_nacho*100) / contador_votos

if votos_a_julieta>votos_a_marcos and votos_a_julieta>votos_a_nacho:
    ganador="julieta"
elif votos_a_marcos>votos_a_nacho:
    ganador="marcos"
else:
    ganador="nachito"
       

print(f" el promedio de edad  del genero femenino es : {acumulador_edad_fem}")
print(f"la cantidad de personas que votaron a nacho o julieta son: {contador_personas}")
print (f"en nombre del mas joven que voto a nacho se llama: {nombre_joven}")
print (f"julieta recibio el {julieta}% de los votos")
print (f"marcos recibio el {marcos}% de los votos")
print (f"nacho recibio el {nacho}% de los votos")
print (f"el que tuvo mas votos fue: {ganador}")







