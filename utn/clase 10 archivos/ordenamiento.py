# metodo de la burbuja
#numeros = [7,4,8,9,1]
'''numeros=["zoe","maria","ana"]
for i in range(len(numeros)-1): #verde
    #print(f"cuando i vale: {i}")
    for j in range(i+1,len(numeros)): #rojo
        if(numeros[i]> numeros[j]):
            auxiliar = numeros[i]
            numeros[i] = numeros[j] 
            numeros[j] = auxiliar
        
print(numeros)
'''
################################################################################################

lista=[{"nombre":"juan","edad":25},{"nombre":"ana","edad":32},{"nombre":"bduardo","edad":56}]

for i in range(len(lista)-1): #verde
    
    for j in range(i+1,len(lista)): #rojo
        if(lista[i]["nombre"] > lista[j]["nombre"]):
            lista[i],lista[j] = lista[j] ,lista[i]
            
        elif(lista[i]["edad"]==lista[j]["edad"]):
            if(lista[i]["nombre"]> lista[j]["nombre"]):
                lista[i],lista[j] = lista[j] ,lista[i]
print(lista)