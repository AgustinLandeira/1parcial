#Las lámparas están al mismo precio de $35 pesos final.
#A. Si compra 6 o más lamparitas bajo consumo tiene un descuento del 50%.
#B. Si compra 5 lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
#C. Si compra 4 lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
#D. Si compra 3 lamparitas bajo consumo marca "ArgentinaLuz" el descuento es del 15%, si es “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
#E. Si el importe final con descuento suma más de $120 se debe sumar un 10% de ingresos brutos en informar del impuesto con el siguiente mensaje: ”IIBB Usted pago X”, siendo X el impuesto que se pagó.
#Curso de ingreso UTN FRA

lamparas= int (input("ingrese la cantidad de lamparas que necesitas: "))

importe = int(lamparas * 35)

marca= input("ingrese la marca bajo consumo(argentinaluz,felipelamparas o escriba otra)")

descuento=0

if lamparas >=6 :
    descuento = (importe * 50) /100
    importe_con_descuento= importe - descuento
    
    
elif lamparas==5 and marca=="argentinaluz":
     descuento = (importe * 40) /100
     importe_con_descuento= importe - descuento
else:
    descuento = (importe * 30) /100
    importe_con_descuento= importe - descuento

if lamparas == 4 and marca =="argentinaluz" or marca == "felipelamparas":
    descuento = (importe * 25) /100
    importe_con_descuento= importe - descuento
else:
    descuento = (importe * 20) /100
    importe_con_descuento= importe - descuento
    
if lamparas==3 and marca=="argentinaluz"  :
       descuento = (importe * 15) /100
       importe_con_descuento= importe - descuento
elif marca=="felipelamparas":
    descuento = (importe * 10) /100
    importe_con_descuento= importe - descuento
elif marca =="otra":
     descuento = (importe * 5) /100
     importe_con_descuento= importe - descuento


if importe_con_descuento >120:
    impuesto=(importe_con_descuento * 10)
    importe_con_ingresos_brutos= importe_con_descuento+impuesto
    print(f"el importe con descuento y impuesto en total es: {importe_con_ingresos_brutos}")
    
if(descuento==0) :
    importe_con_descuento= print(f"no hay descuento,solo sin descuento es: {importe}")


print(f"el importe con descuento es: {importe_con_descuento }")
print (f"uste consumio bajo la marca {marca}")


